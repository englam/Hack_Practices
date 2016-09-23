from scapy.all import *

# sniffer arp filter
'''
arp_filter = sniff(count=1, filter="arp")
print(arp_filter.summary())
print ("#############ARP Show##################")
print(arp_filter[0].show())

print ("##############ARP commands################")
print(arp_filter[0].command())
'''

# Send ARP

arp_packet = ARP()
arp_packet.hwarc = "54:ab:3a:01:98:6d"
arp_packet.pdst = "192.168.1.1"
arp_packet.dst = "ff:ff:ff:ff:ff:ff"

print (arp_packet.show())

send(arp_packet)

#ARP  ,  op=1 -----who-has  --means ask ,  op=2 ---------is at --means my location

def arp_display(packet):
    if packet[ARP].op == 1:
        return "Request: " + packet[ARP].psrc + " is asking about " + packet[ARP].pdst
    if packet[ARP].op == 2:
        return "Response: " + packet[ARP].hwsrc + " has address: " + packet[ARP].psrc

print sniff(prn=arp_display, filter="arp", store=0, count=10)


#ping 1 packet

ping_test = IP(dst="192.168.1.1")/ICMP()
sr1(ping_test)

#continue ping
res_ping = srloop(ping_test,count=5)