import scapy
import sys
import socket

from scapy.all import *
from scapy.all import IP, ICMP, sniff

data_receiver = []

def packet_callback(packet):
    if packet.haslayer(ICMP) and packet[ICMP].type == 8:
        try:
            playload =bytes(packet[ICMP].playload).decode('UTF-8' , errors='ignore')
            print(f"Recived : {playload}")
            data_receiver.append(playload)
        except AttributeError:
            print("no playload found")
            
def receive_data():
    print("wating for ICMP packets .....")
    sniff(filter="icmp", prn=packet_callback, store=0, count=10)

if __name__ == "__main__":
    receive_data()
    
