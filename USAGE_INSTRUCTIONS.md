# How to Use These CTF Tools

## For the Indian Army Quest 2025 CTF Challenge

### Step 1: Get Your PCAP File
If you have a pcap file from the CTF challenge, place it in this directory.

### Step 2: Quick Analysis
Run the quick analysis script first:
```bash
./quick_analysis.sh your_ctf_file.pcap
```

### Step 3: Detailed Analysis
For comprehensive password extraction:
```bash
python3 analyze_pcap.py your_ctf_file.pcap
```

### Step 4: Manual Investigation
If automated tools don't find the password, use the guide in `CTF_ANALYSIS_GUIDE.md` for manual techniques.

## Testing the Tools

If you want to test these tools without a CTF pcap file:

```bash
# Create a sample pcap file (requires sudo for tcpdump)
sudo python3 create_sample_pcap.py

# Then analyze it
./quick_analysis.sh sample_ctf_traffic.pcap
python3 analyze_pcap.py sample_ctf_traffic.pcap
```

## Common CTF Password Locations

1. **HTTP Basic Auth** - Most common in CTFs
2. **Form POST data** - Login forms
3. **URL parameters** - GET requests with passwords
4. **Cookies** - Session tokens or stored passwords
5. **JSON payloads** - Modern web apps

## Expected Output

The tools will show you:
- Exact password strings found
- Where they were found (URL, POST data, headers, etc.)
- Decoded values (Base64, URL encoding, etc.)

Perfect for solving network analysis challenges in cybersecurity competitions!