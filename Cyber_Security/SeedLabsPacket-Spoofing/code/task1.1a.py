#!/usr/bin/python3
from scapy.all import *
# Task 1.1A contianed task 1.1b filter implomentation already
#Author: John Hill
print("Sniffing packets with John")
def print_pkt(pkt):
    pkt.show()
pkt = sniff(filter='dst net 104.17.96.0/24',prn=print_pkt)
