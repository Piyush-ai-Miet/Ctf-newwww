#!/bin/bash

# CTF PCAP Quick Analysis Script for Indian Army Quest 2025
# Usage: ./quick_analysis.sh <pcap_file>

if [ $# -ne 1 ]; then
    echo "Usage: $0 <pcap_file>"
    echo "Quick analysis script for CTF password extraction from HTTP traffic"
    exit 1
fi

PCAP_FILE="$1"

if [ ! -f "$PCAP_FILE" ]; then
    echo "Error: File $PCAP_FILE not found!"
    exit 1
fi

echo "================================================"
echo "Indian Army Quest 2025 - CTF PCAP Quick Analysis"
echo "================================================"
echo "Analyzing: $PCAP_FILE"
echo

# Check if tshark is available
if ! command -v tshark &> /dev/null; then
    echo "Error: tshark not found. Please install with: sudo apt install tshark"
    exit 1
fi

echo "[1] HTTP Traffic Overview:"
echo "-------------------------"
tshark -r "$PCAP_FILE" -Y "http" -T fields -e frame.number -e ip.src -e ip.dst -e http.request.method -e http.host -e http.request.uri | head -20

echo
echo "[2] Looking for Authentication Headers:"
echo "--------------------------------------"
tshark -r "$PCAP_FILE" -Y "http.authorization" -T fields -e http.authorization

echo
echo "[3] Searching for Password Parameters in URLs:"
echo "----------------------------------------------"
tshark -r "$PCAP_FILE" -Y "http.request.uri contains \"password\" or http.request.uri contains \"pass\" or http.request.uri contains \"pwd\"" -T fields -e http.request.uri

echo
echo "[4] POST Requests (likely containing form data):"
echo "------------------------------------------------"
tshark -r "$PCAP_FILE" -Y "http.request.method == POST" -T fields -e http.host -e http.request.uri -e data.data | head -10

echo
echo "[5] Looking for Login-related Traffic:"
echo "-------------------------------------"
tshark -r "$PCAP_FILE" -Y "http.request.uri contains \"login\" or http.request.uri contains \"auth\" or http.request.uri contains \"signin\"" -T fields -e http.request.method -e http.host -e http.request.uri

echo
echo "[6] Cookies that might contain passwords/tokens:"
echo "-----------------------------------------------"
tshark -r "$PCAP_FILE" -Y "http.cookie contains \"password\" or http.cookie contains \"token\" or http.cookie contains \"secret\"" -T fields -e http.cookie

echo
echo "[7] HTTP Responses with Authentication Info:"
echo "--------------------------------------------"
tshark -r "$PCAP_FILE" -Y "http.response and (data.data contains \"password\" or data.data contains \"token\")" -T fields -e http.response.code -e data.data | head -5

echo
echo "================================================"
echo "Analysis complete. Check the output above for:"
echo "- Basic Auth headers (decode with: echo 'string' | base64 -d)"
echo "- Password parameters in URLs"
echo "- Form data in POST requests"
echo "- Authentication cookies"
echo "================================================"

# If basic auth found, try to decode it
AUTH_HEADER=$(tshark -r "$PCAP_FILE" -Y "http.authorization" -T fields -e http.authorization | head -1)
if [[ "$AUTH_HEADER" == Basic* ]]; then
    echo
    echo "[BONUS] Decoding Basic Auth:"
    echo "---------------------------"
    AUTH_STRING=${AUTH_HEADER#"Basic "}
    echo "Encoded: $AUTH_STRING"
    echo "Decoded: $(echo "$AUTH_STRING" | base64 -d 2>/dev/null || echo "Failed to decode")"
fi

echo
echo "For detailed analysis, use: python3 analyze_pcap.py $PCAP_FILE"