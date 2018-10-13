'''
Created on 2018

@author: HSong
'''

#This is a module that will pass parameters to the Emulator and start running the app.
import sys
sys.path.append('/home/pi/workspace/iot-device/apps')

from labs.module04 import I2CSenseHatAdaptor
from time import sleep

senseHatAdaptor = I2CSenseHatAdaptor.I2CSenseHatAdaptor()
senseHatAdaptor.daemon = True
print("Starting system performance app daemon thread...")

senseHatAdaptor.enableEmulator = True
senseHatAdaptor.start()

while (True):
    sleep(5)
    pass

