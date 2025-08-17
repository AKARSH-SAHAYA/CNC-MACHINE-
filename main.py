from  complete_controller import * 
# from bresenham_line import bresenham_line
# from parametric_circle import generate_arc

current_cordinates=[0,0,0]

gcommand=None

control_commands=['G00','G01','GO2','G03','G1','G0','G2','G3','G1']

parsed_command=[]

path ='g_code.txt'
file= open(path,'r')
for line in file:
    cmd=line.strip().split()
    print(cmd)
    for item in cmd:
     command = { 'gcommand': None, 'X': None, 'Y': None, 'Z': None, 'I': None, 'J': None}
     if item.upper() in control_commands:
                    command['gcommand'] = item.upper()
                # Process parameters (X, Y, Z, I, J)
     elif len(item) > 1 and item[0].upper() in ['X', 'Y', 'Z', 'I', 'J']:
       param = item[0].upper()  # Parameter type (e.g., 'X')
       value = item[1:]  # Value part (e.g., '10.5')             
       command[param] = float(value)  # Convert to float 
       parsed_command.append(command)            
      
    if parsed_command[gcommand]=='G00'or 'G0':
          control_cnc(parsed_command['X']-current_cordinates[0],parsed_command['Y'-current_cordinates[1]],parsed_command['Z']-current_cordinates[2])



file.close()
