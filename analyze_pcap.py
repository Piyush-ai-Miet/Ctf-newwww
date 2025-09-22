#!/usr/bin/env python3
"""
CTF PCAP Analyzer - Indian Army Quest 2025
This script analyzes pcap files for HTTP traffic containing passwords.
"""

import subprocess
import sys
import re
import base64
import urllib.parse

def analyze_http_traffic(pcap_file):
    """
    Analyze HTTP traffic in pcap file to extract potential passwords
    """
    print(f"[*] Analyzing {pcap_file} for HTTP traffic...")
    
    # Extract HTTP requests
    try:
        # Use tshark to extract HTTP data
        cmd = [
            'tshark', '-r', pcap_file, 
            '-Y', 'http.request or http.response',
            '-T', 'fields',
            '-e', 'http.request.method',
            '-e', 'http.request.uri',
            '-e', 'http.request.full_uri', 
            '-e', 'http.host',
            '-e', 'http.user_agent',
            '-e', 'http.authorization',
            '-e', 'http.cookie',
            '-e', 'http.content_type',
            '-e', 'data.data',
            '-E', 'header=y'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"[!] Error running tshark: {result.stderr}")
            return
            
        lines = result.stdout.strip().split('\n')
        if len(lines) <= 1:
            print("[!] No HTTP traffic found in pcap file")
            return
            
        print(f"[+] Found {len(lines)-1} HTTP requests/responses")
        
        # Analyze each line for potential passwords
        passwords_found = []
        
        for i, line in enumerate(lines[1:], 1):  # Skip header
            fields = line.split('\t')
            
            print(f"\n[*] Analyzing HTTP entry {i}:")
            
            if len(fields) >= 9:
                method, uri, full_uri, host, user_agent, auth, cookie, content_type, data = fields[:9]
                
                # Check for basic auth
                if auth:
                    print(f"[+] Authorization header found: {auth}")
                    if auth.startswith('Basic '):
                        try:
                            decoded = base64.b64decode(auth[6:]).decode('utf-8')
                            print(f"[+] Basic Auth decoded: {decoded}")
                            passwords_found.append(f"Basic Auth: {decoded}")
                        except:
                            pass
                
                # Check URI for passwords
                if uri:
                    print(f"[+] URI: {uri}")
                    # Look for password parameters
                    password_patterns = [
                        r'password=([^&]+)',
                        r'pass=([^&]+)', 
                        r'pwd=([^&]+)',
                        r'passwd=([^&]+)',
                        r'secret=([^&]+)',
                        r'key=([^&]+)'
                    ]
                    
                    for pattern in password_patterns:
                        matches = re.findall(pattern, uri, re.IGNORECASE)
                        for match in matches:
                            decoded = urllib.parse.unquote(match)
                            print(f"[+] Password found in URI: {decoded}")
                            passwords_found.append(f"URI Parameter: {decoded}")
                
                # Check cookies for passwords
                if cookie:
                    print(f"[+] Cookie: {cookie}")
                    password_patterns = [
                        r'password=([^;]+)',
                        r'pass=([^;]+)',
                        r'secret=([^;]+)',
                        r'token=([^;]+)'
                    ]
                    
                    for pattern in password_patterns:
                        matches = re.findall(pattern, cookie, re.IGNORECASE)
                        for match in matches:
                            print(f"[+] Password found in cookie: {match}")
                            passwords_found.append(f"Cookie: {match}")
                
                # Check POST data
                if data and method == 'POST':
                    print(f"[+] POST data found (hex): {data}")
                    try:
                        # Convert hex to ascii
                        hex_data = data.replace(':', '')
                        ascii_data = bytes.fromhex(hex_data).decode('utf-8', errors='ignore')
                        print(f"[+] POST data (ASCII): {ascii_data}")
                        
                        # Look for password in form data
                        password_patterns = [
                            r'password=([^&]+)',
                            r'pass=([^&]+)',
                            r'pwd=([^&]+)',
                            r'secret=([^&]+)'
                        ]
                        
                        for pattern in password_patterns:
                            matches = re.findall(pattern, ascii_data, re.IGNORECASE)
                            for match in matches:
                                decoded = urllib.parse.unquote(match)
                                print(f"[+] Password found in POST data: {decoded}")
                                passwords_found.append(f"POST Data: {decoded}")
                    except:
                        pass
        
        # Summary
        print(f"\n{'='*60}")
        print("INDIAN ARMY QUEST 2025 - CTF PASSWORD ANALYSIS RESULTS")
        print(f"{'='*60}")
        
        if passwords_found:
            print(f"[+] Found {len(passwords_found)} potential passwords:")
            for i, pwd in enumerate(passwords_found, 1):
                print(f"    {i}. {pwd}")
        else:
            print("[!] No passwords found in HTTP traffic")
            
        print(f"{'='*60}")
        
    except Exception as e:
        print(f"[!] Error analyzing pcap: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 analyze_pcap.py <pcap_file>")
        print("\nThis script analyzes pcap files for HTTP traffic containing passwords")
        print("Suitable for CTF challenges like Indian Army Quest 2025")
        sys.exit(1)
    
    pcap_file = sys.argv[1]
    analyze_http_traffic(pcap_file)

if __name__ == "__main__":
    main()