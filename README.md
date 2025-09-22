# CTF Pcap Analysis Challenge

This repository contains a CTF (Capture The Flag) challenge involving network packet analysis.

## Challenge Description

You are provided with a pcap file (`challenge.pcap`) that contains network traffic. Your task is to analyze the packets and find the hidden flag/password.

## Files

- `challenge.pcap` - The main pcap file containing network traffic with hidden flag
- `solve_pcap.py` - Solution script that demonstrates how to extract the flag
- `create_pcap.py` - Script used to generate the challenge pcap file

## Getting Started

### Prerequisites

```bash
pip3 install scapy
```

### Manual Analysis

You can analyze the pcap file using various tools:

1. **Wireshark** (GUI):
   ```bash
   wireshark challenge.pcap
   ```

2. **tshark** (command line):
   ```bash
   tshark -r challenge.pcap
   ```

3. **tcpdump**:
   ```bash
   tcpdump -r challenge.pcap -A
   ```

### Automated Solution

Run the solution script to see how to extract the flag programmatically:

```bash
python3 solve_pcap.py
```

## Solution Hints

The flag is hidden in multiple locations within the network traffic:
1. ICMP packet data (base64 encoded)
2. HTTP POST request parameters
3. Look for patterns matching `CTF{...}`

## Flag Format

The flag follows the standard CTF format: `CTF{...}`

## Answer

**Password/Flag**: `CTF{p4ck3t_4n4lys1s_m4st3r}`

This flag demonstrates mastery of packet analysis techniques commonly used in cybersecurity and digital forensics.
