import os
import RPi.GPIO as GPIO
import time
import wiringpi

from flask import Flask
import smtplib

def mailSend():
    
    gmail_user = 'pawpatrolserviceshelpdesk@gmail.com'
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

        return ('Email sent!')
    except:
        return ('Something went wrong...')

#def handlingData():
#    emailId = request.form['email']    

def servo():
    try:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(07,GPIO.OUT)
        pwm = GPIO.PWM(07,50)
        pwm.start(7)
        for pulse in range(50, 140, 1):
            DC = 1./18.*(pulse)
            pwm.ChangeDutyCycle(DC)
            time.sleep(.01)
    
        for pulse in range(180, 70, -1):
            DC = 1./18.*(pulse)
            pwm.ChangeDutyCycle(DC)
            time.sleep(0.025)
    except:
        return ('Something went wromg')
    



app = Flask(__name__)


@app.route("/notify")
def xmas():    
    mailSend()
    

#@app.route("/handleData")
#def xmas():    
#    handlingData()

@app.route("/servo")
def move():
    servo()
    

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=82, debug=True)

