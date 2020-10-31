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

count=0
while True:
    try:
           
        #Read State of Sensor
        data=pyro.dRead('A5')
        
        if data==0:# Object Sensed
            while data==0:
                data=pyro.dRead('A5')
            
            count=count+1
            print("Object Sense Count:: "+str(count))
            
       
        
        
    
    
    except:
        if KeyboardInterrupt:
            pyro.close()
            break
print("Closing")
    
