"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira 
Data: 30/04/2025
"""

<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Neopixel y Ventilador</title>
<style>
  body {
    background: #121212;
    color: #eee;
    font-family: Arial, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    margin: 0;
  }
  .led {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background-color: #222;
    margin-bottom: 20px;
    box-shadow: 0 0 20px #111 inset;
    transition: background-color 0.5s ease;
  }
  .led.glow {
    box-shadow:
      0 0 40px currentColor,
      0 0 80px currentColor,
      0 0 120px currentColor;
  }
  h1 {
    margin-bottom: 10px;
  }
  input[type=range] {
    width: 300px;
  }
  .ventilador-status {
    margin-top: 15px;
    font-weight: bold;
    font-size: 1.4em;
  }
  .temp-display {
    margin: 10px 0;
    font-size: 2em;
    font-weight: 600;
    font-family: monospace;
  }
</style>
</head>
<body>

<h1>Control LED Neopixel y Ventilador</h1>

<div class="led" id="led"></div>
<div class="temp-display" id="tempDisplay">Temperatura: 18ºC</div>
<input type="range" id="tempSlider" min="15" max="35" step="0.1" value="18" aria-label="Selector de temperatura"/>
<div class="ventilador-status" id="ventiladorStatus">Ventilador apagado</div>

<script>
  const led = document.getElementById('led');
  const tempDisplay = document.getElementById('tempDisplay');
  const tempSlider = document.getElementById('tempSlider');
  const ventiladorStatus = document.getElementById('ventiladorStatus');

  let temperatura = parseFloat(tempSlider.value);

  tempSlider.addEventListener('input', () => {
    temperatura = parseFloat(tempSlider.value);
    tempDisplay.textContent = 'Temperatura: ' + temperatura.toFixed(1) + 'ºC';

    if (temperatura > 24) {
      led.style.backgroundColor = '#e74c3c'; // rojo
      led.classList.add('glow');
      led.style.color = '#e74c3c';
      ventiladorStatus.textContent = 'Ventilador activado';
      ventiladorStatus.style.color = '#e74c3c';
    } else {
      led.style.backgroundColor = '#2ecc71'; // verde
      led.classList.add('glow');
      led.style.color = '#2ecc71';
      ventiladorStatus.textContent = 'Ventilador apagado';
      ventiladorStatus.style.color = '#2ecc71';
    }
  });

  tempSlider.dispatchEvent(new Event('input'));
</script>

</body>
</html>
