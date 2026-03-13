# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 19:29:12 2026

@author: anwar
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sc

# ============================================================
# 1) Lecture des données
# ============================================================

data = np.loadtxt("data.txt")

x = data[:,0]
y = data[:,1]

print("Nombre de points :", len(x))


# ============================================================
# 2) Statistiques de base
# ============================================================

mean_x = np.mean(x)
mean_y = np.mean(y)

std_x = np.std(x)
std_y = np.std(y)

print("\nStatistiques :")
print("Moyenne x =", mean_x)
print("Moyenne y =", mean_y)
print("Écart-type x =", std_x)
print("Écart-type y =", std_y)


# ============================================================
# 3) Tracé des données
# ============================================================

plt.figure()

plt.scatter(x, y, label="Données expérimentales")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Analyse de données expérimentales")



# ============================================================
# 4) Ajustement d'un modèle
# modèle linéaire : y = a*x + b
# ============================================================

def model(x, a, b):
    return a*x + b

popt, pcov = sc.curve_fit(model, x, y)

a = popt[0]
b = popt[1]

print("\nParamètres du modèle :")
print("a =", a)
print("b =", b)


# ============================================================
# 5) Tracé du modèle ajusté
# ============================================================

xfit = np.linspace(min(x), max(x), 200)
yfit = model(xfit, a, b)

plt.plot(xfit, yfit, color="red", label="Ajustement linéaire")

plt.legend()

plt.savefig("plot.png")
plt.show()


# ============================================================
# 6) Interprétation
# ============================================================

print("\nInterprétation :")
print("Les données montrent une relation approximativement linéaire entre x et y.")
print("Le coefficient directeur indique la variation moyenne de y lorsque x augmente.")