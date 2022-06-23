#!/usr/bin/env python
import os
import geni.portal as portal
import geni.rspec.pg as rspec
import geni.rspec.igext as IG
import geni.rspec.emulab.pnext as PN
import geni.urn as URN

tourDescription = "This the the profile's description"

tourInstructions = "These are the instructions"

BIN_PATH = "/local/repository/bin"
DEPLOY_SRS_WITH_ZMQ = os.path.join(BIN_PATH, "deploy-srs-withZMQ.sh")
DEPLOY_OPEN5GS = os.path.join(BIN_PATH, "deploy-open5gs.sh")
UBUNTU_1804_IMG = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD"
# node_type = [
#     ("d740",
#      "Emulab, d740"),
#     ("d430",
#      "Emulab, d430")
# ]

pc = portal.Context()
request = pc.makeRequestRSpec()

# Creatre 5gCore
cn = request.RawPC("cn")
cn.disk_image = UBUNTU_1804_IMG
cn.addService(rspec.Execute(shell="bash", command=DEPLOY_OPEN5GS))

# Create the UE
ue = request.RawPC("ue")
ue.disk_image = UBUNTU_1804_IMG
ue.addService(rspec.Execute(shell="bash", command=DEPLOY_SRS_WITH_ZMQ))

# Create eNodeB1
enb1 = request.RawPC("enb1")
enb1.disk_image = UBUNTU_1804_IMG
enb1.addService(rspec.Execute(shell="bash", command=DEPLOY_SRS_WITH_ZMQ))


# Create eNodeB2
enb2 = request.RawPC("enb2")
enb2.disk_image = UBUNTU_1804_IMG
enb2.addService(rspec.Execute(shell="bash", command=DEPLOY_SRS_WITH_ZMQ))

# Add instructions
tour = IG.Tour()
tour.Description(IG.Tour.MARKDOWN, tourDescription)
tour.Instructions(IG.Tour.MARKDOWN, tourInstructions)
request.addTour(tour)

pc.printRequestRSpec(request)
