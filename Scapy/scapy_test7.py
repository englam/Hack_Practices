from scapy.all import *
import random

host = "www.facebook.com"
port_range = [22,23,80,443,3389]

for des_port in port_range:
    src_port = random.randint(1024,65534)
    resp = sr1(IP(dst=host)/TCP(sport=src_port,dport=des_port,flags="S"))
    #test = sr1(IP(dst=host)/TCP(sport=src_port,dport=des_port,flags="S"))
    #print (test.haslayer(TCP))


    if(str(type(resp)) == "<type 'NoneType>"):
        print (host + " : " +str(des_port) + "is filtered")
    elif(resp.haslayer(TCP)):
        if(resp.getlayer(TCP).flags == 0x12):
            send_rst = sr(IP(dst=host)/TCP(sport=src_port,dport=des_port,flags="R"),timeout=1, verbose=0)
            print (host + " : " +str(des_port) + " is open")
        elif(resp.getlayer(TCP).flags == 0x14):
            print (host + " : " + str(des_port) + " is closed")
    elif(resp.haslayer(ICMP)):
        if(int(resp.getlayer(ICMP).type) ==3 and int(resp.gatlayer(ICMP).code) in [1,2,3,9,10,13]):
            print (host + " : " + str(des_port) + "is filtered ")



