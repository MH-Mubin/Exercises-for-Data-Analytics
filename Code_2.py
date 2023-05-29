
import pandas as pd
import numpy as np
from statistics import mean,median,mode,stdev
import scipy.stats as stats
import matplotlib.pyplot as plt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
import datetime 
import pytz

#Dataset
age=[2,3,4,6,7,8,9,1,12,13,14,15,16,17,5,10,30,20,39,40,19,18,27]

#to find mean
mean=mean(age)
#print(mean)

#to find median, mode and standard deviation
median=median(age)
mode=mode(age)
stdev=stdev(age)
# print(median)
# print(mode)
# print(stdev)

data = np.array(age)

#to find Z-score
stats.zscore(data)

# For histogram
plt.hist(age,bins='auto')
plt.savefig("fig.png")
plt.show()

# for date & time
today = datetime.date.today()
print(today)

BDTz = pytz.timezone("Asia/Dhaka") 
timeInBD = datetime.datetime.now(BDTz)
current_Time_BD = timeInBD.strftime("%H:%M:%S")

#print("The current time in Dhaka is:", current_Time_BD)

#email and passward
sender_address = 'mahmudhasanmubin1996@gmail.com'
sender_pass = 'snhkxehubrqrtjpm'
receiver_address = 'almehady@gmail.com'
bcc='dev@fridaysoft.net'
subject = "Histogram Report " + str(today)
message = '''Dear sir,
Please find the attatchment.


Regards,
Mahmud Hasan Mubin
Trainee(Data Analytics)
ADN Diginet '''+ current_Time_BD
msg = MIMEMultipart()
msg['From'] = sender_address
msg['To'] = receiver_address
msg['Bcc']=bcc
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))
#Setup the MIME
with open('fig.png', 'rb') as file:
    image = MIMEImage(file.read(), name='fig.png')
    msg.attach(image)
# Connect to the SMTP server and send the email
with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
    server.starttls()
    server.login(sender_address, sender_pass)
    server.send_message(msg)

print('Email sent successfully')
