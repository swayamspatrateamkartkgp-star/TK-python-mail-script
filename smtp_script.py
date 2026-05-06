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

# Updated body for Maddy M. at HCLTech (ESG & Advocacy focus)
HTML_BODY = """
<body>
    <div class="content">
        <p>Dear Maddy,</p>
        
        <p>My name is <strong>{your_name}</strong>, representing <span class="highlight">TeamKART</span>, the official Formula Student team of <strong>IIT Kharagpur</strong>. I am reaching out to you as an advocate for Sustainability and ESG at HCLTech to explore a partnership that bridges technical innovation with the core pillars of social and environmental responsibility.</p>

        <h3>Fostering ESG Excellence through Engineering</h3>
        <p>Operating under the <strong>Department of Mechanical Engineering at IIT Kharagpur</strong>, TeamKART functions as a student-led research cell dedicated to advancing the future of sustainable mobility and engineering education. Our mission aligns with your advocacy goals through:</p>
        <ul>
            <li><strong>Environmental Leadership:</strong> Our successful transition to electric vehicle technology, marked by our <strong>first EV (KE-1)</strong>, serves as a platform for zero-emission powertrain research.</li>
            <li><strong>Social Sustainability & Education:</strong> We provide students from diverse backgrounds with hands-on exposure to advanced simulation and validation tools like ANSYS, fostering technical equity and high-level employability.</li>
            <li><strong>Ethical Project Governance:</strong> Our team emphasizes responsible resource management and cost-efficiency, ensuring technical complexity is balanced with commercial and ethical viability.</li>
        </ul>

        <h3>Legacy of Technical Innovation</h3>
        <p>Rooted in the academic excellence of <strong>IIT Kharagpur</strong>, our team has a proven track record of performance:</p>
        <ul>
            <li><strong>Top 10 Overall Finish</strong> at Formula Bharat 2023.</li>
            <li><strong>3rd Place</strong> in the Cost & Manufacturing Event, validating our expertise in responsible manufacturing.</li>
            <li>A legacy of <strong>eight combustion vehicles</strong> built since 2008, providing the foundation for our current strategic pivot to electric vehicle innovation.</li>
        </ul>

        <p>A CSR partnership with HCLTech would directly support the development of sustainable technical talent in India. We would welcome the opportunity to discuss how our team's research can support HCLTech’s vision for a sustainable and socially responsible future.</p>
"""

HTML_TAIL="""
        <p><strong>For detailed information, please refer to:</strong></p>
        <div class="links-section">
            <a href="{brochure_link}">Our Sponsorship Brochure</a>
            <a href="http://www.teamkart.org/">Official Team Website</a>
            <a href="https://youtube.com/@teamkart3652">15 Years of Engineering Legacy</a>
            <a href="https://www.instagram.com/team.kart/">Instagram Handle</a>
        </div>

        <div class="footer">
            <p>Thank you for your time and consideration.</p>
            <p>Warm regards,</p>
            <table style="border-collapse: collapse; font-family: Arial, sans-serif;">
                <tr>
                    <td style="padding-right: 15px;">
                        <img src="{tk_logo_url}" width="100" style="display: block;">
                    </td>
                    <td style="border-left: 2px solid #E31E24; padding: 0;"></td>
                    <td style="padding-left: 15px; line-height: 1.4; font-size: 10pt;">
                        <span style="font-weight: bold; font-size: 11pt;">{your_name}</span><br>
                        {your_year}-Year Undergraduate Student<br>
                        {your_department}<br>
                        {your_role}, TeamKART<br>
                        IIT Kharagpur<br>
                        Contact: {your_contact}<br>
                        <a href="{your_linkedin}" style="color: #0044cc;">LinkedIn</a> | 
                        <a href="{your_facebook}" style="color: #0044cc;">Facebook</a>
                    </td>
                </tr>
            </table>
        </div>
    </div>
</body>
</html>
"""

def send_emails():
    now = datetime.now()
    today_date = now.strftime("%d-%m-%Y")
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        print(f"Successfully logged in. Sending emails for {today_date}...")
    except Exception as e:
        print(f"Login failed: {e}")
        return

    for index, row in data.iterrows():
        try:
            msg = MIMEMultipart("alternative")
            msg["From"] = formataddr((YOUR_NAME, EMAIL))
            msg["To"] = row["Email"]
            msg["Cc"] = ", ".join(CC_EMAILS)
            msg["Subject"] = SUBJECT
            msg["Message-ID"] = make_msgid(domain="gmail.com")

            html_template = HTML_HEAD + HTML_BODY + HTML_TAIL
            
            html_content = html_template.format(
                your_name = YOUR_NAME,
                brochure_link = BROCHURE_URL,
                tk_logo_url = TK_LOGO_URL,
                your_year = YOUR_YEAR,
                your_department = YOUR_DEPARTMENT,
                your_role = YOUR_ROLE_TK,
                your_contact = YOUR_CONTACT,
                your_linkedin = YOUR_LINKED_IN,
                your_facebook = YOUR_FACEBOOK
            )

            msg.attach(MIMEText(html_content, "html"))
            recipients = [row["Email"]] + CC_EMAILS
            server.sendmail(EMAIL, recipients, msg.as_string())
            ist_now = datetime.now() + timedelta(hours=5, minutes=30)
            print(f"Sent email to {row['Email']} at {ist_now.strftime('%H:%M:%S')} IST")
            
            time.sleep(random.randint(25, 55))

        except Exception as e:
            print(f"Error sending to {row['Email']}: {e}")

    server.quit()

if __name__ == "__main__":
    send_emails()
