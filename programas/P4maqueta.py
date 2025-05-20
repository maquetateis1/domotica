"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira 
Data: 30/04/2025
"""

from microbit import *
import machine

# Constants for servo control
# For micro:bit PWM, period 20 ms (50 Hz), duty cycle in microseconds.
# We set the PWM directly using machine.PWM

servo_pin = machine.PWM(machine.Pin(0))
servo_pin.freq(50)

# Function to convert angle to duty for micro:bit PWM: 
# We will map pulse width from 0.5 ms (500 us) to 2.5 ms (2500 us)
# but microbit PWM duty is 16 bit range and period 20 ms (20000 us)
# duty = pulse_us * max_duty / period_us

def angle_to_duty(angle):
    period = 20000  # microseconds (20ms)
    min_pulse = 500  # 0 degree pulse width in microseconds
    max_pulse = 2500  # 180 degree pulse width in microseconds
    pulse = min_pulse + (max_pulse - min_pulse) * angle / 180
    duty = int(pulse * 65535 / period)
    return duty

# Start with servo at 0 degrees
position = 0
servo_pin.duty_u16(angle_to_duty(position))

while True:
    if button_b.was_pressed():
        if position == 0:
            position = 90
        else:
            position = 0
        servo_pin.duty_u16(angle_to_duty(position))
    sleep(10)  
