"""
Program to test the code numbers of Colour Cards.

Code Reader Connections.

Object Sensor 1 --> Pin A5
Object Sensor 2 --> Pin A4
Object Sensor 3 --> Pin A3
"""

from Phygital_v0 import Phygital_v0 as pyro
import time


pyro.pinMode('A5','dInput')
pyro.pinMode('A4','dInput')
pyro.pinMode('A3','dInput')

pyro.init("COM8")



while True:
   
    try:
        Data1 = pyro.dRead('A5')
        Data2 = pyro.dRead('A4')
        Data3 = pyro.dRead('A3')
        
        DecimalCode = (Data3*4) + (Data2 * 2) + (Data1 *1)
        BinaryCode = str(Data3) +str(Data2)+str(Data1)
        
        print("Binary Code is: " + BinaryCode)
        print("Decimal code is: "+ str(DecimalCode))
        print("")
        time.sleep(1)
  
         
            
       
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
        
print("Closing")
        
    

