#!/usr/bin/env python3
"""
Script to generate sample network traffic for CTF PCAP analysis
This simulates a user solving all the CTF challenges
"""

import requests
import time
import base64
import random

def solve_ctf_challenges(base_url="http://localhost:5000"):
    """
    Automate solving all CTF challenges to generate network traffic
    """
    print("🚀 Starting CTF challenge simulation...")
    
    session = requests.Session()
    
    # 1. Visit home page (Flag 1 discovery)
    print("📍 Step 1: Visiting home page...")
    response = session.get(f"{base_url}/")
    print(f"Status: {response.status_code}")
    
    # 2. Try wrong password first (realistic behavior)
    print("📍 Step 2: Attempting login with wrong password...")
    response = session.post(f"{base_url}/login", data={"password": "password123"})
    print(f"Login attempt 1: {response.status_code}")
    
    # 3. Try correct password (Flag 1)
    print("📍 Step 3: Attempting login with correct password...")
    response = session.post(f"{base_url}/login", data={"password": "admin123"})
    if response.status_code == 200:
        flag1_data = response.json()
        print(f"🚩 Flag 1 Found: {flag1_data.get('flag', 'Not found')}")
    
    # 4. Visit page endpoint (Flag 2)
    print("📍 Step 4: Visiting special page...")
    response = session.get(f"{base_url}/page")
    print(f"Status: {response.status_code}")
    
    # Extract and decode Flag 2
    if "VENRMjAyNXtGIW93M3IjOTJAdFk4JlZrfQ==" in response.text:
        encoded_flag = "VENRMjAyNXtGIW93M3IjOTJAdFk4JlZrfQ=="
        flag2 = base64.b64decode(encoded_flag).decode()
        print(f"🚩 Flag 2 Found: {flag2}")
    
    # 5. Check robots.txt
    print("📍 Step 5: Checking robots.txt...")
    response = session.get(f"{base_url}/robots.txt")
    print(f"Status: {response.status_code}")
    
    # 6. Try to access admin without authentication
    print("📍 Step 6: Attempting admin access without auth...")
    response = session.get(f"{base_url}/admin")
    print(f"Admin access (no auth): {response.status_code}")
    
    # 7. Access admin with special header (Flag 4)
    print("📍 Step 7: Accessing admin with special header...")
    headers = {"X-Admin-Access": "pwn2own"}
    response = session.get(f"{base_url}/admin", headers=headers)
    if response.status_code == 200:
        flag4_data = response.json()
        print(f"🚩 Flag 4 Found: {flag4_data.get('flag', 'Not found')}")
    
    # 8. Try zero-day endpoint without parameter
    print("📍 Step 8: Trying zero-day endpoint...")
    response = session.get(f"{base_url}/zero-day")
    print(f"Zero-day (no param): {response.status_code}")
    
    # 9. Access zero-day with correct parameter (Flag 5)
    print("📍 Step 9: Accessing zero-day with day=0...")
    response = session.get(f"{base_url}/zero-day?day=0")
    if response.status_code == 200:
        flag5_data = response.json()
        print(f"🚩 Flag 5 Found: {flag5_data.get('flag', 'Not found')}")
    
    # 10. Multiple attempts at timing-based endpoint (Flag 3)
    print("📍 Step 10: Attempting timing-based challenge...")
    for attempt in range(15):
        response = session.get(f"{base_url}/source")
        if response.status_code == 200:
            data = response.json()
            if "flag" in data:
                print(f"🚩 Flag 3 Found: {data['flag']}")
                break
        time.sleep(1)
    
    # 11. Check hints
    print("📍 Step 11: Checking hints...")
    response = session.get(f"{base_url}/hint")
    print(f"Hints status: {response.status_code}")
    
    print("✅ CTF simulation completed!")

if __name__ == "__main__":
    # Add some random delays to make traffic more realistic
    solve_ctf_challenges()