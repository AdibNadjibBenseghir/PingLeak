import scapy
import sys
from scapy.all import IP, ICMP, send

def sendy(ip_dest, data, fragment_size=64):
    fragments = [data[i:i+fragment_size] for i in range(0, len(data), fragment_size)]
    
    for i, fragment in enumerate(fragments):
        packet = IP(dst=ip_dest) / ICMP(type=8) / fragment
        send(packet)
        print(f"pkt {i+1}/{len(fragments)} sent with payload : {fragment}")
        
if __name__=="__main__":
    if len(sys.argv) < 3:
        print("We use sender.py on --IP DEST-- --FILE--")
        sys.exit(1)
    ip_dest = sys.argv[1]
    file_path = sys.argv[2]
    
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        sendy(ip_dest, data)
    except FileNotFoundError:
        print("ERREUR file not found")