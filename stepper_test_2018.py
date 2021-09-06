#!/usr/bin/python
# Terry Sturtevant, May 10, 2017
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
stepper_pins=[5,6,13,19]

GPIO.setup(stepper_pins,GPIO.OUT)

stepper_sequence=[]
stepper_sequence.append([GPIO.HIGH, GPIO.LOW, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.HIGH, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.HIGH,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.LOW,GPIO.HIGH])

n = 0
angle = input("Angle in degrees:")
a = (angle/180.0)*255
try:
	while n < a:
                n = n + 1
		current_angle = (n/255.0)*180
#		for row in reversed (stepper_sequence):
		for row in stepper_sequence:
			GPIO.output(stepper_pins,row)
			time.sleep(0.005)
                print(current_angle)
	print("Reversing")
        i = 0
        while i < a:
               i = i + 1
	       current_angle = (i/255.0)*180
               for row in reversed (stepper_sequence):
#               for row in stepper_sequence:
                       GPIO.output(stepper_pins,row)
                       time.sleep(0.005)
               #print(current_angle)

except KeyboardInterrupt:
	pass

GPIO.cleanup()

