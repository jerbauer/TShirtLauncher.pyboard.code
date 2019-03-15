# main.py -- put your code here!


import pyb
from pyb import Pin


#initialize pin X2
P_in = Pin('X2', Pin.IN, Pin.PULL_UP)

#intialize output for FB lights pin 
pinrled = Pin('X4', Pin.OUT_PP)
pingled = Pin('X6', Pin.OUT_PP)

#intialize timer 2 (for front button)
micros = pyb.Timer(2, prescaler=83, period=0x3fffffff)

#assign variable equal to 3 seconds (required depression time for FB) at 1MHz
t_min = 3000000

# pinrled.low()
# pingled.high()
while True:
    if P_in.value() == 1:
        count = micros.counter(0)
        pyb.LED(2).off()
        pinrled.high()
        pingled.low()
    elif P_in.value() == 0:
        count = micros.counter()
        while P_in.value() == 0 and count >= t_min:
            pinrled.low()
            pyb.LED(2).on()
            pingled.high()
    else: 
        pyb.LED(2).off()
        pinrled.high()
        pingled.low()




