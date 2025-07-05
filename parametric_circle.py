import math

def generate_arc(cx, cy, x0, y0, x1, y1, clockwise=False, step_deg=2):
    points = []

    # Radius
    r = math.sqrt((x0 - cx)**2 + (y0 - cy)**2)

    # Start and end angles in radians
    angle_start = math.atan2(y0 - cy, x0 - cx)
    angle_end = math.atan2(y1 - cy, x1 - cx)

    # Normalize angles between 0 and 2π
    if angle_start < 0:
        angle_start += 2 * math.pi
    if angle_end < 0:
        angle_end += 2 * math.pi

    # Compute sweep angle
    if clockwise:
        if angle_start <= angle_end:
            angle_start += 2 * math.pi
        sweep = angle_start - angle_end
        direction = -1
    else:
        if angle_end <= angle_start:
            angle_end += 2 * math.pi
        sweep = angle_end - angle_start
        direction = 1

    # Convert step from degrees to radians
    step_rad = math.radians(step_deg)
    steps = int(sweep / step_rad) + 1

    # Generate points
    for i in range(steps + 1):
        theta = angle_start + direction * i * step_rad
        x = round(cx + r * math.cos(theta))
        y = round(cy + r * math.sin(theta))
        points.append((x, y))

    return points
x0, y0 = 15, 10

# End point
x1, y1 = 10, 15

# Center of arc
cx, cy = 10, 10

# G3 → counter-clockwise
arc_points = generate_arc(cx, cy, x0, y0, x1, y1, clockwise=False)  #G03- FALSE ACW 

for pt in arc_points:
    print("Plot:", pt)
