from socketio_client.manager import Manager

import gevent
from gevent import monkey;
monkey.patch_socket()

io = Manager('localhost', 5000)
chat = io.socket('/')

@chat.on_connect()
def chat_connect():
    chat.emit("Hello")

@chat.on('rpi connection')
def chat_welcome():
    chat.emit({ valAlarm: "etst", valLock: "test", valPosition: "test" })

io.connect()
gevent.wait()