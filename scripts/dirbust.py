#!/usr/bin/python

import sys
import os
import subprocess

if len(sys.argv) != 3:
    print "Usage: dirbust.py <target url> <scan name>"
    sys.exit(0)

url = str(sys.argv[1])
name = str(sys.argv[2])
#folders = ["/usr/share/dirb/wordlists", "/usr/share/dirb/wordlists/vulns"]

found = []
print "INFO: Starting dirb scan for " + url
#for folder in folders:
#    for filename in os.listdir(folder):
filename = "/usr/share/seclists/Discovery/Web-Content/common.txt"

outfile = " -o " + "results/exam/" + name + "_dirb_common.txt" 
DIRBSCAN = "dirb %s %s %s -S -r" % (url, filename, outfile)
try:
    results = subprocess.check_output(DIRBSCAN, shell=True)
    resultarr = results.split("\n")
    for line in resultarr:
        if "+" in line:
	    if line not in found:
	        found.append(line)
except:
    pass

try:
    if found[0] != "":
        print "[*] Dirb found the following items..."
        for item in found:
            print "   " + item
except:
    print "INFO: No items found during dirb scan of " + url		
