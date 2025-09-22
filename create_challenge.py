#!/usr/bin/env python3
"""
Create a PCAP file with unencrypted protocols containing passwords for CTF challenge.
"""

import socket
import subprocess
import time
import base64
import threading
import os

def create_simple_pcap():
    """Create a simple PCAP with clear text protocols"""
    
    pcap_file = "/home/runner/work/Ctf-newwww/Ctf-newwww/challenge.pcap"
    
    # Remove old file if exists
    if os.path.exists(pcap_file):
        os.remove(pcap_file)
    
    # Start tcpdump to capture loopback traffic
    print("Starting packet capture on loopback...")
    capture_proc = subprocess.Popen([
        'sudo', 'tcpdump', '-i', 'lo', '-w', pcap_file, '-s', '65535'
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    time.sleep(2)  # Let tcpdump start
    
    print("Generating unencrypted network traffic with passwords...")
    
    # Create HTTP Basic Auth traffic (unencrypted)
    try:
        # HTTP Basic Auth with clear credentials
        credentials = base64.b64encode(b"ctfuser:flag{basic_auth_secret}").decode('ascii')
        
        # Create a simple HTTP server response
        def http_server():
            server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_sock.bind(('127.0.0.1', 8080))
            server_sock.listen(1)
            
            conn, addr = server_sock.accept()
            data = conn.recv(1024)
            
            # Send HTTP response
            response = b"HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nAccess granted"
            conn.send(response)
            conn.close()
            server_sock.close()
        
        # Start server in background
        server_thread = threading.Thread(target=http_server)
        server_thread.start()
        
        time.sleep(1)
        
        # Send HTTP request with Basic Auth
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('127.0.0.1', 8080))
        
        http_request = f"""GET /admin HTTP/1.1\r
Host: localhost:8080\r
User-Agent: CTF-Client/1.0\r
Authorization: Basic {credentials}\r
Connection: close\r
\r
""".replace('\r', '\r\n')
        
        client_sock.send(http_request.encode())
        response = client_sock.recv(1024)
        client_sock.close()
        
        server_thread.join()
        print("✓ Created HTTP Basic Auth traffic")
        
    except Exception as e:
        print(f"Error creating HTTP traffic: {e}")
    
    time.sleep(1)
    
    # Create FTP-style traffic
    try:
        def ftp_server():
            server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_sock.bind(('127.0.0.1', 2121))
            server_sock.listen(1)
            
            conn, addr = server_sock.accept()
            
            # FTP conversation
            conn.send(b"220 Welcome to CTF FTP Server\r\n")
            data = conn.recv(1024)  # USER command
            conn.send(b"331 Password required for ftpuser\r\n")
            data = conn.recv(1024)  # PASS command
            conn.send(b"230 Login successful\r\n")
            
            conn.close()
            server_sock.close()
        
        # Start FTP server
        ftp_thread = threading.Thread(target=ftp_server)
        ftp_thread.start()
        
        time.sleep(1)
        
        # Create FTP client
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('127.0.0.1', 2121))
        
        # Read welcome message
        response = client_sock.recv(1024)
        
        # Send USER command
        client_sock.send(b"USER ftpuser\r\n")
        response = client_sock.recv(1024)
        
        # Send PASS command with flag
        client_sock.send(b"PASS flag{ftp_password_hidden}\r\n")
        response = client_sock.recv(1024)
        
        client_sock.close()
        ftp_thread.join()
        print("✓ Created FTP login traffic")
        
    except Exception as e:
        print(f"Error creating FTP traffic: {e}")
    
    time.sleep(1)
    
    # Create Telnet-style traffic
    try:
        def telnet_server():
            server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_sock.bind(('127.0.0.1', 2323))
            server_sock.listen(1)
            
            conn, addr = server_sock.accept()
            
            # Telnet login simulation
            conn.send(b"CTF Telnet Server\r\nlogin: ")
            data = conn.recv(1024)  # username
            conn.send(b"password: ")
            data = conn.recv(1024)  # password
            conn.send(b"Welcome to the system!\r\n$ ")
            
            conn.close()
            server_sock.close()
        
        # Start Telnet server
        telnet_thread = threading.Thread(target=telnet_server)
        telnet_thread.start()
        
        time.sleep(1)
        
        # Create Telnet client
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('127.0.0.1', 2323))
        
        # Read login prompt
        response = client_sock.recv(1024)
        
        # Send username
        client_sock.send(b"admin\r\n")
        response = client_sock.recv(1024)
        
        # Send password with flag
        client_sock.send(b"flag{telnet_admin_pass}\r\n")
        response = client_sock.recv(1024)
        
        client_sock.close()
        telnet_thread.join()
        print("✓ Created Telnet login traffic")
        
    except Exception as e:
        print(f"Error creating Telnet traffic: {e}")
    
    time.sleep(2)
    
    # Stop packet capture
    capture_proc.terminate()
    capture_proc.wait()
    
    if os.path.exists(pcap_file):
        size = os.path.getsize(pcap_file)
        print(f"✅ PCAP file created: {pcap_file} ({size} bytes)")
        return True
    else:
        print("❌ Failed to create PCAP file")
        return False

if __name__ == "__main__":
    if create_simple_pcap():
        print("\n🎯 CTF Challenge Ready!")
        print("The PCAP file contains multiple passwords hidden in different protocols.")
        print("Use the find_passwords.py script to analyze and find them!")
    else:
        print("Failed to create CTF challenge")