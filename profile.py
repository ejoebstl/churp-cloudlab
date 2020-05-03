'''Experiment profile for cloudlab experiments'''

import geni.portal as portal
import geni.rspec.pg as pg

N = 5 # NODE COUNT
D = 2 # DEGREE PARAMETER
PORT = 9090

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
nodes[0].addService(pg.Execute(shell="sh", command="PORT={} MY_INDEX={} NODES={} DEGREE={} cd /local/repository && bash ./runBulletin.sh 2>&1 > output.log".format(PORT, 0, ",".join(nodeNames), D)))

# Setup nodes task
for n in range(1, N + 1):
    nodes[n].addService(pg.Execute(shell="sh", command="PORT={} MY_INDEX={} NODES={} DEGREE={} cd /local/repository && bash ./runNode.sh 2>&1 > output.log".format(PORT, n, ",".join(nodeNames), D)))

pc.printRequestRSpec(request)