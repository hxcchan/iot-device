'''
Created on 2018
@author: HSong
'''

from random import uniform
from labs.module02 import SmtpClientConnector
from time import sleep
from sense_hat import SenseHat
import sense_hat

class TempSensorAdaptor():
  
#Initialization of each parameters
    lowVal     = 0
    highVal    = 0
    cruTemp    = 0
    alertDiff  = 5
    enableAdaptor = False
    isPrevTempSet  = False
   
#Connecting to SMTP services
    connector = SmtpClientConnector.SmtpClientConnector()

#Get the sensor data
    sensordata = sense_hat.SenseHat
    p = sensordata.get_temperature(1)

#Get the value of parameters from the App
    def __init__(self,lowVal,highVal,curTemp,enableEmulator):
        self.lowVal = lowVal
        self.highVal = highVal
        self.curTemp = curTemp
        self.enableEmulator = enableEmulator
    
 

#Generate the Information that will be delivered 
    def run(self):
        while True:
            if self.enableAdaptor:
                self.p = uniform(float(self.lowVal), float(self.highVal))
                self.addValue(self.p)
                print('\n-----------------------')
                print('This is your current condition:')
                print(' ' + str(self.sensordata))
                if self.isPrevTempSet == False:
                    self.prevTemp = self.curTemp
                    self.isPrevTempSet = True
                else:
                    if (abs(self.curTemp - self.sensordata.getAvgValue()) >= self.alertDiff):
                        print('\n Current temp exceeds average by > ' + str(self.alertDiff) + '. Triggeringalert...')
                    self.connector.publishMessage('Warning!!!', self.sensordata)
            sleep(30)