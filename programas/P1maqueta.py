from microbit import *
import neopixel

# Configuración del Neopixel en el pin 13

np = neopixel.NeoPixel(pin13, 2)  # 2 LED conectado al pin 13
# Configuración del LED normal en el pin 16
led_normal = pin16
np.clear()

while True:
    # Leer la temperatura
    temperatura = temperature()

    # Si la temperatura es mayor a 28 grados, encender los LEDs
    if temperatura > 15:
        np[0] = (0, 255, 0)  # Encender el Neopixel 1 en rojo
        np[1] = (0, 255, 0)  # Encender el Neopixel 2 en rojo
        np.show()  # Mostrar el color en el LED
        led_normal.write_digital(1)  # Encender el LED normal
    else:
        np[0] = (0, 0, 0)  # Apagar el Neopixel 1
        np[1] = (0, 0, 0)  # Apagar el Neopixel 2
        np.show()  # Mostrar 
        led_normal.write_digital(0)  # Apagar el LED normal

    sleep(1000)  # Esperar 1 segundo antes de volver a comprobar la temperatura


