#!/usr/bin/python3

import socket

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    sock.send(msg_to_wire(message))
    response = sock.recv(1024)
    print "Received: %s" % response
    sock.close()

def msg_to_wire(msg):
    msg_len = len(msg)
    return "%04d%s" % (msg_len,msg)
