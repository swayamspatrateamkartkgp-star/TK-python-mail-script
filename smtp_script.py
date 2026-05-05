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

# Subject Line as requested
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

# Updated body for Ms. Monica Gupta at HCL Technologies
HTML_BODY = """
<body>
    <div class="content">
        <p>Dear Ms. Gupta,</p>
        
        <p>My name is <strong>{your_name}</strong>, representing <span class="highlight">TeamKART</span>, the official Formula Student team of <strong>IIT Kharagpur</strong>. I am reaching out to you at HCL Technologies Limited to explore a collaborative opportunity where technical innovation meets professional skill-building—a core value reflected in HCL's commitment to tech-driven transformation.</p>

        <h3>Empowering Innovation Through Research</h3>
        <p>Operating under the <strong>Department of Mechanical Engineering at IIT Kharagpur</strong>, TeamKART is a specialized research cell where the next generation of engineers executes end-to-end product development. Our initiative aligns with HCL’s focus on technical education and research excellence:</p>
        <ul>
            <li><strong>Digital and Physical Engineering:</strong> Students utilize advanced CAD and ANSYS structural validation to bridge the gap between high-level theory and industrial application.</li>
            <li><strong>Sustainability and Green Tech:</strong> We have pivoted to the electric vehicle sector, successfully manufacturing our <strong>first electric vehicle (KE-1)</strong> to advance the future of sustainable mobility.</li>
            <li><strong>Skill Transformation:</strong> Our members master real-world project execution, developing specialized expertise in powertrain optimization and battery management.</li>
        </ul>

        <h3>Legacy of Technical Excellence</h3>
        <p>The academic rigor of <strong>IIT Kharagpur</strong> has fueled a decade-long legacy of performance. Our milestones include:</p>
        <ul>
            <li><strong>Top 10 Overall Finish</strong> at Formula Bharat 2023.</li>
            <li><strong>3rd Place</strong> in the Cost & Manufacturing Event, showcasing our ability to balance technical complexity with commercial viability.</li>
            <li>Manufacturing of <strong>eight combustion vehicles</strong> prior to our current focus on high-performance EV research.</li>
        </ul>

        <p>A CSR partnership with HCL Technologies would directly support the advancement of technical education and engineering research in India. We would welcome the chance to discuss how our team’s objectives can align with HCL’s vision for technical empowerment.</p>
"""

HTML_TAIL="""
        <p><strong>For more information, please refer to:</strong></p>
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
