import smbus
import time
address = 0x48
A0 = 0x40 
A1 = 0x41 
A2 = 0x42 
A3 = 0x43 
bus = smbus.SMBus(1)
while True:
    bus.write_byte(address,A1)#0-potentiometer, 1-photoresistor,2-thermistor
    value = bus.read_byte(address)
    print(value)
    time.sleep(0.1)
