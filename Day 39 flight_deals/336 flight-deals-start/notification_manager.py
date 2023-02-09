import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_email(self, text, emails):
        letter = f"""\
            <html>
              <body>
                <p>Hi<br>
                   Here is your cheap tickets<br>
                   {text}
                </p>
              </body>
            </html>
            """

        for i in emails:
            email_from = ""
            password = ""
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=email_from, password=password)
                connection.sendmail(
                    from_addr=email_from,
                    to_addrs=i,
                    msg=f"Subject: Cheap tickets\nFrom: {email_from}\nTo: {i}\nContent-Type: text/html\n\n{letter}"
                )
