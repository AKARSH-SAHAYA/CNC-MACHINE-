from machine import Pin   #type: ignore
import time 


# all  the 4 coils of stepper motor A,B,C,D
a=Pin(19,Pin.OUT)  
b=Pin(21,Pin.OUT)
c=Pin(22,Pin.OUT)
d=Pin(23,Pin.OUT)


# i have noticed one thing that in full step there is less torque that why it stops working when there too much friction between due to bad print quality 


forward_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]
# to reverse use reversed(forward_sequence)  in for loop      
  

def control(forward_sequence):
    a.value(forward_sequence[0])
    b.value(forward_sequence[1])
    c.value(forward_sequence[2])
    d.value(forward_sequence[3])
    time.sleep(0.01)

while 1:
    for step in forward_sequence:
        control(step)