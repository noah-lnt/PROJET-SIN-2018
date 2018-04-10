#!/usr/bin/python
# Filename: text.py
import serial
ser = serial.Serial("/dev/ttyS0",115200)

W_buf_logoin = "AT+CREG?\r\n"
W_buf_phone =  "ATD18565708640;\r\n"
ser.write(W_buf_logoin)

print W_buf_logoin

ser.flushInput()
data = ""

try:
	while True:
		while ser.inWaiting() > 0:
			data += ser.read(ser.inWaiting())
		if data != "":
			print data
			if data == "OK":
				print "call phone"
				ser.write(W_buf_phone)
			data = ""
except keyboardInterrupt:
	if ser != None:
		ser.close()
		