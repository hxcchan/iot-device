'''
Created on 2018
'''
from labs.common import ConfigUtil
from labs.common.ActuatorData import ActuatorData
from time import sleep
import threading
from sense_hat import SenseHat


class TempActuatorEmulator(threading.Thread):
    '''
    classdocs
    '''

    enableEmulator = False
    actuatorData = ActuatorData
    senseHat = SenseHat()
    rateInSec = 5

    
    def __init__(self):
        '''
        Constructor
        '''
        super(TempActuatorEmulator, self).__init__()
        self.config = ConfigUtil.ConfigUtil('../../../data/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        
    def processMessage(self, data):
        v = ActuatorData()

        priorValue = v. ActuatorData.getValue()
        p = SenseHat.get_temperature(1)
       
        value = p(self) - priorValue
            
        if value > 0:
            msg = 'The temperature should be lower than before.'
            self.senseHat.show_message(msg)
        
        if value < 0:
            msg = 'The temperature should be higher than before.'
            self.senseHat.show_message(msg)
        
        if value == 0:
            pass
        
        self.actuatorData.updateData(p)
        
    def run(self):
        while (True):
            if self.enableEmulator:
                self.processMessage(self.data_rcv)
            sleep(self.rateInSec)
            