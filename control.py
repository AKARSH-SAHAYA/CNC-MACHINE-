from machine import Pin   #type:ignore
import time 
import math
# first i will make a function to take input in mm  to move the stepper motor using the caliberation logic 
# 1 step = 0.01mm

# all the 4 coils of stepper motor A,B,C,D
a=Pin(19,Pin.OUT)  
b=Pin(21,Pin.OUT)
c=Pin(22,Pin.OUT)
d=Pin(23,Pin.OUT)


half_step_sequence =[
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]
def movement(half_step_sequence):
    a.value(half_step_sequence[0])
    b.value(half_step_sequence[1])
    c.value(half_step_sequence[2])
    d.value(half_step_sequence[3])
    time.sleep(0.02)

def conversion(distance):# firstly i need to convert the distance/cordinates into steps
    steps = (distance/0.01)
    return steps

def forward(steps):
   complete = int(steps/8)
   singles = steps%8
   for i in range(complete):
     for j in  half_step_sequence:
        movement(j)

   for j in range(singles):
      movement(half_step_sequence[j])     




def reverse(steps):
    full_cycles = int(steps / 8)
    singles = steps % 8

    for _ in range(full_cycles):
        for step in reversed(half_step_sequence):
            movement(step)

    for i in range(singles):
        movement(half_step_sequence[::-1][i])
    

def cnc_move(current_position,new_position,x,y):  # the x and y here steps so before using the function use  
   if(current_position[0]<new_position[0]): # for x cordinate
      # to move forward 
      difference=new_position[0]-current_position[0] # number steps to move from the current position 
      forward(difference)
      
   elif(current_position[0]>new_position[0]): # to move back
     # to move in reverse 
    difference=abs(new_position[0]-current_position[0])  
    reverse(difference) 
   elif current_position[0]==new_position[0]:
    pass
  
  
    if(current_position[1]<new_position[1]): # for y cordinate
      # to move forward 
      difference=new_position[1]-current_position[1] # number steps to move from the current position 
      forward(difference)
      
   elif(current_position[1]>new_position[1]): # to move back
     # to move in reverse 
    difference=abs(new_position[1]-current_position[1])  
    reverse(difference) 
   


   elif current_position[1]==new_position[1]:
      pass
    



def update(current_position,new_position):
  current_position[0]=new_position[0]
  current_position[1]=new_position[1]
  

current_position=[0,0]

# add to a while for continous changes
while 1:
 cmd=input("ENTER THE CORDINATES:IN MM [X,Y]")
 new_position=[float(x)for x in cmd.split()]
 x=conversion(new_position[0]) # steps in x 
 y=conversion(new_position[1]) # steps in y 
 cnc_move(current_position=current_position,new_position=new_position,x=x,y=y)
 update(current_position=current_position,new_position=new_position)

