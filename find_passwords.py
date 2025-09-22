#!/usr/bin/env python3
"""
Password finder for PCAP files - CTF Challenge Tool
This script analyzes PCAP files to find embedded passwords and credentials.
"""

import subprocess
import re
import base64
import sys
import os

def analyze_pcap_with_tcpdump(pcap_file):
    """Use tcpdump to analyze PCAP file and extract readable content"""
    print(f"Analyzing PCAP file: {pcap_file}")
    print("=" * 50)
    
    if not os.path.exists(pcap_file):
        print(f"Error: PCAP file {pcap_file} not found!")
        return
    
    # Extract readable ASCII content from packets
    try:
        result = subprocess.run([
            'tcpdump', '-r', pcap_file, '-A'
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            content = result.stdout
            print("Raw packet content:")
            print("-" * 30)
            print(content)
            print("-" * 30)
            
            # Look for passwords in the content
            find_passwords_in_text(content)
            
        else:
            print(f"Error running tcpdump: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        print("Tcpdump analysis timed out")
    except Exception as e:
        print(f"Error analyzing PCAP: {e}")

def find_passwords_in_text(text):
    """Search for common password patterns in text"""
    print("\n🔍 Searching for passwords and credentials...")
    print("=" * 50)
    
    patterns = [
        (r'password[:\s=]+([^\s\r\n]+)', 'Password field'),
        (r'pass[:\s=]+([^\s\r\n]+)', 'Pass field'),
        (r'pwd[:\s=]+([^\s\r\n]+)', 'PWD field'),
        (r'Authorization:\s*Basic\s+([A-Za-z0-9+/=]+)', 'HTTP Basic Auth'),
        (r'USER\s+([^\r\n]+)', 'FTP/Username'),
        (r'PASS\s+([^\r\n]+)', 'FTP/Password'),
        (r'login[:\s=]+([^\s\r\n]+)', 'Login field'),
        (r'username[:\s=]+([^\s\r\n&]+)', 'Username field'),
        (r'flag\{[^}]+\}', 'CTF Flag'),
    ]
    
    findings = []
    
    for pattern, description in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            findings.append((description, match))
            print(f"[{description}] Found: {match}")
    
    # Try to decode Base64 encoded credentials
    print("\n🔓 Attempting to decode Base64 credentials...")
    print("-" * 40)
    
    base64_pattern = r'Basic\s+([A-Za-z0-9+/=]+)'
    base64_matches = re.findall(base64_pattern, text, re.IGNORECASE)
    
    for encoded in base64_matches:
        try:
            decoded = base64.b64decode(encoded).decode('utf-8')
            print(f"Base64 decoded: {encoded} -> {decoded}")
            
            # Check if decoded string contains credentials
            if ':' in decoded:
                username, password = decoded.split(':', 1)
                print(f"  Username: {username}")
                print(f"  Password: {password}")
                findings.append(("Decoded HTTP Basic Auth", decoded))
                
        except Exception as e:
            print(f"Could not decode Base64: {encoded} ({e})")
    
    # Look for URL-encoded data
    print("\n🌐 Checking for URL-encoded data...")
    print("-" * 30)
    
    url_pattern = r'[a-zA-Z_]+=[^&\s]+'
    url_matches = re.findall(url_pattern, text)
    
    for match in url_matches:
        if any(keyword in match.lower() for keyword in ['password', 'pass', 'pwd', 'user', 'login']):
            print(f"Form data: {match}")
            findings.append(("Form data", match))
    
    print(f"\n📊 Summary: Found {len(findings)} potential credentials/passwords")
    
    return findings

def extract_strings_from_pcap(pcap_file):
    """Extract all printable strings from PCAP file"""
    print("\n📝 Extracting all readable strings...")
    print("-" * 40)
    
    try:
        # Use tcpdump to get hex output and convert to strings
        result = subprocess.run([
            'tcpdump', '-r', pcap_file, '-xx'
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            # Extract printable strings from hex data
            hex_data = result.stdout
            
            # Look for strings that might contain passwords
            string_pattern = r'[a-zA-Z0-9@._\-:{}]{4,}'
            strings = re.findall(string_pattern, hex_data)
            
            relevant_strings = []
            for s in strings:
                if any(keyword in s.lower() for keyword in ['password', 'pass', 'user', 'flag', 'auth', 'login', 'admin']):
                    relevant_strings.append(s)
                    print(f"Interesting string: {s}")
            
            return relevant_strings
            
    except Exception as e:
        print(f"Error extracting strings: {e}")
    
    return []

def main():
    """Main function to analyze PCAP file"""
    pcap_file = "challenge.pcap"
    
    if len(sys.argv) > 1:
        pcap_file = sys.argv[1]
    
    print("🕵️  PCAP Password Finder - CTF Challenge Tool")
    print("=" * 60)
    
    # Analyze with tcpdump
    analyze_pcap_with_tcpdump(pcap_file)
    
    # Extract strings
    extract_strings_from_pcap(pcap_file)
    
    print("\n✅ Analysis complete!")
    print("\nHint: Look for:")
    print("- HTTP Basic Authentication (Base64 encoded)")
    print("- FTP USER/PASS commands")
    print("- Form data with username/password fields")
    print("- Any strings containing 'flag{...}'")

if __name__ == "__main__":
    main()