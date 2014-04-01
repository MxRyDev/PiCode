# Playing  with a 7 Segment Display
# Maxwell Hayes
# 3/30/2014

import RPi.GPIO  as gpio
from time import sleep
from threading import Thread

#:::::::lists for pin formations (in BCM #'s)::::::::::

# bcm pins  for LED's  (to be set as outputs)
all  = [2,3,4,17,27,22,10]

#Numbers:
zero = [2,3,4,27,22,10]
one  = [2,10]
two  = [3,2,17,27,22]
three= [3,2,17,10,22]
four = [2,4,17,10]
five = [3,4,17,10,22]
six  = [3,4,17,10,22,27]
seven= [3,2,10]
eight= [2,3,4,17,10,22,27]
nine = [2,3,4,17,10]

# master numbers list:
numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

# init empty list for message to be displayed
message_out = []


# GPIO setup:::::::::::::::::::

# set gpio pin mode to BCM (not board!!!)
gpio.setmode(gpio.BCM)

# Init all LED gpio pins as outputs
for i in all:
        gpio.setup(i, gpio.OUT)

# Init  pin 9 for Button input:
gpio.setup(9,  gpio.IN, pull_up_down = gpio.PUD_DOWN)


# Basic Functions::::::::::::::
def wait_for_button():
        while True:
                pressed = gpio.input(9)
                if pressed: break
        while True:
                pressed = gpio.input(9)
                if  not pressed: break

def clear():
        for i in all:
                gpio.output(i, 0)

def count_up(speed = 1):
        for each_number in numbers:
                wait_for_button()
                clear()
                for each_pin in each_number:
                        gpio.output(each_pin, 1)
                sleep(.1)
                #clear()

def count_down(speed = 1):
        numbers.reverse()
        count_up(speed)
        numbers.reverse()

# :::::::::CODE GOES HERE:::::::::          

clear()
sleep(1.5)
print('Running...')
try:
        while True:
                count_up()

# :::::::::::::::::::::::::::::::::
                
except KeyboardInterrupt:
        gpio.cleanup()
        print('GPIO PINS HAVE BEEN RESET...')
        print('//The  Program is  not still running,  you want to quit')
        quit()
        


