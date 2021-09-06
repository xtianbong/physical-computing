import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.IN)


try: 
	while True:
		GPIO.output(12,False)
		if (GPIO.input(11)== False): 
			print ("LO")
		else:
			print ("HI")
		time.sleep(10)
		GPIO.output(12,True)
		if (GPIO.input(11)== True): 
			print ("HI")
		else:
			print ("LO")
		time.sleep(10)
except KeyboardInterrupt:
	pass

finally:
	GPIO.cleanup()

