import subprocess
from time import sleep
try:
	print("Buttons control the stepper motor, while the servo is controlled by proximity")
	ds = subprocess.Popen(["python", 'distance_servo.py'])
	ds.wait()
	lr = subprocess.Popen(["python", 'lr_stepper.py'])
	lr.wait()
except KeyboardInterrupt:
	pass
	ds.terminate()
	lr.terminate()

