#!/usr/bin/env python
# coding: utf-8

import socket
import urllib.request
import time

while True:
    try:
        file = urllib.request.urlopen('http://google.com');
        print('Connect');
        break;
    except urllib.error.URLError:
        print('No connect');
        time.sleep(3);


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 1111))

print("Connexion au serveur")
command = "raspberry connection"

s.send(command.encode())
receive_command = s.recv(2048)

if receive_command.decode() == "connected":
	print("vous êtes connecté")

s.send(command.encode())
receive_command = s.recv(2048)

if receive_command.decode() == "two":
	print("vous êtes connecté")

