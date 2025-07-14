from NEW_CONTROLLER import * # Assuming control_cnc is defined here
# from bresenham_line import bresenham_line
# from parametric_circle import generate_arc

# Initialize current coordinates
current_coordinates = [0,0]  # we only need to know x and y dimensions 

# List to store parsed commands
parsed_commands = []

# Path to G-code file
path = 'g_code.txt'

# Use 'with' to safely handle file operations
with open(path, 'r') as file:
    for line in file:
        # Skip empty lines
        if not line.strip():
            continue

        # Split the line into components
        cmd = line.strip().split()
      
        # Create a new command dictionary for this line
        command = {'gcommand': None, 'X': None, 'Y': None, 'Z': None, 'I': None, 'J': None}

        # Parse each item in the command line
        for item in cmd:
            # Normalize G-code commands (e.g., G0 to G00, G1 to G01)
            if item.upper() in ['G0', 'G00', 'G1', 'G01', 'G2', 'G02', 'G3', 'G03']:
               
                    command['gcommand'] = item
            elif len(item) > 1 and item[0].upper() in ['X', 'Y', 'Z', 'I', 'J']:
                param = item[0].upper()  # Parameter type (e.g., 'X')
                try:
                    value = int(item[1:])  # Convert value to float
                    command[param] = value
                except ValueError:
                    print(f"Error: Invalid value for {item} in line {cmd}")
                    command = None  # Invalidate command on error
                    break
        if command['gcommand']=='G0' or 'G00':
             # simple moving command 
             if command['X'] is not None and command['Y'] is not None and command['Z'] is None:
                  control_cnc(command['X']-current_coordinates[0],command['Y']-current_coordinates[1])
                  current_coordinates[0]=command['X']
                  current_coordinates[1]=command['Y']
             elif command['X'] is not None and command['Y'] is None and command['Z'] is None:
                  move(xobj,conversion(abs(command['X']-current_coordinates[0])))   
                  current_coordinates[0]=command['X']  
             elif command['X'] is  None and command['Y'] is not None and command['Z'] is None :
                  move(yobj,conversion(abs(command['Y']-current_coordinates[1])))   
                  current_coordinates[1]=command['Y']  
             elif command['X'] is  None and command['Y'] is  None and command['Z'] is not None :
                  
                 if command['Z']>0:
                    pen_up()
                 elif command['Z']<0:
                    pen_down()   
print(current_coordinates)                  