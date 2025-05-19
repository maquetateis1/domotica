"""Programa completo da fila 1 para a maqueta domótica. 
Autores: 
Data: 
"""

from microbit import *
import music
from machine import Pin
import music
import neopixel

np = neopixel.NeoPixel(pin13, 2)  # 2 LED neopixel conectados ao pin 13

led = pin14 # LED branco conectado ao pin14
np.clear()
# Definir o LED no pin 14
led_pin = Pin(14, Pin.OUT)
# El servo está conectado a pin0
servo = machine.PWM(machine.Pin(0))
servo.freq(50)
# PIR sensor conectado a pin0
pir = pin0
# Tira de neopixels conectada a pin1 con 8 LEDs
np = neopixel.NeoPixel(pin1, 8)
# Colores
RED = (255, 0, 0)
OFF = (0, 0, 0)

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

while True:
    if pir.read_digital() == 1:  # presencia detectada
        # Reproducir ringtone dos veces
        music.play(music.POWER_UP)
        music.play(music.POWER_UP)
        # Parpadear neopixels rojos 5 veces periodo 500ms
        for _ in range(5):
            for i in range(len(np)):
                np[i] = RED
            np.show()
            sleep(500)
            for i in range(len(np)):
                np[i] = OFF
            np.show()
            sleep(500)
        # Parpadear LED blanco 5 veces periodo 500ms
        for _ in range(5):
            display.set_all(9)  # encender LED blanco (máxima intensidad)
            sleep(500)
            display.set_all(0)  # apagar LED blanco
            sleep(500)
        # Mostrar cara enfadada 5 veces en la matriz 500ms ON y 500ms OFF
        for _ in range(5):
            display.show(Image.ANGRY)
            sleep(500)
            display.clear()
            sleep(500)
    else:
        display.show(Image.HOUSE)  # mostrar casa cuando no hay presencia
        sleep(100)

while True:
    temperatura = temperature() # gardamos valor da temperatura

    if temperatura > 20:
        np[0] = (0, 255, 0)  # Acender os Neopixel en vermello
        np[1] = (0, 255, 0)
        np.show()  # Mostrar a cor nos neopixel
        led.write_digital(1)  # Acender o LED normal
    else:
        np[0] = (255, 0, 0)  # Apagar os Neopixel
        np[1] = (255, 0, 0)  # Acender os Neopixel en verde
        np.show()  # Mostrar a cor nos neopixel
        led.write_digital(0)  # Apagar o LED normal

    sleep(1000)  # Esperar 1 segundo
