#!/usr/bin/env python
# coding: utf-8 

import socket
import threading

from colorama import init
from colorama import Fore, Back, Style
init()

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))
       

    def run(self): 

        global clients1
        global clients2
   
        print("Connection de %s %s" % (self.ip, self.port, ))

        testa = 0

        while True:
            r = self.clientsocket.recv(2048)
            dateReceive = r.decode("utf-8")

            print(Fore.RED + dateReceive)

            if(r.decode("utf-8") == "raspberry" and testa == 0):
                clients1 = clientsocket
                print(Fore.YELLOW + "add raspberry")
                print(Style.RESET_ALL)
                testa = 1

            elif(r.decode("utf-8") == "client"  and testa == 0):
                clients2 = clientsocket
                print(Fore.GREEN + "add client")
                print(Style.RESET_ALL)
                testa = 1

            elif "raspberry" in r.decode("utf-8"):
                print(Fore.YELLOW + "message raspberry")
                print(Style.RESET_ALL)
                sendData = dateReceive.split("_")[1]
                clients2.sendall(sendData.encode())

            elif "client" in r.decode("utf-8"):
                print(Fore.GREEN +"message client")
                print(Style.RESET_ALL)
                sendData = dateReceive.split("_")[1]
                clients1.sendall(sendData.encode())

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",1111))

while True:
    tcpsock.listen(10)
    print( "En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()