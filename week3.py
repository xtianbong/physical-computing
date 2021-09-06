import subprocess
from time import sleep

mode =raw_input("E or T: ")
try:
	while True:
		if mode=='E':
			ds = subprocess.Popen(["python", 'distance_servo.py'])
			sleep(5)
			ds.terminate()

		if mode=='T':
			lr = subprocess.Popen(["python", 'lr_stepper.py'])
			sleep(5)
			lr.terminate
		mode = 'R'
		mode = raw_input("E or T:")
except KeyboardInterrupt:
	pass

