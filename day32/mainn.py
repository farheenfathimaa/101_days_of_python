import datetime as dt
import random
import smtplib

now=dt.datetime.now()
week_day=now.weekday()


with open("quotes.txt") as quotes:
    lines = quotes.readlines()
    
quote=random.choice(lines)

my_email="somethingisfishy93@gmail.com"
password="something"

if week_day==0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  
        connection.login(user=my_email, password=password)
        subject="Today's Quote!"
        connection.sendmail(from_addr=my_email,
                            to_addrs="somethingisfishy93@yahoo.com",
                            msg=f"Subject:{subject}\n\n{quote}")
else:
    print("it's not Monday today!")