# -*- coding: utf-8 -*-

'''
This script is to identify the device has authentication or not, and change information with database.
If the connection request is a new mac address, this script will save the device's information about mac address, new ID and random password to database.
And return the device ID and password to the device.
'''

import socket
import random
import thread


# Generate the password for device, it will be english and number mixed.
def Random_Password(string_length = 10):    #The string_length can change like print(Random_Password(6)), and the length will be 6
    random = str(uuid.uuid4())
    random = random.replace("-", "")
    Device_password = random[0:string_length]
    return  Device_password

# Generate the device ID, it depends the connection client mac address value.
def Random_ID(string_length = 10):
    random = str(Device_MAC)
    Device_ID = random[0:6]  #datatype is str
    return Device_ID



def main():
    HOST = "0.0.0.0"
    PORT = 30345


if __name__ == "__main__":
    main()
