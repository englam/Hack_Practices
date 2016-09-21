import threading
from scapy.all import *


# our packet callback
def packet_callback(packet):
    #print (packet.show())


    if packet[TCP].payload:

        mail_packet = str(packet[TCP].payload)

        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            print "[*] Server: %s" % packet[IP].dst
            #print "[*] %s" % packet[TCP].payload
            print "[*] TCP: %s" % packet[TCP]





# fire up our sniffer
rec_mail = sniff(filter="tcp port 443", prn=packet_callback, store=0)
print (rec_mail)