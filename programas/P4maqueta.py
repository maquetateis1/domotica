"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira 
Data: 30/04/2025"""
from microbit import *
import time

# Inicializar el servo en el pin0
pin0.set_analog_period(20) # Período 20ms

angle = 0

while True:
    # Calcular d en línea
pulse_ms = 0.5 + (angle / 180.0) * 2.0
duty = int((pulse_ms / 20) * 1023)
pin0.write_analog(duty)
sleep(100)

   if button_b.was_pressed():
# Incrementar angulo en 10 hasta 90, luego 0
   if angle < 90:
angle += 10
   else:
angle = 0
