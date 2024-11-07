# ICMPExfiltrator

ICMPExfiltrator is a Python-based project that demonstrates how data exfiltration can be achieved through ICMP packets. While ICMP (Internet Control Message Protocol) is typically used for network diagnostics (such as ping), this project illustrates how it can also be exploited to hide and transmit sensitive information within the ICMP payload. The project consists of a sender script to transmit data and a receiver script to capture and reconstruct the hidden data.

> **Disclaimer**: This project is for educational purposes only. Unauthorized data exfiltration and network interference are illegal and unethical. Use responsibly and only on networks where you have explicit permission.

## Features

- **Data Transmission via ICMP**: Sends data through ICMP Echo Request packets.
- **Data Reconstruction**: The receiver captures ICMP packets, reads the payload, and reconstructs the hidden information.

## Prerequisites

- **Python 3.x**
- **Scapy** library for packet crafting and network sniffing

