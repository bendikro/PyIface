#!/usr/bin/env python
from pyiface import getIfaces, Interface, IFF_UP

print 'All your interfaces'
allIfaces = getIfaces()
for iface in allIfaces:
    print iface

iff = Interface(name='eth0')
#iff.flags = iff.flags & IFF_UP
print iff
#iff.flags = iff.flags | IFF_UP | IFF_RUNNING
#iff.addr = (socket.AF_INET, sys.argv[1])
#print iff
#iff.netmask = (socket.AF_INET, sys.argv[2])
#iff.flags = iff.flags | IFF_UP
#print iff
#iff.flags = iff.flags & ~IFF_UP
#print iff
