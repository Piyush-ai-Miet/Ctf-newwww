# Indian Cyber Quest 2025 - CTF Challenge

A comprehensive Capture The Flag (CTF) web application designed for the Indian Cyber Quest 2025. This challenge contains 5 flags hidden using various cybersecurity techniques and vulnerabilities.

## 🎯 Challenge Overview

This CTF teaches participants about common web application vulnerabilities and security concepts including:
- Weak authentication and password attacks
- Data encoding and decoding techniques  
- Timing-based attacks and race conditions
- Privilege escalation and access control bypass
- Information disclosure and reconnaissance
- Parameter enumeration and hidden endpoints

## 🚩 Flags to Discover

The challenge contains 5 flags in the format `TCQ2025{...}`:
1. **Flag 1:** Security Break Challenge - `TCQ2025{S3Cur1ty_Br3@k_P@55ed}`
2. **Flag 2:** Flower Power Encoding - `TCQ2025{F!ow3r#92@tY8&Vk}`
3. **Flag 3:** Race Condition Timing - `TCQ2025{Y0u_kn0w_i5_th15_RaC3}`
4. **Flag 4:** Privilege Escalation - `TCQ2025{PwN_2_0wN_N0w_Y0u_ar3_5t3M}`
5. **Flag 5:** Zero Day Discovery - `TCQ2025{D4Y_0_T0_zeR0_d4Y}`

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup and Run
```bash
# Clone the repository
git clone https://github.com/Piyush-ai-Miet/Ctf-newwww.git
cd Ctf-newwww

# Install dependencies
pip install -r requirements.txt

# Run the CTF challenge
python app.py

# Or use the convenience script
./run_ctf.sh
```

The web application will be available at:
- Local: `http://localhost:5000`
- Network: `http://192.168.29.153:5000`

### Using Docker
```bash
# Build the container
docker build -t indian-cyber-quest-ctf .

# Run the container
docker run -p 5000:5000 indian-cyber-quest-ctf
```

## 📚 Documentation

- **[WALKTHROUGH.md](WALKTHROUGH.md)** - Complete step-by-step solution guide
- **[generate_traffic.py](generate_traffic.py)** - Script to generate network traffic for PCAP analysis

## 🛠️ Features

### Web Endpoints
- `/` - Main challenge page (Flag 1)
- `/page` - Secondary challenge page (Flag 2)
- `/login` - Authentication endpoint
- `/admin` - Administrative access (Flag 4)
- `/source` - Timing-sensitive endpoint (Flag 3)  
- `/zero-day` - Hidden parameter endpoint (Flag 5)
- `/robots.txt` - Discovery hints
- `/hint` - Challenge hints

### Security Learning Areas
1. **Web Application Security** - Common vulnerabilities and attack vectors
2. **Authentication Bypass** - Weak passwords and session manipulation
3. **Information Disclosure** - Source code analysis and hidden data
4. **Timing Attacks** - Race conditions and timing-based vulnerabilities
5. **Access Control** - Privilege escalation techniques
6. **Reconnaissance** - Discovery and enumeration methods

## 🔧 Network Traffic Analysis

Generate realistic CTF traffic for PCAP analysis:
```bash
# Generate traffic that solves all challenges
python generate_traffic.py

# Capture traffic with tcpdump (Linux/Mac)
tcpdump -i lo -w ctf_traffic.pcap port 5000

# Analyze with Wireshark
wireshark ctf_traffic.pcap
```

## 🎓 Educational Value

This CTF is designed to teach:
- **Reconnaissance**: Information gathering and discovery techniques
- **Web Exploitation**: Common web application vulnerabilities
- **Cryptography**: Basic encoding/decoding concepts
- **Network Analysis**: Traffic inspection and PCAP analysis
- **Access Control**: Authentication and authorization flaws
- **Timing Attacks**: Race conditions and temporal security issues

## 📋 Challenge Difficulty

- **Target Audience**: Beginner to Intermediate
- **Estimated Time**: 30-60 minutes
- **Required Skills**: Basic web security knowledge, command line tools
- **Optional Tools**: Burp Suite, OWASP ZAP, Wireshark

## 🏆 Scoring

Each flag is worth equal points:
- Flag 1 (Security Break): 20 points
- Flag 2 (Encoding): 20 points  
- Flag 3 (Timing): 20 points
- Flag 4 (Privilege Escalation): 20 points
- Flag 5 (Parameter Discovery): 20 points

**Total**: 100 points

## 🛡️ Security Notes

This application is designed for educational purposes and contains intentional vulnerabilities. **Do not deploy in production environments.**

## 👨‍💻 Author

**Piyush Dhariwal**  
Computer Science Engineering  
MIET (Meerut Institute of Engineering and Technology)  
Email: piyush.dhariwal.cse.2023@miet.ac.in

## 📄 License

This project is created for educational purposes as part of the Indian Cyber Quest 2025.

---

**Happy Hacking! 🚩**
