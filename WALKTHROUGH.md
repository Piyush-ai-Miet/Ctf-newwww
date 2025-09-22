# CTF Challenge Walkthrough - Indian Cyber Quest 2025

## Overview
This CTF challenge contains 5 flags that need to be discovered through various cybersecurity techniques. The web application runs on port 5000 and presents multiple attack vectors.

**Target:** http://192.168.29.153:5000/

## Flags to Find:
1. `TCQ2025{S3Cur1ty_Br3@k_P@55ed}`
2. `TCQ2025{F!ow3r#92@tY8&Vk}`
3. `TCQ2025{Y0u_kn0w_i5_th15_RaC3}`
4. `TCQ2025{PwN_2_0wN_N0w_Y0u_ar3_5t3M}`
5. `TCQ2025{D4Y_0_T0_zeR0_d4Y}`

---

## Flag 1: Security Break Challenge
**Technique:** Weak Password Attack / Source Code Analysis

### Steps:
1. Visit the main page: `http://192.168.29.153:5000/`
2. Inspect the page source (Right-click → View Source)
3. Look for HTML comments - you'll find a hint about weak passwords
4. Try common passwords like `admin123` in the login form
5. Successful login will reveal **Flag 1: `TCQ2025{S3Cur1ty_Br3@k_P@55ed}`**

### Technical Details:
- The password `admin123` is hardcoded in the application
- The flag is returned via JSON response when login is successful

---

## Flag 2: Base64 Decoding Challenge
**Technique:** Encoded Data Analysis

### Steps:
1. Navigate to: `http://192.168.29.153:5000/page`
2. View the page source to find encoded data
3. You'll see a base64 encoded string: `VENRMjAyNXtGIW93M3IjOTJAdFk4JlZrfQ==`
4. Decode the base64 string:
   ```bash
   echo "VENRMjAyNXtGIW93M3IjOTJAdFk4JlZrfQ==" | base64 -d
   ```
5. Result: **Flag 2: `TCQ2025{F!ow3r#92@tY8&Vk}`**

### Technical Details:
- The flag is base64 encoded and embedded in the HTML template
- Base64 is a common encoding technique used in CTFs

---

## Flag 3: Race Condition / Timing Attack
**Technique:** Timing-based Attack

### Steps:
1. Discover the hidden endpoint by checking `http://192.168.29.153:5000/robots.txt`
2. Access: `http://192.168.29.153:5000/source`
3. The endpoint only returns the flag at specific times (when current timestamp % 10 == 0)
4. Keep trying the endpoint until you hit the right timing
5. Alternatively, script multiple requests:
   ```bash
   while true; do
     curl -s http://192.168.29.153:5000/source | grep -o "TCQ2025.*}"
     sleep 1
   done
   ```
6. Success will return: **Flag 3: `TCQ2025{Y0u_kn0w_i5_th15_RaC3}`**

### Technical Details:
- The endpoint uses `time.time() % 10 == 0` condition
- Demonstrates race condition vulnerabilities

---

## Flag 4: Privilege Escalation / Header Manipulation
**Technique:** HTTP Header Injection

### Steps:
1. Discover the admin endpoint from robots.txt: `/admin`
2. Try accessing `http://192.168.29.153:5000/admin` - it will deny access
3. Either:
   - Login first with admin123 (from Flag 1), OR
   - Use the special header: `X-Admin-Access: pwn2own`
4. Use curl with header:
   ```bash
   curl -H "X-Admin-Access: pwn2own" http://192.168.29.153:5000/admin
   ```
5. Success returns: **Flag 4: `TCQ2025{PwN_2_0wN_N0w_Y0u_ar3_5t3M}`**

### Technical Details:
- Demonstrates privilege escalation through session or header manipulation
- Shows how improper authentication can be bypassed

---

## Flag 5: Parameter Discovery / Zero-Day Reference
**Technique:** Parameter Enumeration

### Steps:
1. Discover the hidden endpoint from robots.txt: `/zero-day`
2. Access `http://192.168.29.153:5000/zero-day` - it will give a hint
3. The hint asks "What comes before day 1?"
4. Try the parameter `day=0`:
   ```bash
   curl "http://192.168.29.153:5000/zero-day?day=0"
   ```
5. Success returns: **Flag 5: `TCQ2025{D4Y_0_T0_zeR0_d4Y}`**

### Technical Details:
- Demonstrates parameter enumeration techniques
- References "Day 0" (zero-day) vulnerabilities

---

## Discovery Methods

### robots.txt Analysis
Visit `http://192.168.29.153:5000/robots.txt` to discover hidden endpoints:
- `/admin`
- `/source` 
- `/zero-day`

### Hints Endpoint
Visit `http://192.168.29.153:5000/hint` for additional guidance on each flag.

### Source Code Analysis
Always inspect HTML source code for:
- Hidden comments
- Encoded data
- JavaScript functions
- Hidden form fields

---

## Tools Required

### Basic Tools:
- Web browser (with Developer Tools)
- curl command-line tool
- base64 decoder

### Advanced Tools (Optional):
- Burp Suite for traffic analysis
- OWASP ZAP for automated scanning
- Python/bash scripts for automation

---

## Learning Objectives

This CTF teaches:
1. **Web Application Security**: Common vulnerabilities in web apps
2. **Weak Authentication**: How poor password policies lead to breaches
3. **Data Encoding**: Understanding and decoding common formats
4. **Timing Attacks**: Race conditions and timing-based vulnerabilities
5. **Privilege Escalation**: Bypassing access controls
6. **Information Disclosure**: Finding hidden endpoints and parameters
7. **Reconnaissance**: Using robots.txt and source code analysis

---

## Network Traffic Analysis (PCAP)

For additional practice, you can:
1. Use Wireshark to capture traffic while solving the CTF
2. Analyze HTTP requests and responses
3. Look for patterns in network communication
4. Practice identifying flags in network traffic

To generate a PCAP file:
```bash
# Start packet capture
tcpdump -i lo -w ctf_traffic.pcap port 5000 &

# Solve the CTF challenges
# Stop capture with Ctrl+C

# Analyze with Wireshark
wireshark ctf_traffic.pcap
```

---

## Security Lessons

1. **Always use strong passwords** and avoid hardcoding them
2. **Validate and sanitize all inputs** including headers and parameters
3. **Implement proper session management** and access controls
4. **Be careful with timing-sensitive operations** to avoid race conditions
5. **Don't expose sensitive information** in source code or error messages
6. **Use proper encoding and encryption** for sensitive data
7. **Implement security headers** and proper authentication mechanisms

---

**Designed by:** Piyush Dhariwal  
**Event:** Indian Cyber Quest 2025  
**Difficulty:** Beginner to Intermediate