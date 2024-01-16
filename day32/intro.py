import smtplib

my_email="somethingisfishy93@gmail.com"
password="dlwnxjxpiqcvmnly"
try:
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as connection:
        # connection.starttls() #TLS stands for Transport Layer Security, this command encrpts/secures the email
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="somethingisfishy93@yahoo.com",msg="Subject: hello!\n\nHey! welcome..")

except Exception as e:
    print(f"Error: {e}")
# import smtplib
# from email.mime.text import MIMEText

# my_email = "somethingisfishy93@gmail.com"
# password = "dlwnxjxpiqcvmnly"
# recipient_email = "somethingisfishy93@yahoo.com"

# # Create a MIMEText object to represent your message
# message = MIMEText("Hey! welcome..")

# # Set the "From" and "To" addresses in the MIMEText object
# message["From"] = my_email
# message["To"] = recipient_email
# message["Subject"] = "Subject of the email"  # You can add a subject if needed

# try:
#     # Use the SMTP_SSL class for a secure connection
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=f"subject:Hello subject!\n\n{message.as_string()}")
#     print("Email sent successfully!")
# except Exception as e:
#     print(f"Error: {e}")


import datetime as dt
now=dt.datetime.now()
year=now.year
month=now.month
day=now.weekday()
print(year)
print(type(now))

dob=dt.datetime(year=2000,month=1,day=1)
print(dob)
