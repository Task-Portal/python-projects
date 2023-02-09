##################### Extra Hard Starting Project ######################
import os
import random
import smtplib

import  pandas as pd
import  datetime as dt
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data=   pd.read_csv("birthdays.csv")
month = dt.datetime.now().month
day = dt.datetime.now().day

# print(data)
for i in data.iterrows():
    if (data["month"].item()==month) & (data["day"].item()==day):
        name = data["name"].item()
        email = data["email"].item()

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter = random.choice(os.listdir("letter_templates"))
        with open(f"letter_templates/{letter}","r") as file:
            letter_text= "".join( file.readlines()).replace("[NAME]", name)

        email_from = "jessybriston33@gmail.com"
        password = "rvgcwcmzdphhpfih"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email_from, password=password)
            connection.sendmail(
                from_addr=email_from,
                to_addrs="lion1987.fm@gmail.com",
                msg=f"Subject:Hello\n\n{letter_text}"
            )










# 4. Send the letter generated in step 3 to that person's email address.




