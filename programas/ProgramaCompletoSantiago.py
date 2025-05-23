"""Programa completo da fila 1 para a maqueta domótica. 
Autores: Gandy, Santiao, Housain 
Data: 
"""

import time

# --- Inicio del programa principal ---
print("************************************************************")
print("* Sistema de Control de Micro:bit Combinado         *")
print("************************************************************")
print("Este programa simula el comportamiento de varios sensores y actuadores.")
print("Elige una opción para simular un evento:")
print("  'A'  : Simular pulsación del Botón A (LED y Ringtone)")
print("  'T'  : Simular lectura de Temperatura (Neopixel y Ventilador)")
print("  'P'  : Simular detección de Presencia PIR (Micro:bit alerta)")
print("  'B'  : Simular pulsación del Botón B (Control de Servo)")
print("  'S'  : Salir del programa")
print("************************************************************")

# Variables de estado iniciales para el servo (simuladas)
servo_angle = 0 # 0 grados inicialmente
# En una micro:bit real: pin_servo.write_analog(0)

while True: # Bucle principal que mantiene el programa en ejecución
    try:
        opcion_elegida = input("\nElige una opción (A, T, P, B, S): ").strip().upper()

        if opcion_elegida == 'A':
            print("\n--- Simulación: Botón A Pulsado ---")
            print("Botón A pulsado. ¡Activando LED y RINGTONE!")

            # Simula el encendido del LED
            print("LED Blanco: ENCENDIDO")
            # Código real para micro:bit: pin.P_LED_BLANCO.write_digital(1)

            # Simula la reproducción del sonido RINGTONE
            print("Sonido: RINGTONE reproduciéndose...")
            # Código real para micro:bit: music.play(music.RINGTONE)

            # Esperamos 5 segundos
            time.sleep(5)

            # Simula el apagado del LED
            print("LED Blanco: APAGADO")
            # Código real para micro:bit: pin.P_LED_BLANCO.write_digital(0)
            print("Sonido: RINGTONE terminado.")
            print("Proceso de Botón A completado.")

        elif opcion_elegida == 'T':
            print("\n--- Simulación: Sensor de Temperatura ---")
            try:
                temperatura_str = input("Introduce la temperatura actual en grados Celsius: ")
                temperatura = float(temperatura_str)

                print(f"Temperatura detectada: {temperatura}°C")

                # Condición para temperatura alta (superior a 24º)
                if temperatura > 24:
                    print("--- ¡ALERTA: TEMPERATURA ALTA! ---")
                    print("Neopixel: ILUMINADO EN ROJO")
                    # Código real para micro:bit: np.fill((255, 0, 0)); np.show()
                    print("Ventilador: ENCENDIDO (Relé activado)")
                    # Código real para micro:bit: pin.P_RELE.write_digital(1)
                # Condición para temperatura baja (24º o inferior)
                else:
                    print("--- Temperatura normal ---")
                    print("Neopixel: ILUMINADO EN VERDE")
                    # Código real para micro:bit: np.fill((0, 255, 0)); np.show()
                    print("Ventilador: APAGADO (Relé desactivado)")
                    # Código real para micro:bit: pin.P_RELE.write_digital(0)
            except ValueError:
                print("Error: Por favor, introduce un número válido para la temperatura.")

        elif opcion_elegida == 'P':
            print("\n--- Simulación: Sensor PIR ---")
            deteccion_pir_str = input("¿El sensor PIR detecta presencia? (escribe 'si' o 'no'): ").strip().lower()

            if deteccion_pir_str == "si":
                print("\n--- ¡PRESENCIA DETECTADA! ---")

                # Micro:bit emite el sonido “Ringtone” dúas veces
                print("Sonido: Ringtone (1/2)")
                # Código real para micro:bit: music.play(music.RINGTONE)
                time.sleep(0.5) # Pausa simulada entre tonos
                print("Sonido: Ringtone (2/2)")
                # Código real para micro:bit: music.play(music.RINGTONE)
                time.sleep(0.5) # Pausa simulada

                # LEDs Neopixel parpadean en rojo cinco veces en períodos de 500 ms
                print("Neopixel: Iniciando parpadeo ROJO...")
                for i in range(5):
                    print(f"  Parpadeo {i+1}/5: Neopixel ROJO")
                    # Código real para micro:bit: np.fill((255, 0, 0)); np.show()
                    time.sleep(0.5) # Esperar 500 ms

                    print(f"  Parpadeo {i+1}/5: Neopixel APAGADO")
                    # Código real para micro:bit: np.fill((0, 0, 0)); np.show()
                    time.sleep(0.5) # Esperar 500 ms

                # El LED blanco parpadea también 5 veces en períodos de 500 ms
                print("LED Blanco: Iniciando parpadeo...")
                for i in range(5):
                    print(f"  Parpadeo {i+1}/5: LED Blanco ENCENDIDO")
                    # Código real para micro:bit: pin.P_LED_BLANCO.write_digital(1)
                    time.sleep(0.5) # Esperar 500 ms

                    print(f"  Parpadeo {i+1}/5: LED Blanco APAGADO")
                    # Código real para micro:bit: pin.P_LED_BLANCO.write_digital(0)
                    time.sleep(0.5) # Esperar 500 ms

                # En la matriz aparece la cara enfadada durante 5 veces en períodos de 500 ms
                print("Matriz: Iniciando parpadeo de CARA ENFADADA...")
                for i in range(5):
                    print(f"  Parpadeo {i+1}/5: Matriz Muestra Cara Enfadada")
                    # Código real para micro:bit: display.show(Image.ANGRY)
                    time.sleep(0.5) # Esperar 500 ms

                    print(f"  Parpadeo {i+1}/5: Matriz APAGADA")
                    # Código real para micro:bit: display.clear()
                    time.sleep(0.5) # Esperar 500 ms

                print("--- Secuencia de alerta finalizada. ---")

            elif deteccion_pir_str == "no":
                print("\n--- Sensor PIR: SIN PRESENCIA. ---")
                print("Matriz: Mostrando CASA.")
                # Código real para micro:bit: display.show(Image.HOUSE)
                # Asegurarse de que los Neopixel y el LED blanco estén apagados
                # np.fill((0, 0, 0)); np.show()
                # pin.P_LED_BLANCO.write_digital(0)
            else:
                print("Entrada no válida para PIR. Por favor, escribe 'si' o 'no'.")

        elif opcion_elegida == 'B':
            print("\n--- Simulación: Botón B Pulsado (Control de Servo) ---")
            # Simula la pulsación del botón B
            # En una micro:bit real: if button_b.was_pressed():
            if servo_angle == 0:
                servo_angle = 90
                print("Servo: Moviéndose a 90 grados.")
            else:
                servo_angle = 0
                print("Servo: Moviéndose a 0 grados.")
            # Código real para micro:bit: pin_servo.write_analog(servo_angle)
            # Nota: 'write_analog' es una función. En un entorno real de micro:bit,
            # el control de un servo implica el uso de una función de la librería 'pin'.
            # Para cumplir estrictamente "sin funciones", solo podemos simularlo.
            time.sleep(0.1) # Pequeña pausa para simular el movimiento del servo

        elif opcion_elegida == 'S':
            print("\nSaliendo del programa. ¡Hasta pronto!")
            break # Sale del bucle principal

        else:
            print("Opción no válida. Por favor, elige A, T, P, B o S.")

        # Pequeña pausa general para evitar que el bucle se ejecute demasiado rápido
        time.sleep(0.2)

    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario (Ctrl+C).")
        break

# --- Fin del programa principal ---
print("Programa de simulación finalizado.")
