import RPi.GPIO as GPIO
#import smbus
import time

GPIO.setmode(GPIO.BCM)

TRIGGER = 18
ECHO = 23
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
if __name__ == '__main__':
	try:
        	while True:
            		dist = distance()
            		print ("Measured Distance = %.1f cm" % dist)
            		time.sleep(1)
 
        	# Reset by pressing CTRL + C
    	except KeyboardInterrupt:
        	print("Measurement stopped by User")
        	GPIO.cleanup()
