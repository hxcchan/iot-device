'''
Created on 2018

@author: HSong
'''

from time import sleep
from labs.module01 import SystemPerformanceAdaptor

sysPerfAdaptor = SystemPerformanceAdaptor.SystemPerformanceAdaptor()
sysPerfAdaptor.daemon = True
print("Starting system performance app daemon thread...")

sysPerfAdaptor.enableAdaptor = True
sysPerfAdaptor.start()

while (True):
    sleep(5)
    pass
