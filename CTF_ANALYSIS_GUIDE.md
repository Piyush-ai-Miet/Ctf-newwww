# Indian Army Quest 2025 - CTF PCAP Analysis Guide

This repository contains tools and documentation for analyzing packet capture (pcap) files to extract passwords from HTTP traffic, specifically for the Indian Army Quest 2025 CTF challenge.

## Overview

The challenge involves analyzing network traffic captured in a pcap file to find hidden passwords transmitted over HTTP protocol. This is a common CTF (Capture The Flag) scenario where participants need to examine network communications to extract sensitive information.

## Tools Required

- **tshark**: Command-line network protocol analyzer (part of Wireshark)
- **Python 3**: For running the analysis script
- **tcpdump**: For packet capture (if creating new captures)

## Installation

```bash
sudo apt update
sudo apt install -y tshark tcpdump python3
```

## Usage

### Automated Analysis

Use the provided Python script for comprehensive analysis:

```bash
python3 analyze_pcap.py <pcap_file>
```

### Manual Analysis with tshark

1. **Extract HTTP requests and responses:**
```bash
tshark -r capture.pcap -Y "http.request or http.response" -T fields -e http.request.method -e http.request.uri -e http.host
```

2. **Look for HTTP POST data (often contains passwords):**
```bash
tshark -r capture.pcap -Y "http.request.method == POST" -T fields -e http.request.uri -e data.data
```

3. **Extract HTTP authentication headers:**
```bash
tshark -r capture.pcap -Y "http.authorization" -T fields -e http.authorization
```

4. **Search for specific keywords in HTTP traffic:**
```bash
tshark -r capture.pcap -Y "http contains \"password\" or http contains \"login\"" -V
```

## Common Password Locations in HTTP Traffic

### 1. Basic Authentication Headers
- Format: `Authorization: Basic <base64_encoded_username:password>`
- Decode using: `echo "base64string" | base64 -d`

### 2. URL Parameters (GET requests)
- Look for parameters like: `password=`, `pass=`, `pwd=`, `secret=`
- Example: `http://example.com/login?username=admin&password=secret123`

### 3. POST Form Data
- Form submissions often contain passwords in the request body
- Look for `application/x-www-form-urlencoded` content

### 4. Cookies
- Sometimes passwords or tokens are stored in cookies
- Format: `Cookie: sessionid=abc123; password=secret`

### 5. JSON Payloads
- Modern applications often use JSON for authentication
- Look for `{"username": "admin", "password": "secret123"}`

## Analysis Strategy for Indian Army Quest 2025

1. **Start with HTTP Overview:**
   - Get a general view of all HTTP traffic
   - Identify login pages, authentication endpoints

2. **Focus on Authentication:**
   - Look for login forms, authentication headers
   - Check for weak authentication methods

3. **Examine POST Requests:**
   - Most password submissions use POST method
   - Decode form data and JSON payloads

4. **Check for Encoded Data:**
   - Base64 encoding is common
   - URL encoding may hide passwords

5. **Look for Error Messages:**
   - Failed login attempts might reveal valid usernames
   - Server responses may leak information

## Common CTF Password Patterns

- Military-themed passwords (army, soldier, mission, etc.)
- Indian cultural references
- Date-based passwords (2025, quest2025, etc.)
- Simple patterns (admin, password123, secret)
- Base64 encoded strings

## Security Notes

This analysis is for educational and authorized CTF purposes only. The techniques demonstrated here should only be used on networks and systems you own or have explicit permission to test.

## Troubleshooting

### Permission Issues
```bash
sudo chmod +x analyze_pcap.py
```

### Missing Dependencies
```bash
# If tshark is not found
sudo apt install wireshark-common

# If Python script fails
python3 -m pip install --upgrade pip
```

### Large PCAP Files
For large files, filter traffic first:
```bash
tshark -r large_capture.pcap -Y "http" -w http_only.pcap
```

## Example Commands

Extract all HTTP passwords from a pcap file:
```bash
# Quick search for common password fields
tshark -r capture.pcap -Y "http" -T fields -e data.data | grep -i "password\|pass\|pwd"

# Decode base64 authentication
tshark -r capture.pcap -Y "http.authorization" -T fields -e http.authorization | cut -d' ' -f2 | base64 -d
```

## Expected Output Format

When a password is found, the analysis should provide:
- Source of the password (URL parameter, POST data, header, etc.)
- The actual password string
- Context (which HTTP request/response)
- Timestamp of the traffic

Good luck with the Indian Army Quest 2025 CTF challenge!