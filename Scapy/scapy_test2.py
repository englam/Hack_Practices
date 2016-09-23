from scapy.all import *

pkt = sniff(count=1)

#Get Packet summary
print (pkt[0].summary())

# Packet info
print (pkt[0].show())

# Get ICMP info
#print ("#########################################################################")
#print (pkt[0][ICMP].summary())
#print ("#########################################################################")
#print (pkt[0][ICMP].show())

# Get commands
print ("Scapy Commands")
print (pkt[0].command())


# Get ttl , type and others............
print ("TTL and Type : ")
print (pkt[0][IP].ttl)
print (pkt[0][IP].type)


# Test Layer

for packet in pkt:
    if(packet.haslayer(ICMP)):
        print "ICMP Mode: " + str(packet.getlayer(ICMP).code)

