from flask import Flask
from datetime import date
import smtplib
import random

my_email = "mariayoana.marinova@gmail.com"
password = "tmahgoyljurllnao"

def send_motivational_quote(motivation_quote):
    with smtplib.SMTP("smtp.gmail.com") as connection:
    #secure connection
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="miyamarinova@gmail.com",
            msg=f"Subject: Quote of The Day\n\n{motivation_quote}"
        )


if date.today().weekday() == 3:
    quotes = open('quotes.txt').read().splitlines()
    today_quote = random.choice(quotes)
    send_motivational_quote(today_quote)



