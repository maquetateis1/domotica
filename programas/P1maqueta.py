"""Programa que acende leds en vermello se a temperatura pasa de 20º
Autor: Bernardo Álvarez
Data: 20/040/2025"""

from microbit import *
import neopixel

np = neopixel.NeoPixel(pin13, 2)  # 2 LED neopixel conectados ao pin 13
rele = pin16 # LED branco conectado ao pin14
np.clear()

while True:
    temperatura = temperature() # gardamos valor da temperatura

    if temperatura > 20:
        np[0] = (0, 255, 0)  # Acender os Neopixel en vermello
        np[1] = (0, 255, 0)
        np.show()  # Mostrar a cor nos neopixel
        rele.write_digital(0)  # Acender o LED normal
    else:
        np[0] = (255, 0, 0)  # Apagar os Neopixel
        np[1] = (255, 0, 0)  # Acender os Neopixel en verde
        np.show()  # Mostrar a cor nos neopixel
        rele.write_digital(1)  # Apagar o LED normal

    sleep(100)  # Esperar 1 segundo
