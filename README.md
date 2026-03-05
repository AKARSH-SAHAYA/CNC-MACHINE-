# ESP32 CNC Machine (MicroPython)

A simple **DIY CNC machine project using ESP32 and MicroPython**.
This project demonstrates how a **28BYJ-48 stepper motor** can be controlled using an **ESP32 microcontroller** to create a basic CNC drawing/engraving mechanism.

The project is intended for **learning motion control, embedded programming, and stepper motor interfacing** with MicroPython.

---



## Hardware Used

* **ESP32 Development Board**
* **28BYJ-48 Stepper Motor**
* **ULN2003 Stepper Motor Driver**
* Power Supply (5V)
* Mechanical frame for CNC movement
* Pen/marker for drawing

---

## Software Used

* **MicroPython firmware for ESP32**
* Python scripts for stepper control
* Serial interface for program upload

---

## How It Works

1. The **ESP32 runs MicroPython firmware**.
2. The **28BYJ-48 stepper motor** is connected through a **ULN2003 driver board**.
3. MicroPython code sends step sequences to rotate the motor.
4. Controlled movements allow the CNC mechanism to **draw shapes or images**.

---

## Stepper Motor Control

The **28BYJ-48** is a **5-wire unipolar stepper motor** commonly used in low-cost robotics projects.

Typical control sequence:

```
IN1 → GPIO
IN2 → GPIO
IN3 → GPIO
IN4 → GPIO
```

The ESP32 sends step signals to the **ULN2003 driver**, which energizes the coils of the stepper motor in sequence.

---

## Project Structure

```
CNC-MACHINE
│
├── main.py
├── stepper.py
├── README.md

    
```

---

## Setup Instructions

### 1. Install MicroPython on ESP32

Flash MicroPython firmware using:

```
esptool.py --chip esp32 write_flash -z 0x1000 firmware.bin
```

### 2. Upload Code

Use **ampy** or **Thonny IDE** to upload files:

```
ampy --port /dev/ttyUSB0 put main.py
```

### 3. Connect Stepper Motor

Connect the **ULN2003 driver pins to ESP32 GPIO**.

Example:

| ULN2003 | ESP32   |
| ------- | ------- |
| IN1     | GPIO 14 |
| IN2     | GPIO 27 |
| IN3     | GPIO 26 |
| IN4     | GPIO 25 |

---

## Example MicroPython Code

```python
from machine import Pin
import time

pins = [
    Pin(14, Pin.OUT),
    Pin(27, Pin.OUT),
    Pin(26, Pin.OUT),
    Pin(25, Pin.OUT)
]

sequence = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

while True:
    for step in sequence:
        for i in range(4):
            pins[i].value(step[i])
        time.sleep_ms(5)
```

---

## Applications

* DIY CNC plotter
* Educational robotics
* Motion control learning
* Embedded systems practice

---

## Future Improvements

* Add **X-Y axis control**
* Implement **G-code interpreter**
* Integrate **LVGL GUI**
* Improve motion precision
* Add **WiFi control via ESP32**

---

## Author

**Akarsh Sahaya**

GitHub:
https://github.com/AKARSH-SAHAYA

---

## License

This project is open-source and free to use for learning and experimentation.
