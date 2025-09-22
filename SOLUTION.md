# CTF PCAP Challenge - Solution Guide

## Challenge Solution

This document provides the complete solution for the PCAP password challenge.

### Flags Found

1. **HTTP Basic Authentication Flag**
   - **Location**: HTTP Authorization header
   - **Encoded**: `Y3RmdXNlcjpmbGFne2Jhc2ljX2F1dGhfc2VjcmV0fQ==`
   - **Decoded**: `ctfuser:flag{basic_auth_secret}`
   - **Flag**: `flag{basic_auth_secret}`

2. **FTP Password Flag**
   - **Location**: FTP PASS command
   - **Protocol**: Plain text FTP
   - **Command**: `PASS flag{ftp_password_hidden}`
   - **Flag**: `flag{ftp_password_hidden}`

3. **Telnet Password Flag**
   - **Location**: Telnet login session
   - **Protocol**: Plain text Telnet
   - **Login**: `admin` with password `flag{telnet_admin_pass}`
   - **Flag**: `flag{telnet_admin_pass}`

### Step-by-Step Solution

#### Method 1: Using the provided script
```bash
python3 find_passwords.py challenge.pcap
```

#### Method 2: Manual analysis with tcpdump
```bash
# View all readable content
tcpdump -r challenge.pcap -A

# Look for Base64 patterns and decode them
echo "Y3RmdXNlcjpmbGFne2Jhc2ljX2F1dGhfc2VjcmV0fQ==" | base64 -d
```

#### Method 3: Using strings command
```bash
strings challenge.pcap | grep -i flag
```

### Network Protocols Analyzed

1. **HTTP (Port 8080)**
   - Contains Basic Authentication header
   - Credentials encoded in Base64
   - Need to decode to get username:password

2. **FTP (Port 2121)**
   - Plain text protocol
   - USER and PASS commands visible
   - Password directly visible in PASS command

3. **Telnet (Port 2323)**
   - Plain text protocol  
   - Login prompt and password exchange
   - Password sent in clear text

### Key Learning Points

- **Base64 Encoding**: HTTP Basic Auth uses Base64 encoding for credentials
- **Plain Text Protocols**: FTP and Telnet send passwords in clear text
- **Packet Analysis**: Different protocols expose credentials in different ways
- **CTF Flags**: Look for patterns like `flag{...}` in network traffic

### Tools Used

- `tcpdump` for packet analysis
- `base64` for decoding
- `strings` for text extraction
- Custom Python script for automated analysis

### Security Implications

This challenge demonstrates why:
- Plain text protocols are insecure
- Network traffic should be encrypted
- Credentials can be easily intercepted
- HTTPS/TLS should be used for web traffic
- Secure protocols (SFTP, SSH) should replace insecure ones (FTP, Telnet)

---

**Total Flags**: 3
**Difficulty**: Beginner
**Time to Solve**: 10-30 minutes