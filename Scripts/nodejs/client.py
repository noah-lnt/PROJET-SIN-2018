from socketIO_client import SocketIO, LoggingNamespace

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

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
def client_unlock(data):
	global conditionLock
	conditionLock = "0"
	socketIO.emit('rpi connection', { u'valName': name, u'valAlarm': conditionAlarm, u'valLock': conditionLock, u'valPosition': conditionPosition })


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