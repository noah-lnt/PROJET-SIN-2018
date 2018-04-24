from socketIO_client import SocketIO, LoggingNamespace

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

import threading
import smbus
import math
import time

class Concur(threading.Thread):
    def __init__(self):
        self.stopped = False
        threading.Thread.__init__(self)

    def run(self):
        i = 0
        while not self.stopped:
            # Power management registers
			power_mgmt_1 = 0x6b
			power_mgmt_2 = 0x6c

			def read_byte(adr):
			    return bus.read_byte_data(address, adr)

			def read_word(adr):
			    high = bus.read_byte_data(address, adr)
			    low = bus.read_byte_data(address, adr+1)
			    val = (high << 8) + low
			    return val

			def read_word_2c(adr):
			    val = read_word(adr)
			    if (val >= 0x8000):
			        return -((65535 - val) + 1)
			    else:
			        return val

			def dist(a,b):
			    return math.sqrt((a*a)+(b*b))

			def get_y_rotation(x,y,z):
			    radians = math.atan2(x, dist(y,z))
			    return -math.degrees(radians)

			def get_x_rotation(x,y,z):
			    radians = math.atan2(y, dist(x,z))
			    return math.degrees(radians)


			bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
			address = 0x68       # This is the address value read via the i2cdetect command

			# Now wake the 6050 up as it starts in sleep mode
			bus.write_byte_data(address, power_mgmt_1, 0)

			conditionMode = False
			conditionCount = 0

			while True:
			    time.sleep(0.1)

			    gyro_xout = read_word_2c(0x43)
			    gyro_yout = read_word_2c(0x45)
			    gyro_zout = read_word_2c(0x47)

			    accel_xout = read_word_2c(0x3b)
			    accel_yout = read_word_2c(0x3d)
			    accel_zout = read_word_2c(0x3f)

			    if conditionCount >= 5:
			        GPIO.output(12, GPIO.HIGH)

			    if conditionMode == False or conditionCount >= 15:
			        print "RAZ"
			        x_base = accel_xout
			        y_base = accel_yout
			        z_base = accel_zout
			        conditionMode = True
			        conditionCount = 0

			    if x_base + 2000 <= accel_xout:
			        print "1"
			        conditionCount = conditionCount + 1

			    elif x_base - 2000 >= accel_xout:
			        print "2"
			        conditionCount = conditionCount + 1

			    elif y_base + 2000 <= accel_yout:
			        print "3"
			        conditionCount = conditionCount + 1

			    elif y_base - 2000 >= accel_yout:
			        print "4"
			        conditionCount = conditionCount + 1

			    elif z_base + 2000 <= accel_zout:
			        print "5"
			        conditionCount = conditionCount + 1

			    elif z_base - 2000 >= accel_zout:
			        print "6"
			        conditionCount = conditionCount + 1

			    time.sleep(0.5)

name = "SCOOTER NOAH"
global conditionAlarm
global conditionLock
global conditionPosition
conditionAlarm = "0"
conditionLock = "0"
conditionPosition = "0"

global valLatitude
global valLongitude
valLatitude = "49.119309"
valLongitude = "6.175716"


def client_connect(data):
    print('client connect')
    socketIO.emit('rpi connection', { u'valName': name, u'valAlarm': conditionAlarm, u'valLock': conditionLock, u'valPosition': conditionPosition })

def client_startPosition(data):
	global conditionPosition
	conditionPosition = "1"
	socketIO.emit('rpi connection', { u'valName': name, u'valAlarm': conditionAlarm, u'valLock': conditionLock, u'valPosition': conditionPosition })
	socketIO.emit('rpi position', { u'valLatitude': valLatitude, u'valLongitude': valLongitude })

def client_stopPosition(data):
	global conditionPosition
	conditionPosition = "0"
	socketIO.emit('rpi connection', { u'valName': name, u'valAlarm': conditionAlarm, u'valLock': conditionLock, u'valPosition': conditionPosition })

def client_startAlarm(data):
	global conditionAlarm
	conditionAlarm = "1"
	socketIO.emit('rpi connection', { u'valName': name, u'valAlarm': conditionAlarm, u'valLock': conditionLock, u'valPosition': conditionPosition })
	GPIO.output(12, GPIO.HIGH)
def client_stopAlarm(data):
	global conditionAlarm
	conditionAlarm = "0"
	socketIO.emit('rpi connection', { u'valName': name, u'valAlarm': conditionAlarm, u'valLock': conditionLock, u'valPosition': conditionPosition })
	GPIO.output(12, GPIO.LOW)

def client_lock(data):
	global conditionLock
	conditionLock = "1"
	socketIO.emit('rpi connection', { u'valName': name, u'valAlarm': conditionAlarm, u'valLock': conditionLock, u'valPosition': conditionPosition })
	inst.start()
def client_unlock(data):
	global conditionLock
	conditionLock = "0"
	socketIO.emit('rpi connection', { u'valName': name, u'valAlarm': conditionAlarm, u'valLock': conditionLock, u'valPosition': conditionPosition })
	inst.stop()


def on_reconnect():
    print('reconnect')

socketIO = SocketIO('78.246.39.51', 5000, LoggingNamespace)

socketIO.on('return client connection', client_connect)

socketIO.on('return client start alarm', client_startAlarm)
socketIO.on('return client stop alarm', client_stopAlarm)

socketIO.on('return client lock', client_lock)
socketIO.on('return client unlock', client_unlock)

socketIO.on('return client start position', client_startPosition)
socketIO.on('return client stop position', client_stopPosition)

socketIO.on('reconnect', on_reconnect)

socketIO.wait()