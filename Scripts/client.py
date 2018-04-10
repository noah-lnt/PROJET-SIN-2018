#!/usr/bin/env python
# coding: utf-8

import socket

hote = "80.12.43.225"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print "Connection on {}".format(port)

socket.send(u"Hey my name is Olivier!")

print "Close"
socket.close()