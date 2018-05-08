#this code blinks 4 leds accordingly
#with the four leds connected to board pins 31,33,35,37
import RPi.GPIO as IO
import time


for i in range(100):

    IO.setmode(IO.BOARD)
    IO.setup(31,IO.OUT)
    IO.output(31,1)         #this blinks pin board no 31
    time.sleep(0.1)
    IO.cleanup()		
    time.sleep(0.1)

    IO.setmode(IO.BOARD)
    IO.setup(33,IO.OUT)
    IO.output(33,1)         #this blinks pin board no 33
    time.sleep(0.1)
    IO.cleanup()		
    time.sleep(0.1)

    IO.setmode(IO.BOARD)
    IO.setup(35,IO.OUT)
    IO.output(35,1)         #this blinks pin board no 35
    time.sleep(0.1)
    IO.cleanup()		
    time.sleep(0.1)

    IO.setmode(IO.BOARD)
    IO.setup(37,IO.OUT)
    IO.output(37,1)         #this blinks pin board no 37
    time.sleep(0.1)
    IO.cleanup()		
    time.sleep(0.1)
