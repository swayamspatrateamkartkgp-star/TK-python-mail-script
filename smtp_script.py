import os
import smtplib
import pandas as pd
import time
import random
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr, make_msgid

# Email credentials
EMAIL = "swayamspatra.teamkartkgp@gmail.com"
PASSWORD = os.environ.get("EMAIL_PASSWORD")

# Correct csv file name 
data = pd.read_csv("test_csv.csv")

# CC List updated with Mohamed and Samarth
CC_EMAILS = [
    "samarthkalgaonkar.teamkartkgp@gmail.com",
    "mohamed.teamkartkgp@gmail.com"
] 

# Definitions
BROCHURE_URL = "https://online.fliphtml5.com/TeamKart/1-Qt2Y/" 
YOUR_NAME = "Swayam Swarup Patra"
TK_LOGO_URL = "https://imgs.search.brave.com/sv9Okf6sV5Cmz8fLS-RwmJ4UnGHgVvUuETOSC-FziQQ/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly91Z2Mu/cHJvZHVjdGlvbi5s/aW5rdHIuZWUvZTYw/NTFhMTAtMWFiZC00/NWRhLWI4N2QtMzkz/ZDc5MmM5NjE2X3Rl/YW1rYXJ0LWVsZWN0/cmljLWxvZ28td2hp/dGUtc3EucG5nP2lv/PXRydWUmc2l6ZT1h/dmF0YXItdjNfMA"
YOUR_DEPARTMENT = "Department of Mechanical Engineering"
YOUR_YEAR = "First"
YOUR_ROLE_TK = "Mechanical Subsystem Member"
YOUR_CONTACT = "+91 9827790420"
YOUR_LINKED_IN = "https://www.linkedin.com/in/swayam-swarup-patra-95b47539b/"
YOUR_FACEBOOK = "https://www.facebook.com/TeamKART/"

# Subject Line
SUBJECT = "Greetings from Indian Institute of Technology Kharagpur."

HTML_HEAD = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #1a1a1a; max-width: 600px; margin: 0 auto; }}
        .content {{ padding: 20px; border: 1px solid #e0e0e0; border-radius: 8px; }}
        .highlight {{ color: #E31E24; font-weight: bold; }}
        .links-section {{ background-color: #f4f4f4; padding: 15px; border-left: 4px solid #E31E24; margin: 20px 0; }}
        .links-section a {{ color: #E31E24; text-decoration: none; display: block; margin-bottom: 8px; font-size: 14px; }}
        .footer {{ margin-top: 25px; padding-top: 15px; border-top: 1px solid #eeeeee; }}
        h3 {{ color: #1a1a1a; border-bottom: 2px solid #E31E24; display: inline-block; padding-bottom: 2px; }}
    </style>
</head>"""

# Updated body for Jan Strban (CEAT Ltd Focus)
HTML_BODY = """
<body>
    <div class="content">
        <p>Dear Mr. Strban,</p>
        
        <p>My name is <strong>{your_name}</strong>, representing <span class="highlight">TeamKART</span>, the official Formula Student team of <strong>IIT Kharagpur</strong>. I am reaching out to you at CEAT Ltd to explore a CSR collaboration focused on technical innovation and sustainable engineering—a mission that aligns with CEAT's legacy of high-performance manufacturing and safety.</p>

        <h3>Advancing Vehicle Dynamics and Sustainability</h3>
        <p>Operating as a specialized research cell within the <strong>Department of Mechanical Engineering</strong>, TeamKART provides a unique platform for students to master complex automotive engineering. Our initiative aligns with CEAT's technical standards through:</p>
        <ul>
            <li><strong>High-Performance Engineering:</strong> We execute full design and manufacturing cycles, using advanced validation tools like ANSYS to ensure structural integrity and optimized vehicle dynamics.</li>
            <li><strong>The Shift to Electric Mobility:</strong> We have successfully manufactured our <strong>first electric vehicle (KE-1)</strong>, with current research focused on powertrain efficiency and sustainable zero-emission technology.</li>
            <li><strong>Hands-on Skill Development:</strong> Our team bridges the gap between academic theory and industry application, fostering the
