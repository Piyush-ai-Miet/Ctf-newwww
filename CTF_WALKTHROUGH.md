# CTF Challenge Walkthrough

This document provides a detailed walkthrough for obtaining all 5 flags in this CTF challenge.

## Challenge Overview

- **Target HTTP Server**: http://192.168.29.153:5000/
- **Additional Endpoint**: http://192.168.29.153:5000/page
- **Challenge Type**: Network Analysis + Web Security
- **Tools Required**: Wireshark/tcpdump, Web Browser, Burp Suite/OWASP ZAP, Network scanner

## Flags to Capture

1. **Flag1**: `TCQ2025{S3Cur1ty_Br3@k_P@55ed}`
2. **Flag2**: `TCQ2025{F!ow3r#92@tY8&Vk}`
3. **Flag3**: `TCQ2025{Y0u_kn0w_i5_th15_RaC3}`
4. **Flag4**: `TCQ2025{PwN_2_0wN_N0w_Y0u_ar3_5t3M}`
5. **Flag5**: `TCQ2025{D4Y_0_T0_zeR0_d4Y}`

---

## Flag 1: Security Break Passed
**Flag**: `TCQ2025{S3Cur1ty_Br3@k_P@55ed}`

### Method: Basic Authentication Bypass

1. **Initial Reconnaissance**
   ```bash
   # Scan the target server
   nmap -sC -sV 192.168.29.153
   
   # Check for common vulnerabilities
   nikto -h http://192.168.29.153:5000/
   ```

2. **Access the main page**
   - Navigate to `http://192.168.29.153:5000/`
   - Look for any login forms or authentication mechanisms
   - Check page source for hidden comments or credentials

3. **Common Authentication Bypass Techniques**
   - Try SQL injection: `' OR '1'='1' --`
   - Default credentials: admin/admin, admin/password, root/root
   - Check for authentication bypass via parameter manipulation
   - Look for session cookies that can be modified

4. **Flag Location**
   - Flag likely appears after successful authentication bypass
   - Check response headers, page source, or console output
   - May be hidden in JavaScript variables or HTML comments

---

## Flag 2: Flower Hash
**Flag**: `TCQ2025{F!ow3r#92@tY8&Vk}`

### Method: Directory Traversal and Hidden Content

1. **Directory Enumeration**
   ```bash
   # Use dirb or gobuster to find hidden directories
   dirb http://192.168.29.153:5000/
   gobuster dir -u http://192.168.29.153:5000/ -w /usr/share/wordlists/dirb/common.txt
   ```

2. **Common directories to check**
   - `/admin`
   - `/backup`
   - `/hidden`
   - `/files`
   - `/uploads`
   - `/api`

3. **Look for flower-related content**
   - Search for images, CSS, or JavaScript files related to flowers
   - Check `/static/`, `/assets/`, `/images/` directories
   - Look for base64 encoded data or hidden text in image metadata

4. **Flag Discovery**
   - Flag might be embedded in:
     - Image EXIF data
     - CSS comments
     - JavaScript variables
     - Hidden form fields

---

## Flag 3: Race Condition
**Flag**: `TCQ2025{Y0u_kn0w_i5_th15_RaC3}`

### Method: Race Condition Exploitation

1. **Identify Race Condition Vulnerability**
   - Look for forms that process requests sequentially
   - Check for file upload functionality
   - Look for voting/rating systems
   - Check for account registration or password reset

2. **Tools for Race Condition Testing**
   ```bash
   # Use Burp Suite Intruder with single payload
   # Set attack type to "Sniper" or "Cluster bomb"
   # Send multiple simultaneous requests
   ```

3. **Common Race Condition Scenarios**
   - Multiple simultaneous login attempts
   - Concurrent file uploads
   - Simultaneous form submissions
   - Parallel API requests

4. **Exploitation Steps**
   - Intercept a vulnerable request
   - Send multiple identical requests simultaneously
   - Look for different responses or error messages
   - Flag may appear in one of the race condition responses

---

## Flag 4: Privilege Escalation
**Flag**: `TCQ2025{PwN_2_0wN_N0w_Y0u_ar3_5t3M}`

### Method: Privilege Escalation Attack

1. **Initial Access**
   - Use credentials or vulnerabilities found in previous flags
   - Look for user-level access to the application

2. **Privilege Escalation Techniques**
   ```bash
   # Check for SUID binaries
   find / -perm -u=s -type f 2>/dev/null
   
   # Check sudo permissions
   sudo -l
   
   # Look for world-writable files
   find / -writable -type f 2>/dev/null
   ```

3. **Web Application Privilege Escalation**
   - Parameter manipulation (change user_id, role, etc.)
   - Cookie manipulation
   - JWT token modification
   - Session hijacking
   - Admin panel access

4. **Look for Admin Functionality**
   - Try accessing `/admin`, `/management`, `/control`
   - Check for admin-only API endpoints
   - Look for user role modification capabilities

---

## Flag 5: Zero Day Exploit
**Flag**: `TCQ2025{D4Y_0_T0_zeR0_d4Y}`

### Method: Zero-Day Vulnerability Exploitation

1. **Advanced Vulnerability Assessment**
   ```bash
   # Use automated scanners
   python3 sqlmap.py -u "http://192.168.29.153:5000/" --batch
   
   # Check for XXE vulnerabilities
   # Test for SSRF
   # Look for deserialization vulnerabilities
   ```

2. **Custom Exploit Development**
   - Analyze application behavior thoroughly
   - Look for unusual input validation
   - Test for buffer overflows
   - Check for memory corruption vulnerabilities

3. **Zero-Day Indicators**
   - Unusual server responses
   - Memory leaks or crashes
   - Unexpected behavior in edge cases
   - Custom application logic flaws

4. **Advanced Techniques**
   - Reverse engineering of application binaries
   - Memory dump analysis
   - Custom payload development
   - Exploit chaining

---

## Network Analysis with PCAP Files

Since this challenge mentions PCAP files, network traffic analysis is crucial:

### Tools Required
```bash
# Install Wireshark
sudo apt-get install wireshark

# Install tcpdump
sudo apt-get install tcpdump

# Install tshark for command-line analysis
sudo apt-get install tshark
```

### PCAP Analysis Steps

1. **Capture Network Traffic**
   ```bash
   # Capture traffic while interacting with the server
   sudo tcpdump -i any -w ctf_traffic.pcap host 192.168.29.153
   ```

2. **Analyze with Wireshark**
   - Open the PCAP file in Wireshark
   - Filter by HTTP traffic: `http`
   - Look for POST requests with credentials
   - Check for hidden parameters in HTTP headers

3. **Extract Credentials and Flags**
   ```bash
   # Extract HTTP traffic
   tshark -r ctf_traffic.pcap -Y http -T fields -e http.request.uri -e http.request.method

   # Look for strings that match flag pattern
   strings ctf_traffic.pcap | grep "TCQ2025"
   ```

4. **Common PCAP Flag Locations**
   - HTTP POST data
   - DNS queries
   - TCP stream conversations
   - Hidden in packet timing
   - Steganography in packet sizes

---

## HTTP Endpoint Analysis

### Main Endpoint: http://192.168.29.153:5000/

1. **Initial Analysis**
   ```bash
   # Check HTTP methods
   curl -X OPTIONS http://192.168.29.153:5000/
   
   # Check for sensitive headers
   curl -I http://192.168.29.153:5000/
   
   # Test for HTTP verb tampering
   curl -X PUT http://192.168.29.153:5000/
   curl -X DELETE http://192.168.29.153:5000/
   ```

2. **Parameter Testing**
   ```bash
   # Test for hidden parameters
   curl -d "debug=1" http://192.168.29.153:5000/
   curl -d "admin=true" http://192.168.29.153:5000/
   curl -d "flag=show" http://192.168.29.153:5000/
   ```

### Page Endpoint: http://192.168.29.153:5000/page

1. **Page-Specific Analysis**
   ```bash
   # Check for different responses
   curl http://192.168.29.153:5000/page
   
   # Test with different User-Agents
   curl -H "User-Agent: Mozilla/5.0" http://192.168.29.153:5000/page
   curl -H "User-Agent: Googlebot" http://192.168.29.153:5000/page
   ```

2. **Parameter Injection Testing**
   ```bash
   # Test for LFI/RFI
   curl "http://192.168.29.153:5000/page?file=../../../etc/passwd"
   curl "http://192.168.29.153:5000/page?include=flag.txt"
   
   # Test for SQL injection
   curl "http://192.168.29.153:5000/page?id=1' OR '1'='1"
   ```

---

## Security Tools and Commands

### Essential Commands
```bash
# Network scanning
nmap -sS -O -A 192.168.29.153

# Web vulnerability scanning
nikto -h http://192.168.29.153:5000/

# Directory brute forcing
gobuster dir -u http://192.168.29.153:5000/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

# SQL injection testing
sqlmap -u "http://192.168.29.153:5000/" --batch --dbs

# SSL/TLS testing
sslscan 192.168.29.153:5000
```

### Browser Developer Tools
1. **Inspect Network Traffic**
   - Open Developer Tools (F12)
   - Go to Network tab
   - Look for hidden API calls
   - Check response headers for flags

2. **Console Commands**
   ```javascript
   // Check for hidden variables
   console.log(window);
   
   // Look for flag variables
   for(var key in window) {
       if(key.includes('flag') || key.includes('TCQ')) {
           console.log(key, window[key]);
       }
   }
   ```

---

## Common CTF Techniques Summary

1. **Always check page source** - Flags often hidden in HTML comments
2. **Inspect all HTTP headers** - Custom headers may contain flags
3. **Test all input fields** - SQL injection, XSS, command injection
4. **Check robots.txt** - May reveal hidden paths
5. **Analyze cookies** - Base64 decode, modify values
6. **Test file uploads** - Upload malicious files
7. **Check for backup files** - .bak, .old, .backup extensions
8. **Use Burp Suite** - Intercept and modify requests
9. **Check JavaScript files** - May contain hardcoded credentials
10. **Network analysis** - Monitor all traffic with Wireshark

---

## Flag Submission

Once you've obtained all flags, ensure they follow the format:
- `TCQ2025{...}`
- Exact case sensitivity
- Include all special characters
- No extra spaces

Remember: Each flag represents a different attack vector and security concept. Understanding the methodology is more important than just finding the flags.