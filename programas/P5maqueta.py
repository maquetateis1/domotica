"""Programa completo da fila 1 para a maqueta domótica. 
Autores: Housain, Santiago, Gandy.
Data:5/5/2025"""
from microbit import *
import music
import neopixel
# PIR sensor conectado a pin0
pir = pin0
# Tira de neopixels conectada a pin1 con 8 LEDs
np = neopixel.NeoPixel(pin1, 8)
# Colores
RED = (255, 0, 0)
OFF = (0, 0, 0)
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
