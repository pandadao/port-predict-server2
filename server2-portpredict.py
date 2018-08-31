# -*- coding: utf-8 -*-

import socket
import threading
import os
import sys, struct

#global variable
#variable for client unique number, identifying the device information
V_DeviceIdentify = 0

#IP value to binary
def addr2bytes(addr):
    host, port = addr
    try:
        host = socket.gethostbyname(host)
    except (socket.gaierror, socket.error):
        raise ValueError("invalid host")

    try:
        port = str(port)
    except:
        ValueError("invalid port")

    return str(host), port


def main():
    HOST = "0.0.0.0"
    PORT = 30344

    #socket service Listen
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    while True:
        (csock, adr) = s.accept()
        #print "Client Info: ", csock, adr
        port1_get_from_server1, public_IP_get_from_server1 = csock.recv(1024).split(" ")
        print "main: " + port1_get_from_server1 + " " + public_IP_get_from_server1
        dhost, dport = addr2bytes(adr)
        if not dhost:
            pass
        else:
            print "The Client IP is " + dhost + " and port is " + dport
            send_msg_to_client = dhost + "," + port1_get_from_server1 + "," + dport
#            csock.send(dhost + " " + dport + " the port get from server 1:" + port1_get_from_server1)
            csock.send(send_msg_to_client)
        csock.close()

if __name__ == "__main__":
    main()
