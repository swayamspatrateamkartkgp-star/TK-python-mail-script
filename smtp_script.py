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

# Updated body for Mr. Virendra Somwanshi at Federal Bank Ltd
HTML_BODY = """
<body>
    <div class="content">
        <p>Dear Mr. Somwanshi,</p>
        
        <p>My name is <strong>{your_name}</strong>, representing <span class="highlight">TeamKART</span>, the premier Formula Student team of <strong>IIT Kharagpur</strong>. I am reaching out to you as the Country Head of Wealth Management at Federal Bank to explore a CSR partnership that invests in India’s high-value technical human capital—a mission that aligns with your institution's commitment to growth, excellence, and national development.</p>

        <h3>Investing in Technical Excellence and Future Assets</h3>
        <p>Operating as a specialized research cell under the <strong>Department of Mechanical Engineering at IIT Kharagpur</strong>, TeamKART provides an elite environment for students to master complex engineering and project management. Our initiative supports Federal Bank's vision for social and educational empowerment through:</p>
        <ul>
            <li><strong>Development of Specialized Talent:</strong> Our members master end-to-end product lifecycles, utilizing advanced validation tools like ANSYS to ensure technical rigor and industrial readiness.</li>
            <li><strong>High-Impact Sustainable Research:</strong> We have successfully pioneered green technology within our institute by manufacturing our <strong>first electric vehicle (KE-1)</strong>, promoting zero-emission powertrain innovation.</li>
            <li><strong>Disciplined Resource Management:</strong> TeamKART emphasizes fiscal responsibility and lean manufacturing, ensuring that technical innovation is balanced with high-efficiency resource allocation.</li>
        </ul>

        <h3>Institutional Legacy & Performance Record</h3>
        <p>Reflecting the prestigious academic standards of <strong>IIT Kharagpur</strong>, our team has a consistent record of high-performance delivery:</p>
        <ul>
            <li><strong>Top 10 Overall Finish</strong> at Formula Bharat 2023.</li>
            <li><strong>3rd Place</strong> in the Cost & Manufacturing Event, validating our expertise in cost-effective engineering and operations.</li>
            <li>A decade-long legacy of manufacturing <strong>eight combustion vehicles</strong> prior to our strategic shift toward high-performance electric vehicle research.</li>
        </ul>

        <p>A CSR collaboration with Federal Bank would directly support the advancement of sustainable technical research and the development of the next generation of Indian innovators. I would welcome the opportunity to discuss how our team’s objectives can align with Federal Bank’s vision for technical and educational growth.</p>
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
