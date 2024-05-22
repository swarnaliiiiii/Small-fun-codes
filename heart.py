import math 
from turtle import *

def unitFirst(x):
    return 15*math.sin(x)**3
def unitSecond(x):
    return 12*math.cos(x)-5*\
            math.cos(2*x)-2*\
            math.cos(3*x)-\
            math.cos(4*x)
speed(1000)
bgcolor("black")
for i in range(6000):
    goto(unitFirst(i)*20,unitSecond(i)*20)
    for j in range(5):
        color("#FC8EAC")
    goto(0,0)
done()
        