#import RPi.GPIO as GPIO
#from time import sleep
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(03, GPIO.OUT)
#pwm=GPIO.PWM(03, 50)
#pwm=GPIO.PWM(03, 50)
#pwm.start(0)
#def SetAngle(angle):
#	duty = angle / 18 + 2
#	GPIO.output(03, True)
#	pwm.ChangeDutyCycle(duty)
#	sleep(1)
#	GPIO.output(03, False)
#	pwm.ChangeDutyCycle(0)
#SetAngle(90) 
#SetAngle(180)
#SetAngle(90)
#SetAngle(5)
#pwm.stop()
#GPIO.cleanup()
import RPi.GPIO as GPIO  
from time import sleep   
GPIO.setmode(GPIO.BOARD) 

# Set up pin 11 for PWM
GPIO.setup(11,GPIO.OUT)  
p = GPIO.PWM(11, 50)     
p.start(0)               

# Move the servo back and forth
p.ChangeDutyCycle(3)     
sleep(1)                 
p.ChangeDutyCycle(12)    
sleep(1)

# Clean up everything
p.stop()                 
GPIO.cleanup()           
