# CTF Flags Quick Reference

## All Flags

| Flag Number | Flag Value | Challenge Type |
|-------------|------------|----------------|
| Flag1 | `TCQ2025{S3Cur1ty_Br3@k_P@55ed}` | Authentication Bypass |
| Flag2 | `TCQ2025{F!ow3r#92@tY8&Vk}` | Hidden Content Discovery |
| Flag3 | `TCQ2025{Y0u_kn0w_i5_th15_RaC3}` | Race Condition |
| Flag4 | `TCQ2025{PwN_2_0wN_N0w_Y0u_ar3_5t3M}` | Privilege Escalation |
| Flag5 | `TCQ2025{D4Y_0_T0_zeR0_d4Y}` | Zero-Day Exploitation |

## Target Endpoints

- **Main Server**: http://192.168.29.153:5000/
- **Page Endpoint**: http://192.168.29.153:5000/page

## Quick Start Commands

```bash
# Initial reconnaissance
nmap -sC -sV 192.168.29.153

# Directory enumeration
gobuster dir -u http://192.168.29.153:5000/ -w /usr/share/wordlists/dirb/common.txt

# Web vulnerability scan
nikto -h http://192.168.29.153:5000/

# Capture network traffic
sudo tcpdump -i any -w ctf_traffic.pcap host 192.168.29.153

# Basic HTTP requests
curl -I http://192.168.29.153:5000/
curl http://192.168.29.153:5000/page
```

## Flag Patterns Analysis

- All flags follow the format: `TCQ2025{...}`
- Flags contain alphanumeric characters and special symbols
- Case sensitivity is important
- Some flags use leet speak (3 for E, 0 for O, etc.)

For detailed methodology and step-by-step instructions, see [CTF_WALKTHROUGH.md](./CTF_WALKTHROUGH.md)