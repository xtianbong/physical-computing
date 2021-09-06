import subprocess
from time import sleep

mode =raw_input("Start(press enter): ")
try:
	while True:
		if mode == '' or mode == 'T':
			lr = subprocess.Popen(["python", 'lr_stepper.py'])
			#sleep(60)
			#lr.terminate()

		if mode == ''or mode == 'E':
			ds = subprocess.Popen(["python", 'distance_servo.py'])
			#sleep(5)
			#ds.terminate
		sleep(30)
		#mode = 'R'
		#mode = raw_input("Press enter to continue")
except KeyboardInterrupt:
	pass

