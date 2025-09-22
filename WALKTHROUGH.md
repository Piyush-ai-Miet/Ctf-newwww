# CTF 2025 - Complete Walkthrough

## Overview
This CTF contains 5 flags hidden throughout a Flask web application. Each flag uses different techniques commonly found in Capture The Flag competitions and real-world penetration testing.

**Base URL:** `http://192.168.29.153:5000/`
**Target Flags:**
- Flag1: `TCQ2025{S3Cur1ty_Br3@k_P@55ed}`
- Flag2: `TCQ2025{F!ow3r#92@tY8&Vk}`
- Flag3: `TCQ2025{Y0u_kn0w_i5_th15_RaC3}`
- Flag4: `TCQ2025{PwN_2_0wN_N0w_Y0u_ar3_5t3M}`
- Flag5: `TCQ2025{D4Y_0_T0_zeR0_d4Y}`

---

## Setup Instructions

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application:**
   ```bash
   python3 app.py
   ```

3. **Access the Application:**
   - Open browser to `http://localhost:5000` or `http://192.168.29.153:5000`

---

## Flag 1: Security Breach (Authentication Bypass)
**Flag:** `TCQ2025{S3Cur1ty_Br3@k_P@55ed}`

### Method: Weak Default Credentials
**Target:** `/login` endpoint

#### Steps:
1. Navigate to `http://192.168.29.153:5000/login`
2. Try common default credentials:
   - Username: `admin`
   - Password: `password123`
3. Alternatively, check HTML source code for hints in comments
4. Submit the login form
5. Flag will be displayed on the dashboard after successful authentication

#### Tools:
- Web browser
- View source functionality
- Basic credential testing

#### Learning Outcome:
- Default credentials are a major security vulnerability
- Always change default passwords in production systems
- HTML comments can leak sensitive information

---

## Flag 2: Hidden API Data (Header Analysis)
**Flag:** `TCQ2025{F!ow3r#92@tY8&Vk}`

### Method: HTTP Response Header Analysis
**Target:** `/api/flower` endpoint

#### Steps:
1. Navigate to `http://192.168.29.153:5000/api/flower`
2. Use browser developer tools or curl to examine response headers
3. Look for custom headers starting with `X-`
4. Find the `X-Flower-Token` header
5. The header contains base64 encoded flag data
6. Decode the base64 string to reveal the flag

#### Command Examples:
```bash
# Using curl to see headers
curl -I http://192.168.29.153:5000/api/flower

# Using curl to get full response with headers
curl -v http://192.168.29.153:5000/api/flower

# Decode the base64 header value
echo "VENRMjAyNXtGIW93M3IjOTJAdFk4JlZrfQ==" | base64 -d
```

#### Tools:
- curl
- Browser Developer Tools (Network tab)
- Base64 decoder
- Burp Suite or similar proxy tools

#### Learning Outcome:
- Always examine HTTP headers for hidden data
- APIs may leak information in unexpected places
- Base64 encoding is not encryption or security

---

## Flag 3: Race Condition (Timing Attack)
**Flag:** `TCQ2025{Y0u_kn0w_i5_th15_RaC3}`

### Method: Rapid Sequential Requests
**Target:** `/race` endpoint

#### Steps:
1. Send multiple rapid requests to `http://192.168.29.153:5000/race`
2. The flag appears only when the request counter is between 3-5
3. Use a script or tool to send requests quickly in succession
4. Monitor the response for the flag in the JSON output

#### Script Example:
```bash
# Bash script to hit the endpoint rapidly
for i in {1..10}; do
    curl -s http://192.168.29.153:5000/race | jq .
    sleep 0.1
done
```

#### Python Script:
```python
import requests
import time

url = "http://192.168.29.153:5000/race"
for i in range(10):
    response = requests.get(url)
    print(f"Request {i+1}: {response.json()}")
    time.sleep(0.1)
```

#### Tools:
- curl with bash loops
- Python requests library
- Burp Suite Intruder
- Custom automation scripts

#### Learning Outcome:
- Race conditions exist in poorly designed applications
- Timing-based vulnerabilities require automation
- Concurrent request handling can expose sensitive data

---

## Flag 4: Command Injection Simulation
**Flag:** `TCQ2025{PwN_2_0wN_N0w_Y0u_ar3_5t3M}`

### Method: Parameter Manipulation
**Target:** `/system` endpoint with `cmd` parameter

#### Steps:
1. Navigate to `http://192.168.29.153:5000/system`
2. Test different command parameters:
   - `http://192.168.29.153:5000/system?cmd=ls`
   - `http://192.168.29.153:5000/system?cmd=whoami`
3. Try accessing system files:
   - `http://192.168.29.153:5000/system?cmd=cat /etc/flag.txt`
4. The flag will be displayed in the response

#### Command Examples:
```bash
# Test different commands
curl "http://192.168.29.153:5000/system?cmd=ls"
curl "http://192.168.29.153:5000/system?cmd=whoami"
curl "http://192.168.29.153:5000/system?cmd=cat%20/etc/flag.txt"
```

#### Tools:
- Web browser with URL manipulation
- curl
- URL encoding tools
- Burp Suite parameter testing

#### Learning Outcome:
- Parameter injection vulnerabilities are common
- Always validate and sanitize user input
- System command execution should be heavily restricted

---

## Flag 5: User-Agent Spoofing (Scanner Detection)
**Flag:** `TCQ2025{D4Y_0_T0_zeR0_d4Y}`

### Method: Custom User-Agent Header
**Target:** `/vulnerability` endpoint

#### Steps:
1. Make a request to `http://192.168.29.153:5000/vulnerability` with default User-Agent
2. Observe the response indicates "unknown scanner"
3. Set a custom User-Agent header to `CTF-Scanner-2025`
4. Resend the request with the custom header
5. The flag will be returned in the JSON response

#### Command Examples:
```bash
# Default request (no flag)
curl http://192.168.29.153:5000/vulnerability

# Request with custom User-Agent (flag revealed)
curl -H "User-Agent: CTF-Scanner-2025" http://192.168.29.153:5000/vulnerability
```

#### Tools:
- curl with custom headers
- Browser developer tools (modify headers)
- Burp Suite header modification
- Python requests with custom headers

#### Python Example:
```python
import requests

url = "http://192.168.29.153:5000/vulnerability"
headers = {"User-Agent": "CTF-Scanner-2025"}
response = requests.get(url, headers=headers)
print(response.json())
```

#### Learning Outcome:
- Applications may behave differently based on User-Agent
- Header manipulation is a common penetration testing technique
- Never trust client-side headers for security decisions

---

## Additional Reconnaissance

### robots.txt Analysis
Visit `http://192.168.29.153:5000/robots.txt` for hints about:
- Disallowed directories
- Hidden endpoints
- Challenge-specific clues

### Source Code Analysis
- View page source for hidden comments
- Check JavaScript console messages
- Look for hidden form fields or divs

### Directory/Endpoint Discovery
Common endpoints to test:
- `/admin`
- `/api/*`
- `/login`
- `/dashboard`
- `/source`
- `/debug`

---

## Summary

This CTF demonstrates common web application vulnerabilities:

1. **Authentication Issues** - Weak default credentials
2. **Information Disclosure** - Sensitive data in HTTP headers
3. **Timing Vulnerabilities** - Race conditions and timing attacks
4. **Injection Flaws** - Command injection through parameters
5. **Header Manipulation** - User-Agent based access control bypass

### Tools Used:
- Web browser with developer tools
- curl command-line tool
- Python requests library
- Base64 decoder
- Text editor for scripting

### Skills Demonstrated:
- HTTP protocol analysis
- Parameter manipulation
- Header modification
- Timing attack execution
- Source code review
- Automation scripting

---

## Security Recommendations

1. **Authentication:**
   - Enforce strong password policies
   - Implement multi-factor authentication
   - Never use default credentials in production

2. **Information Disclosure:**
   - Review all HTTP headers for sensitive data
   - Implement proper error handling
   - Use security headers appropriately

3. **Race Conditions:**
   - Implement proper locking mechanisms
   - Use atomic operations where necessary
   - Test for concurrency issues

4. **Input Validation:**
   - Sanitize all user input
   - Use parameterized queries
   - Implement input validation frameworks

5. **Header Security:**
   - Don't rely on client-side headers for security
   - Implement proper authentication mechanisms
   - Use server-side validation only