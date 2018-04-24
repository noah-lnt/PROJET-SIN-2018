from socketIO_client import SocketIO, LoggingNamespace

name = "SCOOTER NOAH"
conditionAlarm = "0"
conditionLock = "0"
conditionPosition = "0"

valLatitude = "49.119309"
valLongitude = "6.175716"


def client_connect(data):
    print('client connect')
    socketIO.emit('rpi connection', { u'valName': name, u'valAlarm': conditionAlarm, u'valLock': conditionLock, u'valPosition': conditionPosition })

def client_postion(data):
    socketIO.emit('rpi position', { u'valLatitude': valLatitude, u'valLongitude': valLongitude })

def client_startAlarm(data):
	conditionAlarm = "1"
	socketIO.emit('rpi connection', { u'valName': name, u'valAlarm': conditionAlarm, u'valLock': conditionLock, u'valPosition': conditionPosition })
def client_stopAlarm(data):
	conditionAlarm = "0"
	socketIO.emit('rpi connection', { u'valName': name, u'valAlarm': conditionAlarm, u'valLock': conditionLock, u'valPosition': conditionPosition })

def client_lock(data):
	conditionLock = "1"
	socketIO.emit('rpi connection', { u'valName': name, u'valAlarm': conditionAlarm, u'valLock': conditionLock, u'valPosition': conditionPosition })
def client_unlock(data):
	conditionLock = "0"
	socketIO.emit('rpi connection', { u'valName': name, u'valAlarm': conditionAlarm, u'valLock': conditionLock, u'valPosition': conditionPosition })


def on_reconnect():
    print('reconnect')

socketIO = SocketIO('78.246.39.51', 5000, LoggingNamespace)

socketIO.on('return client connection', client_connect)

socketIO.on('return client position', client_postion)

socketIO.on('return client start alarm', client_startAlarm)
socketIO.on('return client stop alarm', client_stopAlarm)

socketIO.on('return client lock', client_lock)
socketIO.on('return client unlock', client_unlock)

socketIO.on('return client position', client_postion)

socketIO.on('reconnect', on_reconnect)

socketIO.wait()