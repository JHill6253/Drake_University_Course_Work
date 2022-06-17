from scapy.all import *
print('you are now sniffing with John Hills sniffer')
a = IP()
a.dst='10.0.2.15'
b=ICMP()
p = a/b
send(p)
