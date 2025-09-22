#!/usr/bin/env python3
"""
Verification script to check if all flags are present in the PCAP challenge.
"""

import subprocess
import re
import base64

def verify_challenge(pcap_file="challenge.pcap"):
    """Verify that all expected flags are present in the PCAP file"""
    
    print("🔍 Verifying CTF PCAP Challenge...")
    print("=" * 50)
    
    expected_flags = [
        "flag{basic_auth_secret}",
        "flag{ftp_password_hidden}", 
        "flag{telnet_admin_pass}"
    ]
    
    found_flags = []
    
    try:
        # Extract readable content from PCAP
        result = subprocess.run([
            'tcpdump', '-r', pcap_file, '-A'
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode != 0:
            print(f"❌ Error reading PCAP file: {result.stderr}")
            return False
        
        content = result.stdout
        
        # Look for flag patterns
        flag_pattern = r'flag\{[^}]+\}'
        direct_flags = re.findall(flag_pattern, content)
        
        for flag in direct_flags:
            if flag not in found_flags:
                found_flags.append(flag)
                print(f"✅ Found flag: {flag}")
        
        # Look for Base64 encoded flags
        base64_pattern = r'Basic\s+([A-Za-z0-9+/=]+)'
        base64_matches = re.findall(base64_pattern, content, re.IGNORECASE)
        
        for encoded in base64_matches:
            try:
                decoded = base64.b64decode(encoded).decode('utf-8')
                flag_in_decoded = re.findall(flag_pattern, decoded)
                for flag in flag_in_decoded:
                    if flag not in found_flags:
                        found_flags.append(flag)
                        print(f"✅ Found Base64 encoded flag: {flag}")
            except:
                pass
        
        print(f"\n📊 Verification Results:")
        print(f"Expected flags: {len(expected_flags)}")
        print(f"Found flags: {len(found_flags)}")
        
        missing_flags = []
        for expected in expected_flags:
            if expected not in found_flags:
                missing_flags.append(expected)
        
        if missing_flags:
            print(f"❌ Missing flags: {missing_flags}")
            return False
        else:
            print("✅ All flags found successfully!")
            print("\n🎯 Challenge is ready for deployment!")
            return True
            
    except Exception as e:
        print(f"❌ Error during verification: {e}")
        return False

def check_file_integrity(pcap_file="challenge.pcap"):
    """Check if PCAP file is valid and has content"""
    import os
    
    if not os.path.exists(pcap_file):
        print(f"❌ PCAP file {pcap_file} not found!")
        return False
    
    size = os.path.getsize(pcap_file)
    if size == 0:
        print(f"❌ PCAP file {pcap_file} is empty!")
        return False
    
    print(f"✅ PCAP file found: {pcap_file} ({size} bytes)")
    
    # Check if it's a valid PCAP file
    try:
        result = subprocess.run([
            'file', pcap_file
        ], capture_output=True, text=True)
        
        if 'pcap' in result.stdout.lower():
            print(f"✅ Valid PCAP file format")
            return True
        else:
            print(f"❌ Invalid PCAP file format")
            return False
    except:
        print(f"⚠️  Could not verify file format")
        return True  # Assume it's valid if we can't check

if __name__ == "__main__":
    print("🕵️  CTF PCAP Challenge Verification Tool")
    print("=" * 60)
    
    # Check file integrity
    if not check_file_integrity():
        exit(1)
    
    print()
    
    # Verify challenge content
    if verify_challenge():
        print("\n🎉 Challenge verification completed successfully!")
        print("The CTF challenge is ready for participants.")
    else:
        print("\n❌ Challenge verification failed!")
        print("Please check the PCAP file and regenerate if necessary.")
        exit(1)