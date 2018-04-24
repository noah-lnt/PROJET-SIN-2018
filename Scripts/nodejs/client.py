from socketIO_client import SocketIO, LoggingNamespace

with SocketIO('http://78.246.39.51', 5000, verify=False) as socketIO:
    socketIO.emit('aaa')
    socketIO.wait(seconds=1)
