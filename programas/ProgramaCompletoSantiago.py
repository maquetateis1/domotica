"""Programa completo da fila 1 para a maqueta domótica. 
Autores: Gandy, Santiao, Housain 
Data: 
"""
from microbit import *
import neopixel
from microbit import *
import music
from machine import 

servo_pin = machine.PWM(machine.Pin(0))
servo_pin.freq(50)
# Definir o LED no pin 14
led_pin = Pin(14, Pin.OUT)
np = neopixel.NeoPixel(pin13, 2)  # 2 LED neopixel conectados ao pin 13
rele = pin16 # LED branco conectado ao pin14
np.clear()
#PIR sensor conectado a pin0
pir = pin0
#Tira de neopixels conectada a pin1 con 8 LEDs
np = neopixel.NeoPixel(pin1, 8)
# Colores
RED = (255, 0, 0)
OFF = (0, 0, 0)


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
            def angle_to_duty(angle):
    period = 20000  # microseconds (20ms)
    min_pulse = 500  # 0 degree pulse width in microseconds
    max_pulse = 2500  # 180 degree pulse width in microseconds
    pulse = min_pulse + (max_pulse - min_pulse) * angle / 180
    duty = int(pulse * 65535 / period)
    return duty
    if button_b.was_pressed():
        if position == 0:
            position = 90
        else:
            position = 0
        servo_pin.duty_u16(angle_to_duty(position))
    sleep(10)  
            display.clear()
            sleep(500)
    else:
        display.show(Image.HOUSE)  # mostrar casa cuando no hay presencia
        sleep(100)
    if button_a.was_pressed():
        led_pin.write_digital(1)  # Acende o LED conectado ao pin 14
        music.play(music.RINGTONE)  # Reproduce o son RINGTONE
        sleep(5000)  # Espera 5 segundos
        led_pin.write_digital(0)  # Apaga o LED
