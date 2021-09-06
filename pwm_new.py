import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

p = GPIO.PWM(18, 60)  # channel=12 frequency=60Hz
q = GPIO.PWM(13, 60)  # channel=32 frequency=60Hz
p.start(50)
q.start(50)
time.sleep(5)
try:
    while True:
            p.ChangeDutyCycle(0)
            q.ChangeDutyCycle(100)
            time.sleep(10)
            p.ChangeDutyCycle(100)
            q.ChangeDutyCycle(0)
            time.sleep(10)
except KeyboardInterrupt:
    pass
p.stop()
p.stop()
GPIO.cleanup()

