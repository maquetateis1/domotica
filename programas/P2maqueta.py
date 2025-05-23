"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira 
Data: 30/04/2025
"""

<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>LED Blanco Día-Noche</title>
<style>
  body {
    background-color: #111;
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
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background-color: #333;
    box-shadow: inset 0 0 20px #000;
    margin-bottom: 20px;
    transition: background-color 0.5s ease, box-shadow 0.5s ease;
  }
  .led.encendido {
    background-color: #fff;
    box-shadow:
      0 0 40px #fff,
      0 0 80px #fff,
      0 0 120px #fff;
  }
  h1 {
    margin-bottom: 10px;
  }
  .status {
    font-size: 1.3em;
  }
</style>
</head>
<body>

<h1>LED Blanco Día y Noche</h1>
<div id="led" class="led"></div>
<div id="texto" class="status"></div>

<script>
  var led = document.getElementById('led');
  var texto = document.getElementById('texto');
  var ahora = new Date();
  var hora = ahora.getHours();
  if (hora >= 6 && hora < 18) {
    // Día - LED apagado
    led.classList.remove('encendido');
    texto.textContent = 'Es de día, el LED está apagado.';
  } else {
    // Noche - LED encendido
    led.classList.add('encendido');
    texto.textContent = 'Es de noche, el LED está encendido.';
  }
</script>

</body>
</html>
