"""Programa completo da fila 1 para a maqueta domótica. 
Autores: 
Data: 
"""
from microbit import *
from machine import Pin
import music
import music
import neopixel
import time

np = neopixel.NeoPixel(pin13, 2)  # 2 LED neopixel conectados ao pin 13

led = pin14 # LED branco conectado ao pin14
np.clear()
# Definir o LED no pin 14
led_pin = Pin(14, Pin.OUT)
# El servo está conectado a pin0
servo = machine.PWM(machine.Pin(0))
servo.freq(50)
# Inicializar el servo en el pin0
pin0.set_analog_period(20)  # Período 20ms (50Hz)
angle = 0
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
