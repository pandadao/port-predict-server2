# -*- coding: utf-8 -*-

'''
This script is to identify the device has authentication or not, and change information with database.
If the connection request is a new mac address, this script will save the device's information about mac address, new ID and random password to database.
And return the device ID and password to the device.
'''

import socket
import random
import thread
import uuid
import MySQLdb


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

# Generate the password for device, it will be english and number mixed.
def Random_Password(string_length = 10):    #The string_length can change like print(Random_Password(6)), and the length will be 6
    random = str(uuid.uuid4())
    random = random.replace("-", "")
    Device_password = random[0:string_length]
    return  Device_password


'''
This part has to redesign, because the repeat probability is too high!!!!
'''
# Generate the device ID, it depends the connection client mac address value.
def Random_ID(Device_MAC, string_length = 10):
    random = str(Device_MAC)
    Device_ID = random[0:string_length]  #datatype is str
    return Device_ID

def Stored_to_DB(Device_MAC):
    db = MySQLdb.connect("localhost", "newuser", "newpassword", "IPPort_Information")
    cursor = db.cursor()
    # the command about search one data is:     SELECT * FROM `Device_relative` WHERE `mac_address` = '123'
    sql = "SELECT `mac_address` FROM `Device_relative` WHERE `mac_address` = " + Device_MAC
    cursor.execute(sql)
    result = cursor.fetchone()
    # if no match data in db, save it.
    if result == None:
        command = "INSERT INTO `Device_relative` (`mac_address`, `DeviceID`, `password`, `Register_Time`, `Public_IP`) VALUE ()"




def Information_Process(Device_MAC):
    # Check the device has registered or not.
    Stored_to_DB(Device_MAC)


    #Device_ID = Random_ID(Device_MAC, 6)
    Device_ID = Device_MAC
    Device_password = Random_Password(6)
    send_msg_to_client = Device_ID + " " + Device_password
    return send_msg_to_client



def main():
    HOST = "0.0.0.0"
    PORT = 30345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    while True:
        (csock, adr) = s.accept()

        Device_MAC = csock.recv(1024)
        print ("Device_MAC: " + Device_MAC)
        dhost, dport = addr2bytes(adr)

        if not dhost:
            pass
        else:
            send_msg_to_client = Information_Process(Device_MAC)
            csock.send(send_msg_to_client)
        csock.close()


if __name__ == "__main__":
    main()
