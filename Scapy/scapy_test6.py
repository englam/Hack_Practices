# -*- coding: utf-8 -*-
#dns , qd = query domain , sport = source port, dport =des port
from scapy.all import *

dns = sr1(IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname="www.thepacketgeek.com")),verbose=0)
print (dns.show())
print (dns[DNS].summary())

