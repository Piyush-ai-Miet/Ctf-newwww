#!/usr/bin/env python3
"""
Create a sample HTTP pcap file for CTF demonstration
This creates synthetic HTTP traffic containing various password scenarios
"""

import subprocess
import sys
import time
import socket
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class TestHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if 'password=' in self.path:
            # Simulate login with password in URL
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Login successful!")
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Welcome to Indian Army Quest 2025 CTF")
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        # Simulate login form processing
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Form data received")
    
    def log_message(self, format, *args):
        # Suppress server logs
        pass

def create_sample_traffic():
    """Generate sample HTTP traffic with passwords"""
    
    print("[*] Creating sample HTTP traffic with passwords...")
    
    # Start a simple HTTP server in background
    server = HTTPServer(('localhost', 8080), TestHTTPHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    time.sleep(1)  # Let server start
    
    # Generate various HTTP requests with passwords
    import urllib.request
    import base64
    
    try:
        # 1. Basic Authentication
        print("[*] Generating Basic Auth request...")
        auth_string = base64.b64encode(b'admin:armyquest2025').decode('ascii')
        req = urllib.request.Request('http://localhost:8080/login')
        req.add_header('Authorization', f'Basic {auth_string}')
        urllib.request.urlopen(req, timeout=2)
        
        # 2. Password in URL parameter
        print("[*] Generating URL parameter password...")
        urllib.request.urlopen('http://localhost:8080/login?username=soldier&password=indianarmy123', timeout=2)
        
        # 3. POST form data
        print("[*] Generating POST form data...")
        post_data = urllib.parse.urlencode({
            'username': 'ctfplayer',
            'password': 'quest2025flag',
            'action': 'login'
        }).encode('utf-8')
        
        req = urllib.request.Request('http://localhost:8080/submit', data=post_data)
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        urllib.request.urlopen(req, timeout=2)
        
        # 4. Cookie with password
        print("[*] Generating request with password cookie...")
        req = urllib.request.Request('http://localhost:8080/dashboard')
        req.add_header('Cookie', 'sessionid=abc123; remember_password=securepass456')
        urllib.request.urlopen(req, timeout=2)
        
        time.sleep(1)
        
    except Exception as e:
        print(f"[!] Some requests failed (normal): {e}")
    
    server.shutdown()
    print("[+] Sample traffic generation complete!")

def main():
    print("=========================================")
    print("Indian Army Quest 2025 - Sample PCAP Creator")
    print("=========================================")
    print()
    
    # Check if tcpdump is available
    try:
        subprocess.run(['tcpdump', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("[!] tcpdump not found. Please install with: sudo apt install tcpdump")
        sys.exit(1)
    
    pcap_file = "sample_ctf_traffic.pcap"
    
    print(f"[*] Creating sample pcap file: {pcap_file}")
    print("[*] This will capture HTTP traffic with various password scenarios")
    print()
    
    # Start tcpdump capture
    tcpdump_cmd = [
        'sudo', 'tcpdump', '-i', 'lo', '-w', pcap_file,
        'port', '8080', '-s', '0'
    ]
    
    print(f"[*] Starting packet capture...")
    capture_process = subprocess.Popen(tcpdump_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    time.sleep(2)  # Let tcpdump start
    
    # Generate traffic
    create_sample_traffic()
    
    time.sleep(2)  # Let tcpdump capture everything
    
    # Stop capture
    capture_process.terminate()
    capture_process.wait()
    
    print(f"[+] Sample pcap file created: {pcap_file}")
    print()
    print("Now you can analyze it with:")
    print(f"  ./quick_analysis.sh {pcap_file}")
    print(f"  python3 analyze_pcap.py {pcap_file}")
    print()
    print("Expected passwords to find:")
    print("  1. Basic Auth: admin:armyquest2025")
    print("  2. URL Parameter: indianarmy123") 
    print("  3. POST Data: quest2025flag")
    print("  4. Cookie: securepass456")

if __name__ == "__main__":
    main()