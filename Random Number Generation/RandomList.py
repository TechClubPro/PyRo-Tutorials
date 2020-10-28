"""Program to use the Random Library"""

import random as rd



userinput='y'

while userinput=='y':
    
    userinput=input("Do you want to generate new random number? y/n")
    
    #Generate 5 random numbers between 0 and 10
    randomNumList = rd.sample(range(0,10),3)
    print(randomNumList)