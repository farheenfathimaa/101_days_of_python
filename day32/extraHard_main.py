##################### Extra Hard Starting Project ######################
import pandas
import random
import datetime as dt
# 1. Update the birthdays.csv

birthdays=pandas.read_csv("birthdays.csv")
now=dt.datetime.now()
present_month=now.month
present_day=now.day
# 2. Check if today matches a birthday in the birthdays.csv
bd_months=birthdays.month.to_list
bd_date=birthdays.day.to_list

def letter_choose():
    letters=["letter_1.txt","letter_2.txt","letter_3.txt"]
    return random.choice(letters)

# for _ in birthdays:
#     if present_month==bd_months and present_day==bd_date:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
with open(letter_choose,"w") as letter:
    print(letter)
# 4. Send the letter generated in step 3 to that person's email address.




