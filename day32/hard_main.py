# ##################### Hard Starting Project ######################
# import pandas
# import random
# import datetime as dt
# import smtplib
# # 1. Update the birthdays.csv with your friends & family's details. 
# # HINT: Make sure one of the entries matches today's date for testing purposes. 
# birthdays=pandas.read_csv("birthdays.csv")
# now=dt.datetime.now()
# present_month=now.month
# present_day=now.day
# # 2. Check if today matches a birthday in the birthdays.csv
# # HINT 1: Only the month and day matter. 
# # HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# # birthdays_dict = {
# #     (month, day): data_row
# # }
# birthdays_dict={}
# for index, row in birthdays.iterrows():
#     birthdays_dict[(row["day"], row["month"])]=index


# #HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# letters=["letter_1.txt","letter_2.txt","letter_3.txt"]
# if (present_day,present_month) in birthdays_dict:
#     letter=random.choice(letters)
#     with open(file=f"letter_templates/{letter}",mode="a") as bdletter:
#         x=[NAME]
#         x.replace(x,index["name"])
# # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# # HINT: https://www.w3schools.com/python/ref_string_replace.asp

# # 4. Send the letter generated in step 3 to that person's email address.
# # HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# my_email="something@gmail.com"
# password="pass"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  
#     connection.login(user=my_email, password=password)
#     subject="Happy birthday!"
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="email",
#                         msg=letter)

# her solution
from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "something@gmail.com"
MY_PASSWORD = "pass"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
