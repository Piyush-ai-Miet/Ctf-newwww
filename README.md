# Indian Army Quest 2025 - CTF PCAP Analysis

This repository contains tools for analyzing packet capture (pcap) files to extract passwords from HTTP traffic for the Indian Army Quest 2025 CTF challenge.

## Files

- `analyze_pcap.py` - Comprehensive Python script for PCAP analysis
- `quick_analysis.sh` - Quick bash script for immediate results
- `CTF_ANALYSIS_GUIDE.md` - Detailed guide and documentation

## Quick Start

1. **Install dependencies:**
   ```bash
   sudo apt install tshark tcpdump python3
   ```

2. **Analyze a pcap file:**
   ```bash
   # Quick analysis
   ./quick_analysis.sh your_capture.pcap
   
   # Detailed analysis
   python3 analyze_pcap.py your_capture.pcap
   ```

## What it finds

- HTTP Basic Authentication passwords
- Form submission passwords (POST data)
- URL parameter passwords
- Authentication cookies
- JSON payload credentials

Perfect for CTF challenges involving network traffic analysis!
