#Christmas tree
from scapy.all import *
from random import randint

template = IP(dst="192.168.13.195")/TCP()

template[TCP].flags ="UFP"

xmas =[]

for packets in range(0,1000):
    #print(template.show())
    xmas.extend(template)
    xmas[packets].dport = randint(1,65535)

#print(xmas)
send(xmas)
