# main.py -- put your code here!

import pyb
from pyb import Pin
from pyb import Switch
# from encoder import Encoder

##INITIALIZING EXTERNAL COMPONENTS
#initialize pin X2 for FB
P_in = Pin('X2', Pin.IN, Pin.PULL_UP)

#intialize output for FB lights pin 
pinrled = Pin('X4', Pin.OUT_PP)
pingled = Pin('X6', Pin.OUT_PP)


## INITIALIZING BOARD COMPONENTS
#intialize timer 2 (for front button)
micros = pyb.Timer(2, prescaler=83, period=0x3fffffff)

#initialize switch 'USR'
sw = Switch()

## INTIALIZING VARIABLES
#assign variable equal to 3 seconds (required depression time for FB) at 1MHz
t_min = 3000000


while True:
    if P_in.value() == 1:
        count = micros.counter(0)
        pyb.LED(2).off()
        pyb.LED(3).off()
        pinrled.high()
        pingled.low()
    elif P_in.value() == 0:
        count = micros.counter()
        while P_in.value() == 0 and count >= t_min:
            pinrled.low()
            pyb.LED(2).on()
            pingled.high()
            if sw.value() == True:
                pyb.LED(3).on()
            else: 
                pyb.LED(3).off()
    else: 
        pyb.LED(2).off()
        pyb.LED(3).off()
        pinrled.high()
        pingled.low()

