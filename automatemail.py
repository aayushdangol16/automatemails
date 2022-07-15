import smtplib
email = "mail@gmail.com"
password = "password"
message="testing"
server=smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)
f=open("mail.txt","r")
mails=f.read()
li=list(mails.split("\n"))
for items in li:
    server.sendmail(email,items,message)
server.close()