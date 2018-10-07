'''
Created on 2018
@author: HSong
'''

from random import uniform
from labs.module02 import SmtpClientConnector
from labs.common import SensorData
from time import sleep

class TempSensorEmulator():

#Initialization of each parameters
    lowVal     = 0
    highVal    = 0
    cruTemp    = 0
    alertDiff  = 0
    enableEmulator = False
    isPrevTempSet  = False

#Connecting to SMTP services
    connector = SmtpClientConnector.SmtpClientConnector()

#Get the sensor data
    sensordata = SensorData.SensorData()

#Get the value of parameters from the App
    def __init__(self,lowVal,highVal,curTemp,enableEmulator):
        self.lowVal = lowVal
        self.highVal = highVal
        self.curTemp = curTemp
        self.enableEmulator = enableEmulator

#Generate the Information that will be delivered 
    def run(self):
        while True:
            if self.enableEmulator:
                self.curTemp = uniform(float(self.lowVal), float(self.highVal))
                self.sensordata.addValue(self.curTemp)
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