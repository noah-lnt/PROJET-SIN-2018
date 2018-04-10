import serial
import time 

phone = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=1.0)

phone.write('AT+CPIN=2012\r\n')
result=phone.read(100)
print result

phone.write('AT+CMGF=1\r\n')
result=phone.read(100)
print result

phone.write('AT+CMGS="+33623761142"\r\n')
result=phone.read(100)
print result