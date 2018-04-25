#!/usr/bin/python
import sys
import subprocess

if len(sys.argv) != 2:
    print "Usage: %s  <ip address>" % sys.argv[0]
    sys.exit(0)

ip = sys.argv[1]
cmd = "nmap --top-ports 10 %s --open" %(ip)
results = subprocess.check_output (cmd, shell=True)
resultsfile = "results/" + ip + "_lightscan.txt"
f = open(resultsfile, "w")
f.write(results)
f.close

