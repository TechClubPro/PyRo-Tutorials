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

while True:
    try:
       
     LEDState= input("Please Specify the state of LEDs").lower()
        
     if LEDState=="on":
         pyro.dWrite('A0', 1)
         pyro.dWrite('A1', 1)
         pyro.dWrite('A2', 1)
         pyro.dWrite('A3', 1)
         pyro.dWrite('A4', 1)
     elif LEDState=="off":  
         pyro.dWrite('A0', 0)
         pyro.dWrite('A1', 0)
         pyro.dWrite('A2', 0)
         pyro.dWrite('A3', 0)
         pyro.dWrite('A4', 0)
     else:
          pyro.close()
          break
        
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
        
print("Closed the Connection!!")

"""Closing"""
