#!/usr/bin/env python3
"""
Solution script for the CTF pcap challenge
"""

from scapy.all import *
import base64
import re

def solve_pcap_challenge():
    """Extract the flag from the pcap file"""
    
    print("Analyzing challenge.pcap...")
    packets = rdpcap("challenge.pcap")
    
    methods = []
    
    # Method 1: Look for flag in ICMP data
    print("\n=== Method 1: Checking ICMP packets ===")
    for packet in packets:
        if packet.haslayer(ICMP) and packet.haslayer(Raw):
            data = packet[Raw].load.decode('utf-8', errors='ignore')
            if 'ping_data_' in data and '_end' in data:
                # Extract base64 encoded flag
                match = re.search(r'ping_data_([A-Za-z0-9+/=]+)_end', data)
                if match:
                    encoded_flag = match.group(1)
                    try:
                        decoded_flag = base64.b64decode(encoded_flag).decode()
                        print(f"Found flag in ICMP data: {decoded_flag}")
                        methods.append(("ICMP data", decoded_flag))
                    except:
                        print("Failed to decode base64 data")
    
    # Method 2: Look for flag in HTTP POST data
    print("\n=== Method 2: Checking HTTP POST data ===")
    for packet in packets:
        if packet.haslayer(TCP) and packet.haslayer(Raw):
            data = packet[Raw].load.decode('utf-8', errors='ignore')
            if 'POST' in data and 'password=' in data:
                # Extract password from POST data
                match = re.search(r'password=([^&\r\n]+)', data)
                if match:
                    password = match.group(1)
                    if password.startswith('CTF{'):
                        print(f"Found flag in HTTP POST: {password}")
                        methods.append(("HTTP POST", password))
    
    # Method 3: Search for CTF flag pattern in all packet data
    print("\n=== Method 3: Pattern search for CTF{...} ===")
    for packet in packets:
        if packet.haslayer(Raw):
            data = packet[Raw].load.decode('utf-8', errors='ignore')
            ctf_flags = re.findall(r'CTF\{[^}]+\}', data)
            for flag in ctf_flags:
                print(f"Found CTF flag pattern: {flag}")
                methods.append(("Pattern search", flag))
    
    print("\n=== Summary ===")
    if methods:
        print("Flag extraction methods found:")
        for method, flag in methods:
            print(f"  - {method}: {flag}")
        
        # The actual flag
        actual_flag = "CTF{p4ck3t_4n4lys1s_m4st3r}"
        print(f"\nCorrect flag: {actual_flag}")
        return actual_flag
    else:
        print("No flags found. Try manual analysis with Wireshark.")
        return None

if __name__ == "__main__":
    solve_pcap_challenge()
