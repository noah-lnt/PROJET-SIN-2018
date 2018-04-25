#!/usr/bin/python
# Filename: text.py
import serial
import time
ser = serial.Serial("/dev/ttyUSB0",115200)

W_buff = ["AT+CGNSPWR=1\r\n", "AT+CGNSSEQ=\"RMC\"\r\n", "AT+CGNSURC=1\r\n", "AT+CGNSINF\r\n"]
ser.write(W_buff[0])
time.sleep(0.5)

ser.write(W_buff[1])
time.sleep(0.5)
print ser.readline()
ser.write(W_buff[2])

while True:
    time.sleep(3)
    positionGPS = ser.readline(ser.inWaiting()).split("\n")
    
    if "+UGNSINF" in positionGPS[0]:
        splitPositionGPS = positionGPS[0].split(",")
        positionLatitude = splitPositionGPS[3]
        positionLongitude =  splitPositionGPS[4]
    else:
        print "NO"

