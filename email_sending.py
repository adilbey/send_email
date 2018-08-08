# smtplib is a library provided by Python for working on emails
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Write your email address
sender = "my_email@gmail.com"
# Write the email address/adresses you want to send the email to
# to enter multiple adresses add ; between each email address
recipient = "example_email@gmail.com; another_example@hotmail.com"

email = MIMEMultipart()
email['From'] = sender
email['To'] = recipient
# Write the subject of the email
email['Subject'] = "Email subject"
# Write the text you want to email
body = "Email text you want to send"
email.attach(MIMEText(body, 'plain'))

# You can attach files too if you want
filename = r'PATH of the attachment'
attachment = open(filename, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
email.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, "PASSWORD of sender")
text = email.as_bytes()
server.sendmail(sender, recipient, text)
server.quit()

print("successfully sent email to ", recipient)