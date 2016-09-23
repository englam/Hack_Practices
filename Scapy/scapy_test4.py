from scapy.all import *

IP1 = IP()
print (IP1.show())

TCP1 = IP()/TCP()
print (TCP1.show())

TCP_Payload = IP()/TCP()/"AAAAA"
print(TCP_Payload.show())

send(TCP_Payload)