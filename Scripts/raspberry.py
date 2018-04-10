#!/usr/bin/env python
# coding: utf-8

import socket

hote = "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print "Connection on {}".format(port)

socket.send(u"Hey my name is Olivier!")

print 'Server is now listening on port 9900!'
client, addr = sock.accept() 
print client
print 'Waiting for data...'
data = client.recv(4096) 

print "Close"
socket.close()