from machine import Pin ,UART #type:ignore
import time
# LOOKING AT THE G CODE FILES I CAN SEE 
# FIRST COMMAND IS G COMMAND 
# FOWOLLED BY X ,Y,Z CO ORDINATES  AND THEN FOLLWED CRICLE INTERPOLATION OR F FEED RATE COMMAND 
# G00,G01,G02,G03,G21 TO TELL  THE CNC ALL THE CO_ORDINATES ARE IN MILLIMETERS IN OUR CASE ALL THE DRAWING MUST BE 


def gcode():
    pass

def co_ordinates():
    pass

def circle_cw():
    pass
def circle_acw():
     pass
def line_interpolation():
    pass

def move():  # for fg code G0  to move the machine to a particular co-ordinate without action 
    pass 










com = UART(1, baudrate=115200, tx=22, rx=23)

while True:
    com.write(b"ok\n")
  
    if com.any():
        p = com.readline()
        if p:
           commands=p.split()
           token=commands[0]
           if(token=='G0'):
               move()
           elif(token=='G01'):
              line_interpolation()
           elif(token=='G02'):
              circle_cw()
           elif(token=='G03'):
               circle_acw()
           else :
               pass    
                   
                  













