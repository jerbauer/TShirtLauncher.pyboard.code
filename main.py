# # # # main.py -- put your code here!


import pyb
from pyb import Pin


#initialize pin X2
P_in = Pin('X2', Pin.IN, Pin.PULL_UP)


#intialize timer 2 (for front button)
micros = pyb.Timer(2, prescaler=83, period=0x3fffffff)

#assign variable equal to 3 seconds (required depression time for FB) at 1MHz
t_min = 3000000


while True:
    if P_in.value() == 1:
        count = micros.counter(0)
        pyb.LED(3).off()
    elif P_in.value() == 0:
        count = micros.counter()
        while P_in.value() == 0 and count >= t_min:
        #count = micros.counter()
            pyb.LED(3).on()
    else: 
        pyb.LED(3).off()





# import pyb
# from pyb import Pin

# #initialize pin X2
# P_in = Pin('X2', Pin.IN, Pin.PULL_UP)


# #intialize timer 2 (for front button)
# micros = pyb.Timer(2, prescaler=83, period=0x3fffffff)

# #assign variable equal to 3 seconds (required depression time for FB) at 1MHz
# t_min = 3000000

# # while True:
# if P_in.value() == 0:
#     micros.counter(0)
#     while micros > t_min:
#         micros.callback(lambda t: pyb.LED(3).on())
# #     elif
# #     micros.callback(lambda t: pyb.LED(3).off())
# # elif
# #     pyb.LED(3).off()
