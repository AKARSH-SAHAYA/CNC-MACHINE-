
from machine import Pin  # type: ignore
import time

# Stepper pin sets for X, Y, Z axes
x_pins = [4, 5, 18, 19]
y_pins = [12, 13, 14, 15]
z_pins = [27, 21, 32, 33]

# Half-step sequence (8 steps per cycle)
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

# mm to steps (based on calibration)
def convert_to_steps(distance):
    return int(distance / 0.01)  # Adjust this based on your CNC's steps per mm

# Initialize 4 pins as output for a stepper
def pins_init(pin_list):
    try:
        return [Pin(p, Pin.OUT) for p in pin_list]
    except Exception as e:
        print(f"Pin init error: {e}")
        

# Perform a single half-step sequence on the stepper
def step_motor(pin_obj, step):
    if not pin_obj:
        return
    for i in range(4):
        pin_obj[i].value(step[i])
    time.sleep(0.005)  # Adjust for motor speed

# Move forward
def move(pin_obj, steps):
    if not pin_obj:
        return
    for _ in range(steps):
        for step in forward_sequence:
            step_motor(pin_obj, step)

# Move reverse
def reverse(pin_obj, steps):
    if not pin_obj:
        return
    for _ in range(steps):
        for step in reversed(forward_sequence):
            step_motor(pin_obj, step)

# Core CNC movement function
def control_cnc(x_dist, y_dist, z_dist):
    try:
        x_steps = convert_to_steps(abs(x_dist))
        y_steps = convert_to_steps(abs(y_dist))
        z_steps = convert_to_steps(abs(z_dist))
        max_steps = max(x_steps, y_steps, z_steps, 1)
        
        x_step_size = x_dist / max_steps if max_steps > 0 else 0
        y_step_size = y_dist / max_steps if max_steps > 0 else 0
        z_step_size = z_dist / max_steps if max_steps > 0 else 0
        
        for _ in range(max_steps):
            if x_dist > 0:
                reverse(xobj, convert_to_steps(abs(x_step_size)))
            elif x_dist < 0:
                move(xobj, convert_to_steps(abs(x_step_size)))
            if y_dist > 0:
                 move(yobj, convert_to_steps(abs(y_step_size)))
            elif y_dist < 0:
                reverse(yobj, convert_to_steps(abs(y_step_size)))
                              
            if z_dist > 0:
                move(zobj, convert_to_steps(abs(z_step_size)))
            elif z_dist < 0:
                reverse(zobj, convert_to_steps(abs(z_step_size)))
    except Exception as e:
        print(f"Motion error: {e}")

# Initialize pin objects for each axis
xobj = pins_init(x_pins)
yobj = pins_init(y_pins)
zobj = pins_init(z_pins)

