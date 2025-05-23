"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira 
Data: 30/04/2025
"""

import time
import board
import neopixel
import adafruit_dht

# Configuración de pines (ajusta según tu conexión)
PIN_NEOPIXEL = board.D2  # Pin donde conectas los Neopixel (ej. GPIO2 en ESP32)
PIN_RELE_VENTILADOR = board.D4  # Pin donde conectas el relé del ventilador (ej. GPIO4 en ESP32)
PIN_SENSOR_DHT = board.D15 # Pin donde conectas el sensor DHT11/22 (ej. GPIO15 en ESP32)

NUM_PIXELS = 1 # Si solo tienes un Neopixel, si tienes una tira ajusta este valor

# Inicialización de Neopixel
pixels = neopixel.NeoPixel(PIN_NEOPIXEL, NUM_PIXELS, brightness=0.5, auto_write=False)

# Inicialización del sensor DHT
dht_sensor = adafruit_dht.DHT22(PIN_SENSOR_DHT) # O adafruit_dht.DHT11 si usas ese modelo

# Lógica principal del programa
while True:
    try:
        temperatura = dht_sensor.temperature
        print(f"Temperatura: {temperatura:.1f} ºC")

        if temperatura > 24:
            # Temperatura alta: Neopixel rojo y ventilador encendido
            pixels.fill((255, 0, 0))  # Rojo
            pixels.show()
            board.digitalio.DigitalInOut(PIN_RELE_VENTILADOR).direction = board.digitalio.Direction.OUTPUT
            board.digitalio.DigitalInOut(PIN_RELE_VENTILADOR).value = True # Activa el relé
            print("Temperatura > 24ºC: LED ROJO, Ventilador ENCENDIDO")
        else:
            # Temperatura baja: Neopixel verde y ventilador apagado
            pixels.fill((0, 255, 0))  # Verde
            pixels.show()
            board.digitalio.DigitalInOut(PIN_RELE_VENTILADOR).direction = board.digitalio.Direction.OUTPUT
            board.digitalio.DigitalInOut(PIN_RELE_VENTILADOR).value = False # Desactiva el relé
            print("Temperatura <= 24ºC: LED VERDE, Ventilador APAGADO")

    except RuntimeError as error:
        # Errores de lectura del sensor DHT (comunes al inicio)
        print(f"Error al leer el sensor DHT: {error.args[0]}")
    except Exception as error:
        # Otros errores inesperados
        print(f"Ocurrió un error inesperado: {error}")

    time.sleep(5) # Espera 5 segundos antes de la siguiente lectura
