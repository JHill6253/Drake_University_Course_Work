#!usr/bin/python
#Author: John Hill
from scapy.all import*
#Function shows initial packets and then shows spoofed packets
def spoof_pkt(pkt):
    if ICMP in pkt and pkt[ICMP].type == 8:
        print('LETS SNIFF AND SPOOF SON!')
        print('Input...')
        print('Src IP: ', pkt[IP].src)
        print('Dst IP:', pkt[IP].dst)

        ip = IP(src = pkt[IP].dst, dst = pkt[IP].src, ihl = pkt[IP].ihl)
        icmp = ICMP(type=0, id = pkt[ICMP].id, seq = pkt[ICMP].seq)
        data = pkt[Raw].load
        newpkt = ip/icmp/data

        print('Output...')
        print('Src IP', newpkt[IP].src)
        print('dst IP', newpkt[IP].dst)
        send(newpkt, verbose = 0)
pkt = sniff(filter='icmp and src host 10.0.2.4',prn=spoof_pkt)
