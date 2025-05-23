"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira 
Data: 30/04/2025
"""

from microbit import *

# Inicializamos el servo a 0 grados
servo_angle = 0
pin_servo.write_analog(0) # Asumiendo que el servo está conectado al pin_servo (por ejemplo, pin1)

while True:
    if button_b.was_pressed():
        if servo_angle == 0:
            servo_angle = 90
        else:
            servo_angle = 0
        pin_servo.write_analog(servo_angle) # Actualizamos la posición del servo
    sleep(10) # Pequeña pausa para evitar lecturas múltiples del botón
