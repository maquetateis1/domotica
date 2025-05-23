"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira 
Data: 30/04/2025
"""

Copyimport time
import board
import digitalio
import audioio

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=digitalio.Pull.DOWN)

wave_file = open("RINGTONE.wav", "rb")
ringtone = audioio.WaveFile(wave_file)

while True:
    if button_a.value:
        led.value = True
        audioio.AudioOut(board.A0, ringtone).play()
        time.sleep(5)
        led.value = False

