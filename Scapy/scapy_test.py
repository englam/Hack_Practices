from scapy.all import *
a = sniff(filter="icmp and host 192.168.13.216", count=2)
print (a.summary())

b = sniff(count=50)
print(b.summary())


