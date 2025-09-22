# CTF 2025 - Web Application Challenge

A Capture The Flag (CTF) web application containing 5 hidden flags for security enthusiasts and penetration testers.

## 🚩 Challenge Overview

This CTF demonstrates common web application vulnerabilities and security testing techniques. Participants must discover 5 flags hidden throughout the application using various methods:

- **Flag1:** `TCQ2025{S3Cur1ty_Br3@k_P@55ed}` - Authentication bypass
- **Flag2:** `TCQ2025{F!ow3r#92@tY8&Vk}` - HTTP header analysis  
- **Flag3:** `TCQ2025{Y0u_kn0w_i5_th15_RaC3}` - Race condition exploitation
- **Flag4:** `TCQ2025{PwN_2_0wN_N0w_Y0u_ar3_5t3M}` - Command injection simulation
- **Flag5:** `TCQ2025{D4Y_0_T0_zeR0_d4Y}` - User-Agent spoofing

## 🔧 Setup Instructions

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application:**
   ```bash
   python3 app.py
   ```

3. **Access the Challenge:**
   - Open browser to `http://localhost:5000` or `http://192.168.29.153:5000`
   - Start hunting for flags!

## 📚 Available Endpoints

- `/` - Main challenge page with overview
- `/page` - Primary challenge page (as requested)
- `/login` - Authentication system
- `/api/flower` - API endpoint with hidden data
- `/race` - Timing-based challenge
- `/system` - Command testing interface
- `/vulnerability` - Security scanner simulation
- `/robots.txt` - Reconnaissance hints

## 📖 Complete Walkthrough

For detailed step-by-step solutions, see [WALKTHROUGH.md](WALKTHROUGH.md)

## 🎯 Learning Objectives

- Web application penetration testing
- HTTP protocol analysis
- Authentication security
- API security testing
- Timing attack techniques
- Input validation vulnerabilities
- Header manipulation
- Reconnaissance methods

## ⚠️ Disclaimer

This application is designed for educational purposes only. Use only in controlled environments for learning cybersecurity concepts.

## 🏁 Getting Started

1. Visit the main page to get oriented
2. Read the hints and explore different endpoints
3. Use tools like curl, browser dev tools, and scripts
4. Check the walkthrough if you get stuck
5. Have fun learning!
