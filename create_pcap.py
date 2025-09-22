#!/usr/bin/env python3
"""
Script to create a CTF pcap file with hidden flag/password
"""

from scapy.all import *
import base64

def create_ctf_pcap():
    """Create a pcap file with hidden flag for CTF challenge"""
    
    # CTF flag/password hidden in the pcap
    flag = "CTF{p4ck3t_4n4lys1s_m4st3r}"
    
    packets = []
    
    # Create some normal looking HTTP traffic
    packets.append(Ether()/IP(src="192.168.1.100", dst="8.8.8.8")/TCP(sport=12345, dport=80)/"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    packets.append(Ether()/IP(src="8.8.8.8", dst="192.168.1.100")/TCP(sport=80, dport=12345)/"HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, World!")
    
    # Create DNS queries
    packets.append(Ether()/IP(src="192.168.1.100", dst="8.8.8.8")/UDP(sport=12346, dport=53)/DNS(rd=1, qd=DNSQR(qname="example.com")))
    packets.append(Ether()/IP(src="8.8.8.8", dst="192.168.1.100")/UDP(sport=53, dport=12346)/DNS(qr=1, qd=DNSQR(qname="example.com"), an=DNSRR(rrname="example.com", rdata="93.184.216.34")))
    
    # Hide the flag in ICMP data
    flag_encoded = base64.b64encode(flag.encode()).decode()
    packets.append(Ether()/IP(src="192.168.1.100", dst="192.168.1.1")/ICMP()/f"ping_data_{flag_encoded}_end")
    
    # Add some more normal traffic to make it less obvious
    packets.append(Ether()/IP(src="192.168.1.100", dst="192.168.1.1")/ICMP()/"normal ping data")
    
    # Hide flag in HTTP POST data
    post_data = f"username=admin&password={flag}&login=true"
    packets.append(Ether()/IP(src="192.168.1.100", dst="10.0.0.1")/TCP(sport=12347, dport=80)/f"POST /login HTTP/1.1\r\nHost: ctf-server.local\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(post_data)}\r\n\r\n{post_data}")
    
    # Add response
    packets.append(Ether()/IP(src="10.0.0.1", dst="192.168.1.100")/TCP(sport=80, dport=12347)/"HTTP/1.1 302 Found\r\nLocation: /dashboard\r\n\r\n")
    
    # Write to pcap file
    wrpcap("challenge.pcap", packets)
    print(f"Created challenge.pcap with {len(packets)} packets")
    print(f"Hidden flag: {flag}")
    
    # Create a solution script
    create_solution_script(flag)

def create_solution_script(flag):
    """Create a script that shows how to extract the flag"""
    solution = f'''#!/usr/bin/env python3
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
    print("\\n=== Method 1: Checking ICMP packets ===")
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
                        print(f"Found flag in ICMP data: {{decoded_flag}}")
                        methods.append(("ICMP data", decoded_flag))
                    except:
                        print("Failed to decode base64 data")
    
    # Method 2: Look for flag in HTTP POST data
    print("\\n=== Method 2: Checking HTTP POST data ===")
    for packet in packets:
        if packet.haslayer(TCP) and packet.haslayer(Raw):
            data = packet[Raw].load.decode('utf-8', errors='ignore')
            if 'POST' in data and 'password=' in data:
                # Extract password from POST data
                match = re.search(r'password=([^&\\r\\n]+)', data)
                if match:
                    password = match.group(1)
                    if password.startswith('CTF{{'):
                        print(f"Found flag in HTTP POST: {{password}}")
                        methods.append(("HTTP POST", password))
    
    # Method 3: Search for CTF flag pattern in all packet data
    print("\\n=== Method 3: Pattern search for CTF{{...}} ===")
    for packet in packets:
        if packet.haslayer(Raw):
            data = packet[Raw].load.decode('utf-8', errors='ignore')
            ctf_flags = re.findall(r'CTF\\{{[^}}]+\\}}', data)
            for flag in ctf_flags:
                print(f"Found CTF flag pattern: {{flag}}")
                methods.append(("Pattern search", flag))
    
    print("\\n=== Summary ===")
    if methods:
        print("Flag extraction methods found:")
        for method, flag in methods:
            print(f"  - {{method}}: {{flag}}")
        
        # The actual flag
        actual_flag = "{flag}"
        print(f"\\nCorrect flag: {{actual_flag}}")
        return actual_flag
    else:
        print("No flags found. Try manual analysis with Wireshark.")
        return None

if __name__ == "__main__":
    solve_pcap_challenge()
'''
    
    with open("solve_pcap.py", "w") as f:
        f.write(solution)
    print("Created solve_pcap.py - solution script")

if __name__ == "__main__":
    create_ctf_pcap()