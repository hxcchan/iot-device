'''
Created on 2018

@author: HSong
'''

#This is a module that will pass parameters to the Emulator and start running the app.

from labs.module02 import TempSensorEmulator

startRunning = TempSensorEmulator.TempSensorEmulator(5, 70, 35, True)

startRunning.run()