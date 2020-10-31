"""
Program to Read the State of Object Sensor 
and Put On LED when Object is Sensed.
"""

from Phygital_v0 import Phygital_v0 as pyro


# Pin Initialization
pyro.pinMode('A0','dOutput')
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
            pyro.dWrite('A0',1)
            
        else:
            print("No Object")
            pyro.dWrite('A0',0)
        
        
        
    
    
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
print("Closing")
    
