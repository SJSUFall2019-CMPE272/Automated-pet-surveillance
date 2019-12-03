import smtplib
gmail_user = 'Pawpatrolserviceshelpdesk@gmail.com'
gmail_password = 'Cmpe272Ranjan'

sent_from = gmail_user
to = ['atharvamunshi19@gmail.com']
subject = 'OMG Super Important Message'
# body = 'Hey, what's up?\n\n- You'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, "Hellooo")
    server.close()

    print ('Email sent!')
except:
    print ('Something went wrong...')
