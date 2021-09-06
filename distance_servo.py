import RPi.GPIO as GPIO
import time

control = [5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]

servo = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)

TRIGGER = 18
ECHO = 24
GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def distance():
	GPIO.output(TRIGGER,True)
	time.sleep(0.00001)
	GPIO.output(TRIGGER, False)

	StartTime = time.time()
	StopTime = time.time()

	while GPIO.input(ECHO) == 0:
        	StartTime = time.time()

	while GPIO.input(ECHO) == 1:
        	StopTime = time.time()

	TimeElapsed = StopTime - StartTime

	distance = (TimeElapsed * 34300) / 2
 
        return distance	

p=GPIO.PWM(servo,50)# 50hz frequency

p.start(2.5)# starting duty cycle ( it set the servo to 0 degree )

v_control=7.5
try:
    while True:
        dist = distance()
        if dist > 10:
            while v_control < 10:
                p.ChangeDutyCycle(v_control)
                v_control+=0.5
                time.sleep(0.03)
                #print x
        else:
            while v_control > 0:
                p.ChangeDutyCycle(v_control)
                v_control-=0.5
                time.sleep(0.03)
           
           
            print ("Distance = %.1f cm" % dist)
            time.sleep(0.5)
        
           
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
