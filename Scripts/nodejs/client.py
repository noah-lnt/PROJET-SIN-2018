from socketIO_client import SocketIO, LoggingNamespace

def on_connect(data):
    print('connect')
    socketIO.emit('rpi connection', { u'valAlarm': "test", u'valLock': "test", u'valPosition': "test" })

def on_disconnect():
    print('disconnect')

def on_reconnect():
    print('reconnect')

def on_aaa_response(*args):
    print('on_aaa_response', args)

socketIO = SocketIO('78.246.39.51', 5000, LoggingNamespace)

socketIO.on('return client connection', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)

socketIO.wait()