#! /usr/bin/python
# Quick and dirty script that read's vhosts.txt and converts them to Nessus format hostname[ip-address] to be pasted into a scan
import socket, urlparse, re

fIn = open('vhosts.txt')

for line in fIn:
    if '/' in line:
        if (re.match('(?:http|https)://', line)):
            hName = urlparse.urlparse(line).hostname
        else:
            hName = urlparse.urlparse("http://" + line).hostname
    else:
        hName = line.rstrip('\n')

    
    try:
        ipAddr = socket.gethostbyname(hName)
        print hName + "[" + ipAddr + "]"
    except:
        pass
    
