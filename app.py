#!/usr/bin/env python3
"""
CTF Web Application
Contains 5 hidden flags for participants to discover
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import time
import hashlib
import base64
import os
from functools import wraps

app = Flask(__name__)
app.secret_key = 'ctf_secret_key_2025'

# Flag storage
FLAGS = {
    'flag1': 'TCQ2025{S3Cur1ty_Br3@k_P@55ed}',
    'flag2': 'TCQ2025{F!ow3r#92@tY8&Vk}',
    'flag3': 'TCQ2025{Y0u_kn0w_i5_th15_RaC3}',
    'flag4': 'TCQ2025{PwN_2_0wN_N0w_Y0u_ar3_5t3M}',
    'flag5': 'TCQ2025{D4Y_0_T0_zeR0_d4Y}'
}

# Race condition variables
race_condition_counter = 0
race_condition_window = 0

def rate_limit(max_per_second=1):
    """Rate limiting decorator for race condition challenge"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            global race_condition_counter, race_condition_window
            current_time = time.time()
            
            if current_time - race_condition_window > 1:
                race_condition_counter = 0
                race_condition_window = current_time
            
            race_condition_counter += 1
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/')
def index():
    """Main page with basic information"""
    return render_template('index.html')

@app.route('/page')
def page():
    """Secondary page mentioned in the problem statement"""
    return render_template('page.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page for Flag1 - Security/Password challenge"""
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        # Simple password challenge - weak credentials
        if username == 'admin' and password == 'password123':
            session['logged_in'] = True
            session['username'] = username
            return render_template('dashboard.html', flag=FLAGS['flag1'])
        else:
            return render_template('login.html', error='Invalid credentials')
    
    return render_template('login.html')

@app.route('/api/flower')
def flower_api():
    """API endpoint for Flag2 - Hidden in response headers/comments"""
    response = jsonify({
        'message': 'Welcome to the flower API',
        'status': 'active',
        'version': '1.0'
    })
    
    # Flag2 hidden in custom header
    response.headers['X-Flower-Token'] = base64.b64encode(FLAGS['flag2'].encode()).decode()
    return response

@app.route('/race')
@rate_limit(max_per_second=5)
def race():
    """Race condition endpoint for Flag3"""
    global race_condition_counter
    
    # Flag3 appears only during specific race condition timing
    if race_condition_counter >= 3 and race_condition_counter <= 5:
        return jsonify({
            'status': 'success',
            'message': 'Race condition detected!',
            'flag': FLAGS['flag3'],
            'counter': race_condition_counter
        })
    else:
        return jsonify({
            'status': 'waiting',
            'message': 'Keep trying...',
            'counter': race_condition_counter
        })

@app.route('/system')
def system():
    """System information page for Flag4 - Command injection simulation"""
    cmd = request.args.get('cmd', 'ls')
    
    # Simulate command injection vulnerability (safely)
    if cmd == 'cat /etc/flag.txt':
        return f"<pre>System output:\n{FLAGS['flag4']}</pre>"
    elif cmd == 'ls':
        return "<pre>System output:\nindex.html\npage.html\nflag.txt</pre>"
    elif cmd == 'whoami':
        return "<pre>System output:\nctf-user</pre>"
    else:
        return f"<pre>System output:\nCommand '{cmd}' not found or not allowed</pre>"

@app.route('/vulnerability')
def vulnerability():
    """Zero-day simulation for Flag5"""
    user_agent = request.headers.get('User-Agent', '')
    
    # Flag5 appears with specific User-Agent
    if 'CTF-Scanner-2025' in user_agent:
        return jsonify({
            'vulnerability': 'detected',
            'type': 'zero-day',
            'flag': FLAGS['flag5'],
            'message': 'Vulnerability scanner detected the zero-day exploit!'
        })
    else:
        return jsonify({
            'status': 'secure',
            'message': 'No vulnerabilities detected',
            'scanner': 'unknown'
        })

@app.route('/robots.txt')
def robots():
    """Robots.txt with hints"""
    return """User-agent: *
Disallow: /admin
Disallow: /secret
Disallow: /api/
Allow: /race
Allow: /system
Allow: /vulnerability

# Flag hunters: check the flower API headers
# System admins: try common commands on /system?cmd=
# Security researchers: use proper User-Agent on /vulnerability
"""

@app.route('/source')
def source():
    """Source code disclosure for debugging"""
    return "<pre>This endpoint would show source code in a real CTF</pre>"

@app.errorhandler(404)
def not_found(error):
    """Custom 404 page with hints"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)