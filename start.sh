#!/bin/bash

# CTF 2025 Startup Script

echo "🚩 Starting CTF 2025 Web Application..."
echo ""

# Check if Flask is installed
if ! python3 -c "import flask" &> /dev/null; then
    echo "Installing Flask..."
    pip install flask
    echo ""
fi

# Check if requirements are met
if [ -f "requirements.txt" ]; then
    echo "Installing requirements..."
    pip install -r requirements.txt
    echo ""
fi

echo "Starting Flask application on port 5000..."
echo "Access the CTF at: http://localhost:5000"
echo "Or at: http://192.168.29.153:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the application
python3 app.py