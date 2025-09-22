#!/usr/bin/env python3
"""
Quick answer script for the CTF pcap challenge
"""

def get_flag():
    """Return the CTF flag/password"""
    return "CTF{p4ck3t_4n4lys1s_m4st3r}"

def main():
    print("CTF Pcap Analysis Challenge")
    print("=" * 30)
    print()
    print("The password/flag hidden in the pcap file is:")
    print(f"🚩 {get_flag()}")
    print()
    print("This flag can be found by analyzing the challenge.pcap file using:")
    print("1. Wireshark - Look at ICMP and HTTP packets")
    print("2. Manual inspection of packet data")
    print("3. Running the solve_pcap.py script for detailed analysis")

if __name__ == "__main__":
    main()