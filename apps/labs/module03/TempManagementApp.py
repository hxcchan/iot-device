'''
Created on 2018

@author: HSong
'''

#This is a module that will pass parameters to the Emulator and start running them.
from time import sleep
from labs.module03 import TempSensorAdaptor
from labs.module03 import TempActuatorEmulator

sysPerfAdaptor = TempSensorAdaptor.TempSensorAdaptor(5,70,35,True)
sysActuatorProxy = TempActuatorEmulator.TempActuatorEmulator()

sysPerfAdaptor.enableAdaptor = True
sysPerfAdaptor.run()


sysActuatorProxy.enableEmulator = True
sysActuatorProxy.start()

while (True):
    sleep(10)
    pass
