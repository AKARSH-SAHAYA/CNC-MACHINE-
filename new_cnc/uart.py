from  machine import UART  #type: ignore
import time 
com=UART( 1,baudrate=115200,tx=22 ,rx=23)
com.write("Grbl 1.1h ['$' for help]")
time.sleep(0.2)
while True: #grbl startup sequences 
    command =com.read() # reads for the bytes  of the data 
    if com =='?':
        com.write("<Idle|MPos:0.000,0.000,0.000|FS:0,0>")
    elif com == '$$' :
        com.write("$0=10")   
        com.write("$1=25")
        com.write("$2=0")
        com.write("ok")