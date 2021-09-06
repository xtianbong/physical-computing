import RPi.GPIO as GPIO
import smbus
import time
 
address = 0x48
bus = smbus.SMBus(1)
cmd  = 0x40 # control byte to communicate with the PCF8591
Z_Pin = 22  # GPIO Pin connected to Joystick's SW Pin
 
def analogRead(chn): # read the digital quantity representation or AD Conversion value from each of the A0 to A3 pins
	value = bus.read_byte_data(address, cmd+chn)
	return value
 
def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Z_Pin, GPIO.IN, GPIO.PUD_UP)
     
def loop():
	while True:
        	valZ= GPIO.input(Z_Pin)
        	valVRY = analogRead(0)
        	valVRX = analogRead(1)
        	print('VRX:', valVRX, '\nVRY:', valVRY, '\nZ:', valZ)
        	time.sleep(0.01)    # set a delay between reads
         
def destroy():
	bus.close()
	GPIO.cleanup()
     
def main():
    	print("Initializing Resources")
    	setup()
    	try:
        	loop()
    	except KeyboardInterrupt:   # close the script by pressing CTRL + C
        	destroy()
if __name__ == "__main__":
	main()
