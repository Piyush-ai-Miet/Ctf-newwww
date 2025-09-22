#!/usr/bin/env python3
"""
CTF Challenge Web Application for Indian Cyber Quest
Author: Piyush Dhariwal
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import base64
import hashlib
import time
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'TCQ2025_secret_key_for_session'

# Flags for the CTF
FLAGS = {
    'flag1': 'TCQ2025{S3Cur1ty_Br3@k_P@55ed}',
    'flag2': 'TCQ2025{F!ow3r#92@tY8&Vk}',
    'flag3': 'TCQ2025{Y0u_kn0w_i5_th15_RaC3}',
    'flag4': 'TCQ2025{PwN_2_0wN_N0w_Y0u_ar3_5t3M}',
    'flag5': 'TCQ2025{D4Y_0_T0_zeR0_d4Y}'
}

@app.route('/')
def home():
    """
    Main page - Flag1 Challenge: Security Break Password
    Flag is hidden in a comment and accessible via weak password
    """
    return render_template('index.html')

@app.route('/page')
def page():
    """
    Second page - Flag2 Challenge: Flower Power
    Flag is hidden in base64 encoded form
    """
    # Flag2 encoded in base64: TCQ2025{F!ow3r#92@tY8&Vk}
    encoded_flag = base64.b64encode(FLAGS['flag2'].encode()).decode()
    return render_template('page.html', encoded_data=encoded_flag)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login page for Flag1 - weak password check
    """
    if request.method == 'POST':
        password = request.form.get('password', '')
        # Weak password: admin123
        if password == 'admin123':
            session['logged_in'] = True
            return jsonify({'success': True, 'flag': FLAGS['flag1'], 'message': 'Security Break Passed!'})
        else:
            return jsonify({'success': False, 'message': 'Invalid password'})
    return render_template('login.html')

@app.route('/source')
def source():
    """
    Flag3 Challenge: Race condition / timing attack
    """
    current_time = int(time.time())
    # Flag3 is only visible during specific time conditions (race condition)
    if current_time % 10 == 0:  # Available every 10 seconds at exact second
        return jsonify({'flag': FLAGS['flag3'], 'message': 'You know this race!'})
    else:
        return jsonify({'message': 'Try again at the right time...', 'hint': 'Timing is everything'})

@app.route('/admin')
def admin():
    """
    Flag4 Challenge: Pwn to Own
    Requires session manipulation or direct access
    """
    if session.get('logged_in') or request.headers.get('X-Admin-Access') == 'pwn2own':
        return jsonify({'flag': FLAGS['flag4'], 'message': 'Now you are 5t3M (system)!'})
    else:
        return jsonify({'error': 'Access denied. You need to pwn this to own it.'})

@app.route('/zero-day')
def zero_day():
    """
    Flag5 Challenge: Day 0 to Zero Day
    Hidden endpoint, requires specific parameter
    """
    day_param = request.args.get('day', '')
    if day_param == '0':
        return jsonify({'flag': FLAGS['flag5'], 'message': 'Day 0 to Zero Day achieved!'})
    else:
        return jsonify({'hint': 'What comes before day 1?'})

@app.route('/robots.txt')
def robots():
    """
    Robots.txt file that hints at hidden endpoints
    """
    return '''User-agent: *
Disallow: /admin
Disallow: /source
Disallow: /zero-day
Allow: /
Allow: /page

# Hidden paths for CTF:
# /admin - requires authentication
# /source - timing sensitive
# /zero-day?day=0 - parameter required
'''

@app.route('/hint')
def hint():
    """
    Hints for CTF participants
    """
    hints = {
        'flag1': 'Check the source code and try common passwords',
        'flag2': 'Look for encoded data in the page source',
        'flag3': 'Timing is everything - keep trying at different seconds',
        'flag4': 'Try to become admin or use special headers',
        'flag5': 'Check robots.txt and think about day zero'
    }
    return jsonify(hints)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)