from netaddr import *
import socket

ipv4_addrerss = "192.168.13.103"
ipv6_address = "2001::1"

#check IPv4
ipv4 = IPAddress(ipv4_addrerss)
print (ipv4.version)
print (ipv4.words)

#check IPv6 address
ipv6 = IPAddress(ipv6_address)
print (ipv6.version)

# 2 , Binary
ip = IPNetwork("192.168.13.103/24")

print (ip.ip.bits())
Binary = ip.ip.bits()
print (Binary)

Binary2 = ip.ip.bin
print (Binary2)


# 16 , HEX
hex_test = int(ipv4)
print (hex_test)

hex_transfer = hex(hex_test)
print (hex_transfer)



#################Check IP Subnet####################

for ipv4_addrerss in IPNetwork("192.168.13.103/32"):
    print ("Single IP Test")

i = 0
for ipv4_addrerss in IPNetwork("192.168.13.0/24"):
    print ("Subnet IP Test Number: %d" %(i))
    i+=1