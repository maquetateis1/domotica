"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira 
Data: 30/04/2025
"""

import time

# Asumiendo que 'LED' y 'RINGTONE' son predefinidos o accesibles en el entorno
# Por ejemplo, en un entorno como MicroPython o Arduino (con sintaxis Python-like)
# LED_PIN = 2  # Asumiendo que el LED está conectado al pin 2
# BUTTON_PIN = 3 # Asumiendo que el botón A está conectado al pin 3
# speaker = Speaker() # Asumiendo una clase o función para controlar el sonido

print("Programa iniciado. Esperando la pulsación del botón A...")

while True:
    # Simulación de la lectura del botón A
    # En un microcontrolador real, esto sería una lectura de un pin digital
    button_A_pressed = input("Pulsa 'A' y Enter para simular la pulsación del botón A: ").strip().upper()

    if button_A_pressed == 'A':
        print("Botón A pulsado. Encendiendo LED y reproduciendo RINGTONE...")
        # Encender el LED
        # Esto es una simulación; en hardware real se activaría el pin del LED
        print("LED: ON")

        # Reproducir el sonido RINGTONE
        # Esto es una simulación; en hardware real se activaría la reproducción de sonido
        print("Sonido: RINGTONE reproduciéndose...")

        time.sleep(5) # Esperar 5 segundos

        # Apagar el LED
        print("LED: OFF")
        print("Sonido: RINGTONE terminado.")
        print("Esperando la próxima pulsación del botón A...")
    else:
        print("Pulsación no reconocida. Intenta de nuevo.")
