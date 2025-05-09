"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira 
Data: 30/04/2025"""

from microbit import *
import machine

# El servo está conectado a pin0
servo = machine.PWM(machine.Pin(0))
servo.freq(50)

# Función para poner ángulo en servo (0º a 180º)
# Servo típico usa duty entre ~26 (0º) y ~128 (180º) en periodo 20ms (freq 50Hz)
# Para 0º -> duty=26, para 90º duty=77 aprox.

def set_angle(angle):
    duty = 26 + (angle * (128-26)) // 180
    servo.duty(duty)

# Estado inicial
angle = 0
set_angle(angle)

button_b_last = False

while True:
    button_b = button_b.is_pressed()
    if button_b and not button_b_last:
        # Cambiar ángulo
        if angle == 0:
            angle = 90
        else:
            angle = 0
        set_angle(angle)
    button_b_last = button_b
    sleep(50)
