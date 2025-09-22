#!/bin/bash
# CTF Challenge Runner Script
# Indian Cyber Quest 2025

echo "🚩 Indian Cyber Quest 2025 - CTF Challenge Setup 🚩"
echo "================================================="
echo

# Check if Python and pip are available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is required but not installed."
    exit 1
fi

if ! command -v pip &> /dev/null && ! command -v pip3 &> /dev/null; then
    echo "❌ pip is required but not installed."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Check if installation was successful
if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies."
    exit 1
fi

echo "✅ Dependencies installed successfully!"
echo

# Start the Flask application
echo "🚀 Starting CTF Challenge Server..."
echo "🌐 Server will be available at: http://localhost:5000"
echo "🌐 Or on your network at: http://192.168.29.153:5000"
echo
echo "📚 For detailed walkthrough, see: WALKTHROUGH.md"
echo "🔧 To generate traffic for PCAP analysis, run: python generate_traffic.py"
echo
echo "Press Ctrl+C to stop the server"
echo "================================================="

# Start the Flask app
python app.py