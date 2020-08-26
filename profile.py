'''Experiment profile for cloudlab experiments'''

import geni.portal as portal
import geni.rspec.pg as pg

# Describe the parameter(s) this profile script can accept.
portal.context.defineParameter( "N", "Number of VMs", portal.ParameterType.INTEGER, 4)

# Retrieve the values the user specifies during instantiation.
params = portal.context.bindParameters()

N = params.N # NODE COUNT
D = int(N/2) # DEGREE PARAMETER
PORT = 9090
SITES = 2

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Helpers for configuring each docker container
def requestContainer(name):
    node = request.XenVM(name)
    return node

# Create Nodes
nodes = [requestContainer('bulletin')]
nodeNames = ['bulletin']

for n in range(1, N + 1):
    nodes += [requestContainer('node' + str(n))]
    nodeNames += ['node' + str(n)]

request.Link(members=nodes)

# Setup bulletin task
nodes[0].addService(pg.Execute(shell="sh", command="cd /local/repository && PORT={} MY_INDEX={} NODES={} DEGREE={} bash ./runBulletin.sh > output.log 2>&1".format(PORT, 0, ",".join(nodeNames), D)))

# Setup nodes task
for n in range(1, N + 1):
    nodes[n].addService(pg.Execute(shell="sh", command="cd /local/repository && PORT={} MY_INDEX={} NODES={} DEGREE={} bash ./runNode.sh > output.log 2>&1".format(PORT, n, ",".join(nodeNames), D)))


# Set node sites
for n in range(N + 1):
    nodes[n].Site('Site' + str(n % SITES + 1))
    

pc.printRequestRSpec(request)
