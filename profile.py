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

# All in one network.
network = request.LAN("network0")

# Helpers for configuring each docker container
def requestContainer(name):
    node = request.DockerContainer(name)
    node.docker_extimage = 'ejoebstl/churp-cloudlab'
    iface = node.addInterface("if1")
    network.addInterface(iface)

def envSetup(node, id):
    node.docker.env = """
    PORT=%d
    MY_INDEX=%d
    NODES=%s
    DEGREE=%d
    """.format(PORT, id, nodeNames, D)

# Create Nodes
nodes = [requestContainer('bulletin')]
nodeNames = ['bulletin']

for n in range(1, N + 1):
    nodes += [requestContainer('node' + str(n))]
    nodeNames += ['node' + str(n)]

# Setup node task
envSetup(bulletin, 0)
bulletin.docker_cmd = "./runBulletin.sh"

for n in range(1, N + 1):
    envSetup(nodes[n], n)
    nodes[n].docker_cmd = "./runNode.sh"

pc.printRequestRSpec(request)