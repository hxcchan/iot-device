'''
Created on 2018

@author: HSong
'''
import os
from datetime import datetime

class SensorData():
        timeStamp = None
        name = 'Not set'
        curValue = 0
        avgValue = 0
        minValue = 0
        maxValue = 0
        totValue = 0
        sampleCount = 0
        
        def __init__(self):
            self.timeStamp = str(datetime.now())
            
        def addValue(self, newVal):
            self.sampleCount += 1
            self.timeStamp = str(datetime.now())
            self.curValue = newVal
            self.totValue += newVal
            if (self.curValue < self.minValue):
                self.minValue = self.curValue
            if (self.curValue > self.maxValue):
                self.maxValue = self.curValue
            if (self.totValue != 0 and self.sampleCount > 0):
                self.avgValue = self.totValue / self.sampleCount
                
        def getAvgValue(self):
            return self.avgValue
        
        def getMaxValue(self):
            return self.maxValue
        
        def getMinValue(self):
            return self.minValue
        
        def getValue(self):
            return self.curValue

        def setName(self, name):
            self.name = name

# Reading system information              
        def __str__(self):
            customStr = \
                str(self.name + ':' + \
                os.linesep + '\tTime: ' + self.timeStamp + \
                os.linesep + '\tCurrent: ' + str(self.curValue) + \
                os.linesep + '\tAverage: ' + str(self.avgValue) + \
                os.linesep + '\tSamples: ' + str(self.sampleCount) + \
                os.linesep + '\tMin: ' + str(self.minValue) + \
                os.linesep + '\tMax: ' + str(self.maxValue))
            return customStr
