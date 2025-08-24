import numpy as np
Ensayos = 10000
Lanzamientos = np.random.randint(1,7, Ensayos)
Esperanza_Practica = Lanzamientos.mean()
Dado=[1,2,3,4,5,6]
n=len(Dado)
Probxi = 0
for xi in Dado:
    Probxi = Probxi + (xi * 1/n)
print("Esperanza Practica ", Esperanza_Practica)
print("Esperanza teoriaca ", Probxi)

# correr en la terminal
# python esperanza.py

# instalar pip install numpy
