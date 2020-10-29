"""
Program to Read the State of Object Sensor 
and Display it on Console.
"""

from Phygital_v0 import Phygital_v0 as pyro


# Pin Initialization
pyro.pinMode('A5','dInput')
#Communication Init
pyro.init("COM8")

while True:
    try:
           
        #Read State of Sensor
        data=pyro.dRead('A5')
        print("Sensor State: "+ str(data))
        
        if data==0:# Object Sensed
            print("Object Sensed")
            
        else:
            print("No Object")
        
        
        
    
    
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
print("Closing")
    