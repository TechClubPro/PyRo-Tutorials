"""
Code to Control LED State On-Off

LED connected at A0

"""

"""Library"""
from Phygital_v0 import Phygital_v0 as pyro
import time

"""Pin Initialization"""
pyro.pinMode('A0','dOutput')
pyro.pinMode('A1','dOutput')
pyro.pinMode('A2','dOutput')
pyro.pinMode('A3','dOutput')
pyro.pinMode('A4','dOutput')

"""Init"""
pyro.init("COM15")

"""LED ON"""
LEDPins=['A0','A1','A2','A3','A4']

while True:
    try:
       
        for i in range(5):
            pyro.dWrite(LEDPins[i],1)
            time.sleep(0.5)
            pyro.dWrite(LEDPins[i],0)
            
        time.sleep(1)
#        for i in range(5):
#            pyro.dWrite(LEDPins[i],0)
#            
#        time.sleep(1)
        
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
        
print("Closed the Connection!!")

"""Closing"""
