from RPLCD import i2c
import RPi.GPIO as GPIO
import pygame
from pygame.locals import *
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_UP)
switch = GPIO.input(21)
pygame.init()
# constants
lcdmode = 'i2c'
cols = 20
rows = 4
charmap = 'A00'
i2c_expander = 'PCF8574'

address = 0x27 
port = 1 

# Initialise LCD and pygame
lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap,
                  cols=cols, rows=rows)

pygame.init()
text = input('Enter Text:')
lcd.write_string(text)
try:	
	while True:
		if switch==True:
			mode = input("CLEAR (C) or NEW LINE (N)")
			if mode == 'C':
				lcd.close(clear=True)
				text = input('New text:')
				#lcd.close(clear=True)
				lcd.write_string(text)
			elif mode == 'N':
				text = input('New Line:')
				lcd.crlf()
				lcd.write_string(text)
		#print(switch)
		switch = GPIO.input(21)
		sleep(0.1)
		'''
		lcd.write_string('see?')
		lcd.crlf()
		sleep(3)
		'''
			
except KeyboardInterrupt:
	#turn off the light and clear the screen
	lcd.backlight_enabled = False 
	lcd.close(clear=True)
