from microbit import *
import music

# Pin onde está conectado o LED (pin 14)
led_pin = pin14

# Definir a duración do LED (5 segundos)
led_duration = 5000

# Bucle principal
while True:
    if button_a.is_pressed():  # Comprobar se o botón A está pulsado
        # Acender o LED
        led_pin.write_digital(1)
        
        # Reproducir o son RINGTONE (ou outro que desexes)
        music.play(music.RINGTONE)
        
        # Esperar 5 segundos
        sleep(led_duration)
        
        # Apagar o LED
        led_pin.write_digital(0)
        
        # Facer unha pequena pausa antes de comprobar de novo
        sleep(100)
