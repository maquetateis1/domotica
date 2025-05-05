from microbit import*
import neopixel

# Configuración del sensor PIR y los neopixels
pir_pin = pin0  # Pin donde está conectado el sensor PIR
np = neopixel.NeoPixel(pin1, 10)  # 10 LEDs neopixel en el pin1

def parpadeo_neopixel(color, veces):
    for _ in range(5):
        for i in range(len(np)):
            np[i] = color
        np.show()
        sleep(500)
        for i in range(len(np)):
            np[i] = (0, 0, 0)  # Apagar los LEDs
        np.show()   
        sleep(500)

def parpadeo_led_blanco(blanco,5):
    for _ in range(5):
        display.show(Image.SQUARE)  # LED blanco encendido
        sleep(500)
        display.clear()  # Apagar LED
        sleep(500)

def parpadeo_led_rojo(rojo ,5):
    for _ in range(5):
        display.show(Image.SQUARE)  # LED rojo encendido
        sleep(500)
        display.clear()  # Apagar LED
        sleep(500)

def mostrar_cara_enfadada(veces):
    for _ in range(5):
        display.show(Image.SAD)  # Mostrar cara enfadada
        sleep(500)
        display.clear()  # Apagar
        sleep(500)

def mostrar_casa():
    display.show(Image.HOUSE)  # Mostrar casa

while True:
    if pir_pin.read_digital() == 1:  # Si se detecta presencia
        # Emitir sonido "Ringtone" dos veces
        music.play(music.RINGTONE, wait=False)
        sleep(1000)  # Esperar un segundo
        music.play(music.RINGTONE, wait=False)
        
        # Parpadeo de neopixels en rojo
        parpadeo_neopixel((255, 0, 0), 5)
        
        # Parpadeo del LED blanco
        parpadeo_led_blanco(5)
        
        # Mostrar cara enfadada
        mostrar_cara_enfadada(5)
    else:
        mostrar_casa()  # Mostrar casa si no hay presencia

