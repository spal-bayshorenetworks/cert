#!/usr/bin/python
import sys
import subprocess

if len(sys.argv) != 3:
    print "Usage: %s  <ip address> <dns server>" % sys.argv[0]
    sys.exit(0)

ip = sys.argv[1]
dns = sys.argv[2]
cmd = "nmap -p- -sV %s --reason --dns-server %s" %(ip, dns)
results = subprocess.check_output (cmd, shell=True)
resultsfile = "results/" + ip + "_heavyscan.txt"
f = open(resultsfile, "w")
f.write(results)
f.close

