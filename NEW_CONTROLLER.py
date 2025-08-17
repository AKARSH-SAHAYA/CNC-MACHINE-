from machine import Pin # type: ignore
import time


# Stepper pin sets for X, Y, Z axes
x_pins = [13,16,17,23]
y_pins = [19,21,22,25]
z_pins = [26,27,32,33]

# Half-step sequence (8 steps per cycle)
halfstep_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

def conversion(distance):
    """Convert distance (mm) to steps (assuming 0.01mm/step)."""
    return round(float(distance / 0.01),3)  # Ensure integer steps

def pins_init(pins):
    """Initialize a list of Pin objects for stepper motor control."""
    try:
        return [Pin(pin, Pin.OUT) for pin in pins]
    except Exception as e:
        print(f"Pin initialization error: {e}")
        return []

def step_motor(pin_obj, step):
    """Perform a single half-step sequence on the stepper."""
    if not pin_obj or len(pin_obj) != 4:
        print("Invalid pin object")
        return
    try:
        for i in range(4):
            pin_obj[i].value(step[i])
        time.sleep_ms(2)  # Configurable delay (2ms for smoother motion)
    except Exception as e:
        print(f"Step motor error: {e}")

def move(pin_obj, steps):
    """Move stepper motor forward for specified steps."""
    if not pin_obj or steps < 0:
        print("Invalid move parameters")
        return
    try:
        for _ in range(int(steps)):
            for step in halfstep_sequence:
                step_motor(pin_obj, step)
    except Exception as e:
        print(f"Move error: {e}")

def reverse(pin_obj, steps):
    """Move stepper motor backward for specified steps."""
    if not pin_obj or steps < 0:
        print("Invalid reverse parameters")
        return
    try:
        for _ in range(int(steps)):
            for step in reversed(halfstep_sequence):
                step_motor(pin_obj, step)
    except Exception as e:
        print(f"Reverse error: {e}")

def control_cnc(x_dist, y_dist):
    """Control CNC movement for X and Y axes."""
    try:
        x_dist=round(float(x_dist),3)
        y_dist=round(float(y_dist),3)
        x_steps = conversion(abs(x_dist))
        y_steps = conversion(abs(y_dist))
        max_steps = max(x_steps, y_steps,1)

        
        x_step_size = x_steps / max_steps  # Steps per iteration
        y_step_size = y_steps / max_steps  # Steps per iteration

        x_accum = 0.0  # Accumulated steps for X
        y_accum = 0.0  # Accumulated steps for Y

        for _ in range(int(max_steps)):
            if x_dist != 0:
                x_accum += x_step_size
                if x_accum >= 1.0:
                    steps = int(x_accum)
                    x_accum -= steps
                    if x_dist > 0:
                        reverse(xobj, steps) 
                    else:
                        move(xobj, steps)
                       
                        
                        
            if y_dist != 0:
                y_accum += y_step_size
                if y_accum >= 1.0:
                    steps = int(y_accum)
                    y_accum -= steps
                    if y_dist > 0:
                        reverse(yobj, steps)
                    else:
                        move(yobj, steps) 
                        
                        
                        
                        
                        
    except Exception as e:
        print(f"Motion error: {e}")

def pen_down():
    """Lower the pen (Z-axis forward)."""
    try:
        move(zobj, 50)
    except Exception as e:
        print(f"Pen down error: {e}")

def pen_up():
    """Raise the pen (Z-axisbackward)."""
    try:
        reverse(zobj, 50)
    except Exception as e:
        print(f"Pen up error: {e}")


# Initialize pin objects
xobj = pins_init(x_pins)
yobj = pins_init(y_pins)
zobj = pins_init(z_pins)

