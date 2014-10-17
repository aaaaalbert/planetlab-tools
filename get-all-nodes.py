"""
get-all-nodes.py looks up all nodes from the PlanetLab clearinghouse,
    and prints (and stores as `pickle`d file) all details about them.

Usage:
    python get-all-nodes.py PLANETLAB_USERNAME PLANETLAB_PASSWORD
"""
# For more details on what methods are used on which interface, please 
# see the PLC API tutorial, http://planet-lab.org/doc/plcapitut, and 
# PLC API docs, http://planet-lab.org/doc/plc_api

import xmlrpclib
import sys
import pprint
import pickle

# allow_none=True enables a non-standard extension to XML-RPC that 
# allows null values (None in Python) to be passed.
api_server = xmlrpclib.ServerProxy('https://www.planet-lab.org/PLCAPI/', 
    allow_none=True)

# Create an empty dictionary (XML-RPC struct)
auth = {}

# Specify password authentication
auth['AuthMethod'] = 'password'

# Username and password
try:
  auth['Username'] = sys.argv[1]
  auth['AuthString'] = sys.argv[2]
except IndexError:
  sys.exit("""Please provide a Planet-Lab username and password as first and 
second command-line arguments!""")


authorized = api_server.AuthCheck(auth)
if not authorized:
  sys.exit("Authorization failed with username '" + auth["Username"] + "'.")


nodes_overall = api_server.GetNodes(auth)
print "Found", len(nodes_overall), "nodes overall:"
pprint.pprint(nodes_overall)

print "Writing node dict to file...",
nodedict_file = open("nodedict.pickle", "w")
pickle.dump(nodes_overall, nodedict_file)
nodedict_file.close()
print "Done!"

