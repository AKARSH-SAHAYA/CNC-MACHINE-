# this code is written for the caliberation of stepper motor with  linear displacement 

# so the objective of the code is to measure the linear displacement when 100 steps has occured .
# we will take 3-5 reading and then  take average of it .
# we will store the linear displacement in one step 

from machine import Pin  #type:ignore
import time

print("THE PINS USED HERE ARE 19 21 22 23  FOR A,B,C,D COILS RESPECTIVELY")
a=Pin(19,Pin.OUT)  
b=Pin(21,Pin.OUT)
c=Pin(22,Pin.OUT)
d=Pin(23,Pin.OUT)

# taking input to know how many times caliberation has to be done 
number_of_test=int(input("ENTER THE NUMBER OF TIMES CALIBERATION SHOULD RUN "))
n=number_of_test  # copy of number of test which helps to find the avg
avg = 0.0 # to store the avg distance in 100 steps in mm 
forward_sequence = [          # full step forward sequences 
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
backward_sequence=[          # full step backward  sequences 
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0]
]

def move(forward_sequence):
    a.value(forward_sequence[0])
    b.value(forward_sequence[1])
    c.value(forward_sequence[2])
    d.value(forward_sequence[3])
    time.sleep(0.01)


def reverse(forward_sequence):
    a.value(forward_sequence[0])
    b.value(forward_sequence[1])
    c.value(forward_sequence[2])
    d.value(forward_sequence[3])
    time.sleep(0.01) 


def reset():                       # to reset the system for next caliberation test 
   for test in range(25):
       for step in backward_sequence:
           reverse(step)
    
while number_of_test>0:
    for test in range(25):
       for step in forward_sequence:
           move(step)
    print("MEASURE THE DISTANCE ")
    time.sleep(10)
    reset()
    distance=float(input("ENTER THE DISTANCE IN MM"))
    avg +=distance
    number_of_test=number_of_test-1

print("THE AVERAGE DISPLACEMENT FOR 1 STEP IS ")
print((avg/n)/100)                   # if we dont divide it will giver the avg of 100 steps not one 
