#!/usr/bin/env python
import os
import geni.portal as portal
import geni.rspec.pg as rspec
import geni.rspec.igext as IG
import geni.rspec.emulab.pnext as PN
import geni.urn as URN

tourDescription = "This profile creates 4 nodes, 1 EPC, 2 eNodeBs and 1 UE." \
                  "All nodes are part of a LAN, with IPs 10.10.1.1-10.10.1.4"

tourInstructions = "These are the instructions"

BIN_PATH = "/local/repository/bin"
DEPLOY_SRS_WITH_ZMQ = os.path.join(BIN_PATH, "deploy-srs-withZMQ.sh")
DEPLOY_OPEN5GS = os.path.join(BIN_PATH, "install-open5gs.sh")
UBUNTU_1804_IMG = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD"
node_type = [
    ("d740",
     "Emulab, d740"),
    ("d430",
     "Emulab, d430")
]


pc = portal.Context()

pc.defineParameter("cn_node_type",
                   "Type of compute node for Open5GS CN",
                   portal.ParameterType.STRING,
                   node_type[0],
                   node_type)

pc.defineParameter("enb1_node", "PhantomNet NUC+B210 for first eNodeB",
                   portal.ParameterType.STRING, "nuc2", advanced=True)

pc.defineParameter("enb2_node", "PhantomNet NUC+B210 for second eNodeB",
                   portal.ParameterType.STRING, "nuc4", advanced=True)

pc.defineParameter("ue_node", "PhantomNet NUC+B210 for UE",
                   portal.ParameterType.STRING, "nuc1", advanced=True)

params = pc.bindParameters()
pc.verifyParameters()

request = pc.makeRequestRSpec()

# Create 5gCore
epc = request.RawPC("epc")
epc.disk_image = UBUNTU_1804_IMG
iface1 = epc.addInterface("eth1")
iface1.addAddress(rspec.IPv4Address("10.10.1.1", "255.255.255.0"))
#epc.addService(rspec.Execute(shell="bash", command=DEPLOY_SRS_WITH_ZMQ))

# Create eNodeB1
enb1 = request.RawPC("enb1")
enb1.disk_image = UBUNTU_1804_IMG
iface2 = enb1.addInterface("eth1")
iface2.addAddress(rspec.IPv4Address("10.10.1.2", "255.255.255.0"))
#enb1.addService(rspec.Execute(shell="bash", command=DEPLOY_SRS_WITH_ZMQ))

# Create eNodeB2
enb2 = request.RawPC("enb2")
enb2.disk_image = UBUNTU_1804_IMG
iface3 = enb2.addInterface("eth1")
iface3.addAddress(rspec.IPv4Address("10.10.1.3", "255.255.255.0"))
#enb2.addService(rspec.Execute(shell="bash", command=DEPLOY_SRS_WITH_ZMQ))

# Create the UE
ue = request.RawPC("ue")
ue.disk_image = UBUNTU_1804_IMG
iface4 = ue.addInterface("eth1")
iface4.addAddress(rspec.IPv4Address("10.10.1.4", "255.255.255.0"))
#ue.addService(rspec.Execute(shell="bash", command=DEPLOY_SRS_WITH_ZMQ))

# Setup LAN
link = request.LAN("lan")
link.addInterface(iface1)
link.addInterface(iface2)
link.addInterface(iface3)
link.addInterface(iface4)
link.link_multiplexing = True
link.vlan_tagging = True
link.best_effort = True

# Add instructions
tour = IG.Tour()
tour.Description(IG.Tour.MARKDOWN, tourDescription)
tour.Instructions(IG.Tour.MARKDOWN, tourInstructions)
request.addTour(tour)

pc.printRequestRSpec(request)
