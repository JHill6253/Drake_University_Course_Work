#FacebookIP: 157.240.2.35
#!usr/bin/python
#Author: John Hill
from scapy.all import*
a = IP(dst='10.0.2.4',ttl = 1)
b = ICMP()
p = a/b
send(p)
