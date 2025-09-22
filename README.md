# CTF PCAP Password Challenge

A Capture The Flag (CTF) challenge involving network packet analysis to find hidden passwords and credentials.

## Challenge Description

You have been given a PCAP file (`challenge.pcap`) containing network traffic. Hidden within this traffic are multiple passwords and flags that you need to find. Your mission is to analyze the PCAP file and extract all the hidden credentials.

## Files Included

- `challenge.pcap` - The main challenge file containing network traffic with embedded passwords
- `find_passwords.py` - Analysis tool to help find passwords in PCAP files
- `create_challenge.py` - Script used to generate the challenge (for reference)

## How to Solve

1. **Manual Analysis**: Use tools like `tcpdump`, `wireshark`, or `tshark` to analyze the PCAP file
   ```bash
   tcpdump -r challenge.pcap -A
   ```

2. **Automated Analysis**: Use the provided password finder script
   ```bash
   python3 find_passwords.py challenge.pcap
   ```

3. **Look for**:
   - HTTP Basic Authentication (Base64 encoded credentials)
   - FTP login commands (USER/PASS)
   - Telnet login sessions
   - Any strings containing `flag{...}`

## Expected Flags

The challenge contains **3 flags** hidden in different protocols:
- HTTP Basic Authentication flag
- FTP login flag  
- Telnet login flag

## Tools and Techniques

### Common Tools for PCAP Analysis:
- `tcpdump` - Command line packet analyzer
- `wireshark` - GUI network protocol analyzer
- `tshark` - Terminal version of Wireshark
- `strings` - Extract printable strings from files

### Useful Commands:
```bash
# View readable content
tcpdump -r challenge.pcap -A

# Extract HTTP traffic
tcpdump -r challenge.pcap -A 'port 80 or port 8080'

# Extract FTP traffic
tcpdump -r challenge.pcap -A 'port 21 or port 2121'

# Extract Telnet traffic
tcpdump -r challenge.pcap -A 'port 23 or port 2323'

# Search for specific strings
strings challenge.pcap | grep -i flag
```

## Learning Objectives

- Understanding network protocol analysis
- Learning to extract credentials from network traffic
- Base64 decoding techniques
- Recognizing different authentication methods in network protocols

## Difficulty Level

**Beginner** - Suitable for those new to network analysis and PCAP file investigation.

Good luck and happy hunting! 🕵️‍♂️
