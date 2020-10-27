"""Program to use the Random Library"""

import random as rd



userinput='y'

while userinput=='y':
    userinput=input("Do you want to generate new random number? y/n")
    
    num=rd.randint(100,185)

    print(num)