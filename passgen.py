import string
import random

tamaño = int(input("Indique el tamaño de la contraseña: "))
caracteres = string.ascii_letters + string.digits 
password = "".join(random.choice(caracteres) for i in range(tamaño))

print("La contraseña generada es: " + password)