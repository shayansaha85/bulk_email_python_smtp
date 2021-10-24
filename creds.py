import smtplib
import email.mime.text as emt
import email.mime.multipart as emm
import pandas as pd

# user credentials (can be placed in a .properties file)
email_user = 'shayan851997@gmail.com'
email_password = '***********'

df = pd.read_csv("./email_ids.csv")
email_send = list(df['email_id'])


# email part
subject = 'FINAL CHECK'
body = 'Hello, this is a check email'


message = emm.MIMEMultipart()
message['From'] = email_user
message['To'] = ", ".join(email_send)
message['Subject'] = subject

message.attach(emt.MIMEText(body,'plain'))
text = message.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)
server.sendmail(email_user,email_send,text)
server.quit()