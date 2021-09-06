import smbus
import time
address = 0x48
A0 = 0x40 #photoresistor
A1 = 0x41 #thermistor
A2 = 0x42 #external
A3 = 0x43 #potentiometer

outvalue=0
cmd =0x40

bus = smbus.SMBus(1)
while True:
    bus.write_byte_data(address,cmd,outvalue)
    outvalue += 1
    if outvalue == 256:
        outvalue =0
    print("AOUT:%3d" %outvalue)
    bus.write_byte(address,A3)
    value = bus.read_byte(address)
    #print(value)
    print("AIN:%1.3f  " %(value*3.3/255))
    time.sleep(0.5)
