# CTF Tools and Setup Guide

This guide helps you set up the necessary tools and environment for completing the CTF challenge.

## Required Tools

### 1. Network Analysis Tools

#### Wireshark (GUI Network Analyzer)
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install wireshark

# Add user to wireshark group
sudo usermod -a -G wireshark $USER

# CentOS/RHEL
sudo yum install wireshark-qt

# macOS (with Homebrew)
brew install --cask wireshark
```

#### TShark (Command-line Network Analyzer)
```bash
# Usually comes with Wireshark
tshark --version

# Standalone installation
sudo apt-get install tshark
```

#### TCPDump (Packet Capture)
```bash
# Ubuntu/Debian
sudo apt-get install tcpdump

# CentOS/RHEL
sudo yum install tcpdump

# macOS
brew install tcpdump
```

### 2. Web Application Testing Tools

#### Burp Suite Community Edition
```bash
# Download from: https://portswigger.net/burp/communitydownload
# Or install via package manager

# Ubuntu (Snap)
sudo snap install burp-suite

# Arch Linux
yay -S burpsuite
```

#### OWASP ZAP (Alternative to Burp)
```bash
# Ubuntu/Debian
sudo apt-get install zaproxy

# Download from: https://www.zaproxy.org/download/
# Java required
java -jar ZAP_2.x.x.jar
```

### 3. Network Reconnaissance Tools

#### Nmap (Network Scanner)
```bash
# Ubuntu/Debian
sudo apt-get install nmap

# CentOS/RHEL
sudo yum install nmap

# macOS
brew install nmap
```

#### Gobuster (Directory Brute Forcer)
```bash
# Ubuntu/Debian
sudo apt-get install gobuster

# From source
go install github.com/OJ/gobuster/v3@latest

# Download binary from: https://github.com/OJ/gobuster/releases
```

#### Dirb (Web Content Scanner)
```bash
# Ubuntu/Debian
sudo apt-get install dirb

# CentOS/RHEL
sudo yum install dirb
```

#### Nikto (Web Vulnerability Scanner)
```bash
# Ubuntu/Debian
sudo apt-get install nikto

# From GitHub
git clone https://github.com/sullo/nikto
cd nikto/program
perl nikto.pl -h http://target.com
```

### 4. SQL Injection Tools

#### SQLMap (Automated SQL Injection)
```bash
# Ubuntu/Debian
sudo apt-get install sqlmap

# From GitHub
git clone https://github.com/sqlmapproject/sqlmap.git
cd sqlmap
python3 sqlmap.py -u "http://target.com"
```

### 5. General Purpose Tools

#### cURL (HTTP Client)
```bash
# Usually pre-installed on most systems
curl --version

# Ubuntu/Debian
sudo apt-get install curl

# CentOS/RHEL
sudo yum install curl
```

#### jq (JSON Processor)
```bash
# Ubuntu/Debian
sudo apt-get install jq

# CentOS/RHEL
sudo yum install jq

# macOS
brew install jq
```

#### Base64 Tools
```bash
# Usually pre-installed
echo "SGVsbG8gV29ybGQ=" | base64 -d

# Windows
certutil -decode input.txt output.txt
```

## Environment Setup

### 1. Kali Linux (Recommended)
Kali Linux comes with most CTF tools pre-installed:
```bash
# Update package list
sudo apt update && sudo apt upgrade

# Install additional tools if needed
sudo apt install -y gobuster ffuf wfuzz
```

### 2. Ubuntu/Debian Setup
```bash
# Update system
sudo apt update && sudo apt upgrade

# Install essential tools
sudo apt install -y \
    nmap \
    wireshark \
    tcpdump \
    curl \
    jq \
    nikto \
    dirb \
    sqlmap \
    gobuster \
    python3 \
    python3-pip \
    git

# Install Python tools
pip3 install requests beautifulsoup4 urllib3
```

### 3. macOS Setup
```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install tools
brew install nmap wireshark tcpdump curl jq python3 git

# Install additional tools
pip3 install requests beautifulsoup4 sqlmap
```

## Browser Setup

### Firefox Extensions
1. **FoxyProxy** - Proxy management
2. **Wappalyzer** - Technology detection
3. **User-Agent Switcher** - Change user agent
4. **Cookie Manager** - Cookie manipulation

### Chrome Extensions  
1. **Proxy SwitchyOmega** - Proxy management
2. **Wappalyzer** - Technology detection
3. **EditThisCookie** - Cookie editor
4. **User-Agent Switcher** - Change user agent

## Wordlists

### Download Common Wordlists
```bash
# Create wordlists directory
mkdir -p ~/wordlists

# SecLists (comprehensive wordlist collection)
cd ~/wordlists
git clone https://github.com/danielmiessler/SecLists.git

# Dirb wordlists
sudo apt-get install dirbuster
# Wordlists location: /usr/share/dirbuster/wordlists/

# Common directories
wget https://raw.githubusercontent.com/v0re/dirb/master/wordlists/common.txt

# Big directory list
wget https://raw.githubusercontent.com/daviddias/node-dirbuster/master/lists/directory-list-2.3-medium.txt
```

## Network Configuration

### Set up Traffic Capture
```bash
# Check network interfaces
ip link show

# Set interface to promiscuous mode (for packet capture)
sudo ip link set eth0 promisc on

# Configure iptables for traffic routing (if needed)
sudo iptables -t nat -A OUTPUT -p tcp --dport 80 -j REDIRECT --to-port 8080
```

## Python Environment Setup

### Virtual Environment
```bash
# Create virtual environment
python3 -m venv ctf-env

# Activate environment
source ctf-env/bin/activate  # Linux/macOS
# ctf-env\Scripts\activate   # Windows

# Install required packages
pip install requests urllib3 beautifulsoup4 pycrypto
```

### Useful Python Libraries
```bash
pip install \
    requests \
    urllib3 \
    beautifulsoup4 \
    cryptography \
    pycrypto \
    base64 \
    hashlib \
    json \
    re
```

## Quick Verification

### Test Tool Installation
```bash
# Test network tools
nmap --version
wireshark --version
tcpdump --version

# Test web tools
curl --version
gobuster version
nikto -Version

# Test Python
python3 --version
pip3 --version
```

### Test Basic Functionality
```bash
# Test network connectivity to target
ping -c 4 192.168.29.153

# Test HTTP connectivity
curl -I http://192.168.29.153:5000/

# Test port accessibility
nmap -p 5000 192.168.29.153
```

## Troubleshooting

### Common Issues

#### Permission Denied for Packet Capture
```bash
# Add user to wireshark group
sudo usermod -a -G wireshark $USER
sudo chmod +x /usr/bin/dumpcap

# Alternative: run with sudo
sudo wireshark
sudo tcpdump -i any host 192.168.29.153
```

#### Tool Not Found
```bash
# Check if tool is in PATH
which nmap
which gobuster

# Add to PATH if needed
export PATH=$PATH:/usr/local/bin
echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc
```

#### Network Access Issues
```bash
# Check firewall settings
sudo ufw status
sudo iptables -L

# Test connectivity
telnet 192.168.29.153 5000
nc -v 192.168.29.153 5000
```

## CTF-Specific Setup

### Create Working Directory
```bash
mkdir -p ~/ctf-challenge
cd ~/ctf-challenge

# Create subdirectories
mkdir {traffic,payloads,flags,notes,scripts}
```

### Traffic Capture Setup
```bash
# Start packet capture for the challenge
sudo tcpdump -i any -w ~/ctf-challenge/traffic/challenge.pcap host 192.168.29.153 &
```

### Proxy Configuration
```bash
# Configure Burp Suite proxy
# Browser → Proxy Settings → Manual Configuration
# HTTP Proxy: 127.0.0.1 Port: 8080
# HTTPS Proxy: 127.0.0.1 Port: 8080
```

## Next Steps

1. **Test all tools** with the verification commands above
2. **Review the** [CTF_WALKTHROUGH.md](./CTF_WALKTHROUGH.md) for detailed methodology
3. **Start with reconnaissance** using nmap and basic HTTP requests
4. **Set up traffic capture** before beginning the challenge
5. **Configure proxy tools** (Burp Suite/OWASP ZAP) for request interception

## Additional Resources

- **OWASP Testing Guide**: https://owasp.org/www-project-web-security-testing-guide/
- **Burp Suite Documentation**: https://portswigger.net/burp/documentation
- **Wireshark User Guide**: https://www.wireshark.org/docs/wsug_html_chunked/
- **Nmap Network Scanning**: https://nmap.org/book/
- **SecLists Wordlists**: https://github.com/danielmiessler/SecLists