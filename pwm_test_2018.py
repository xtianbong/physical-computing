import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
p.start(50)
time.sleep(1)
angle = input("Angle in degrees:")
duty_cycle = (angle/180.0)*12
n=0
try:
    while n <=  duty_cycle:
            p.ChangeDutyCycle(n)
	    n=n+0.1
            time.sleep(0.1)
	    if n>duty_cycle:
	    	n=0
	    print(n)
    
except KeyboardInterrupt:
    i=3
    while i > 0:
	    p.ChangeDutyCycle(i)
	    time.sleep(0.05)
            i=i-0.2
    pass
p.stop()
GPIO.cleanup()
