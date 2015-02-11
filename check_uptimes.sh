#!/bin/bash
#
# This script collects uptime statistics for Planet-Lab nodes.
#
# Interesting result output takes the form
#
# ``###'' HOSTNAME UPTIME_IN_SECONDS IDLE_TIME_IN_SECONDS UNIX_TIMESTAMP
#
# That is, three hash signs, the Planet-Lab machine's hostname,
# its uptime and idle time in seconds (from /proc/uptime), and the 
# current Unix time on the machine.
#
# Expect lots of SSH errors (despite of the pile of generous^W
# insecure options we provide). Also, lots of node names refuse 
# to resolve, although the Planet-Lab clearinghouse still advertises 
# them.

SLICENAME=poly_seattle
CREDENTIALS=~/.ssh/planetlab
HOSTLIST=`cat poly_seattle_pl_nodes.txt`

for NODE in $HOSTLIST ;
do ssh -i $CREDENTIALS -o ConnectTimeout=10 -o StrictHostKeyChecking=false -o UserKnownHostsFile=/dev/null -o PasswordAuthentication=no $SLICENAME@$NODE 'echo \#\#\# `hostname` `cat /proc/uptime` `date +%s`'
done

