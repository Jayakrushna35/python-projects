import smtplib

my_email = "write your own email"
password = "emailpassword"

with smtplib.SMTP("smtp.gmail.com") as connection :
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="sender addresss",
        msg="write your message"

    )