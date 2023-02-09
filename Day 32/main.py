import random
import smtplib
import datetime as dt

# get quote

with open("quotes.txt") as file:
    quotes= file.readlines()
    quote= random.choice(quotes)





# send imail


date_now = dt.datetime.now()


if date_now.weekday()==3:
    email = "your email"
    password = "your password"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="email",
            msg=f"Subject:Hello\n\n{quote}"
        )




