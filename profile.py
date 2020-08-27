'''Experiment profile for cloudlab experiments'''

import geni.portal as portal
import geni.rspec.pg as pg

# Describe the parameter(s) this profile script can accept.
portal.context.defineParameter( "N", "Number of VMs", portal.ParameterType.INTEGER, 4)
portal.context.defineParameter( "SITES", "Number of SITES", portal.ParameterType.INTEGER, 2)

# Retrieve the values the user specifies during instantiation.
params = portal.context.bindParameters()

N = params.N # NODE COUNT
D = int(N/2) # DEGREE PARAMETER
PORT = 9090
SITES = params.SITES

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Helpers for configuring each docker container
def requestContainer(name):
    node = request.RawPC(name)
    return node

# Create Nodes
nodes = [requestContainer('bulletin')] # Bulletin
nodeips = ['192.168.1.254']

for n in range(1, N + 1):
    nodes += [requestContainer('node' + str(n))]
    nodeips += ['192.168.1.' + str(n)]

#request.Link(members=nodes) # TRY LAN

# Setup bulletin task
nodes[0].addService(pg.Execute(shell="sh", command="cd /local/repository && PORT={} MY_INDEX={} NODES={} DEGREE={} bash ./runBulletin.sh > output.log 2>&1".format(PORT, 0, ",".join(nodeips), D)))

# Setup nodes task
for n in range(1, N + 1):
    nodes[n].addService(pg.Execute(shell="sh", command="cd /local/repository && PORT={} MY_INDEX={} NODES={} DEGREE={} bash ./runNode.sh > output.log 2>&1".format(PORT, n, ",".join(nodeips), D)))


# Set node sites
for i in range(N + 1):
    nodes[i].Site('Site' + str(i % SITES + 1))


''' Networking '''

# Create an array for interfaces
ifaces = []

for i in range(N + 1):
    node = nodes[i]

    # Node networking
    iface = node.addInterface("eth1")
    iface.addAddress(pg.IPv4Address(nodeips[i], "255.255.255.0"))
    ifaces.append(iface)

lan = request.LAN("lan")
lan.bandwidth=100000

for iface in ifaces:
    lan.addInterface(iface)

    

pc.printRequestRSpec(request)
