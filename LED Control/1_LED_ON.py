"""
Code to Control LED State On-Off

LED connected at A0

"""

"""Library"""
from Phygital_v0 import Phygital_v0 as pyro

"""Pin Initialization"""
pyro.pinMode('A0','dOutput')

"""Init"""
pyro.init("COM8")

"""LED ON"""

while True:
    try:
        pyro.dWrite('A0',1)#LED ON
          
        
        
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
        
print("Closed the Connection!!")

"""Closing"""
