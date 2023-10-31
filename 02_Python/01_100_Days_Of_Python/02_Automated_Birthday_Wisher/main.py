import smtplib

my_email = "vivalaed@gmail.com"
my_password = "M3t@llic@1987"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="edgardo.panza@gmail.com", msg= "This is just a test")
connection.close()

