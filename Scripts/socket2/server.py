#!/usr/bin/env python
# coding: utf-8 

import socket
import threading
import time

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 
   
        print("Connection de %s %s" % (self.ip, self.port, ))
        try:
            r = self.clientsocket.recv(2048)
            print(r.decode())
            global command
            command = "connected"
            self.clientsocket.send(command.encode()
                )

            r = self.clientsocket.recv(2048)
            print(r.decode())
            command = "two"
            self.clientsocket.send(command.encode()
                )
        except:
            print("Client déconnecté...")

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",1111))

while True:
    tcpsock.listen(10)
    print( "En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()

    try:
        print(command)
    except:
        print("no command")
    time.sleep(5)

