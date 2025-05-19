"""Programa completo da fila 1 para a maqueta domótica. 
Autores: 
Data: 
"""

from microbit import *
import music
from machine import Pin

# Definir o LED no pin 14
led_pin = Pin(14, Pin.OUT)
# El servo está conectado a pin0
servo = machine.PWM(machine.Pin(0))
servo.freq(50)

while True:
    if button_a.was_pressed():
        led_pin.write_digital(1)  # Acende o LED conectado ao pin 14
        music.play(music.RINGTONE)  # Reproduce o son RINGTONE
        sleep(5000)  # Espera 5 segundos
        led_pin.write_digital(0)  # Apaga o LED


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
