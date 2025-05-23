"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira 
Data: 30/04/2025
"""

Copy# Importing the datetime module to get the current time
import datetime

# Defining the day and night time ranges
daytime = range(6, 18)  # Assuming daytime from 6:00 to 17:59
nighttime = range(18, 6+24) # Assuming nighttime from 18:00 to 5:59 the next day

# Getting the current time
current_time = datetime.datetime.now().time()

# Checking if it's night or day
if current_time.hour in nighttime:
    print("It's night time. Turning on the white LED.")
    # Code to turn on the white LED goes here
else:
    print("It's day time. Turning off the white LED.")
    # Code to turn off the white LED goes here

