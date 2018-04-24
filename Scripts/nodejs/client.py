from socketIO_client import SocketIO, LoggingNamespace

name = "SCOOTER NOAH"
conditionAlarm = "0"
conditionLock = "0"
conditionPosition = "0"

valLatitude = "49.119309"
valLongitude = "6.175716"

def client_connect(data):
    print('client connect')
    socketIO.emit('rpi connection', { u'valAlarm': name, u'valAlarm': conditionAlarm, u'valLock': on_connect, u'valPosition': conditionPosition })

def client_postion(data):
    socketIO.emit('rpi position', { u'valLatitude': valLatitude, u'valLongitude': valLongitude })

def on_reconnect():
    print('reconnect')

socketIO = SocketIO('78.246.39.51', 5000, LoggingNamespace)

socketIO.on('return client connection', client_connect)
socketIO.on('return client position', client_postion)

socketIO.on('reconnect', on_reconnect)

socketIO.wait()