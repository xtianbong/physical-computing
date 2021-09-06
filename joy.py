#!/usr/bin/python
# Terry Sturtevant, May 10, 2017
import RPi.GPIO as GPIO
import time
import smbus
address = 0x48
A0 = 0x40 
A1 = 0x41 
A2 = 0x42 
A3 = 0x43 
bus = smbus.SMBus(1)


GPIO.setmode(GPIO.BCM)
pins=[5,6,22]

GPIO.setup(pins,GPIO.IN)

#x=GPIO.input(5)
#y=GPIO.input(6)
#s=GPIO.input(22) #switch
start=True

try:
	while True:
		#bus.write_byte(address,A3)
    		x = bus.read_byte_data(address, 0x40+1)
		y = bus.read_byte_data(address, 0x40+2)
		s = GPIO.input(22) #switch 
		#bus.write_byte(address,A2)
		#y = bus.read_byte(address)
		print(x)
		print(y)
		print(s)
		print("-------------------------------------------------------------")
		time.sleep(0.1)

except KeyboardInterrupt:
	print("Done")
	pass

GPIO.cleanup()

