# -*- coding: utf-8 -*-

'''
This script is to identify the device has authentication or not, and change information with database.
If the connection request is a new mac address, this script will save the device's information about mac address, new ID and random password to database.
And return the device ID and password to the device.
'''

import socket
import random
import thread 


'''
generate a random password for device, the format is english and number mixed.

def Random_value(string_length = 10):
    random = str(uuid.uuid4())
    random = random.replace("-", "")
    return random[0:string_length]

print(Random_value(6))
'''

def Random_value(string_length = 10):
    random = str(uuid.uuid4())
    random = random.replace("-", "")
    return random[0:string_length]



def main():


if __name__ == "__main__":
    main()
