from machine import Pin   #type: ignore
import time 


# all  the 4 coils of stepper motor A,B,C,D
a=Pin(19,Pin.OUT)  
b=Pin(21,Pin.OUT)
c=Pin(22,Pin.OUT)
d=Pin(23,Pin.OUT)


forward_sequence = [          # full step sequences 
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]
backward_sequence=[          # full step sequences 
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0]
]

def control(forward_sequence):
    a.value(forward_sequence[0])
    b.value(forward_sequence[1])
    c.value(forward_sequence[2])
    d.value(forward_sequence[3])
    time.sleep(0.01)

while 1:
    for step in forward_sequence:
        control(step)