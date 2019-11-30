import smtplib
gmail_user = ''
gmail_password = ''

sent_from = gmail_user
to = ['']
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
