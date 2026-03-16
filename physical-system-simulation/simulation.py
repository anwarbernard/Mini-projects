# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 07:12:15 2026

@author: anwar
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# ============================================================
# 1) Paramètres physiques
# ============================================================

m = 1.0       # masse (kg)
c = 0.8       # coefficient d'amortissement (kg/s)
k = 10.0      # raideur du ressort (N/m)

x0 = 0.10     # position initiale (m)
v0 = 0.0      # vitesse initiale (m/s)

t_min = 0.0
t_max = 10.0
n_points = 1000
t_eval = np.linspace(t_min, t_max, n_points)


# ============================================================
# 2) Équation différentielle
#    y = [x, v]
#    x' = v
#    v' = -(c/m)v - (k/m)x
# ============================================================

def damped_oscillator(t, y):
    x, v = y
    dxdt = v
    dvdt = -(c / m) * v - (k / m) * x
    return [dxdt, dvdt]


# ============================================================
# 3) Résolution numérique
# ============================================================

sol = solve_ivp(
    damped_oscillator,
    (t_min, t_max),
    [x0, v0],
    t_eval=t_eval
)

t = sol.t
x = sol.y[0]
v = sol.y[1]


# ============================================================
# 4) Énergies
# ============================================================

kinetic_energy = 0.5 * m * v**2
potential_energy = 0.5 * k * x**2
total_energy = kinetic_energy + potential_energy


# ============================================================
# 5) Statistiques simples
# ============================================================

print("=== Simulation d'un oscillateur amorti ===")
print(f"Masse m = {m} kg")
print(f"Amortissement c = {c} kg/s")
print(f"Raideur k = {k} N/m")
print(f"Position initiale x0 = {x0} m")
print(f"Vitesse initiale v0 = {v0} m/s")
print()
print(f"Position max = {np.max(x):.5f} m")
print(f"Position min = {np.min(x):.5f} m")
print(f"Vitesse max = {np.max(v):.5f} m/s")
print(f"Vitesse min = {np.min(v):.5f} m/s")
print(f"Énergie totale initiale = {total_energy[0]:.6f} J")
print(f"Énergie totale finale   = {total_energy[-1]:.6f} J")


# ============================================================
# 6) Création du dossier figures
# ============================================================

os.makedirs("figures", exist_ok=True)


# ============================================================
# 7) Tracé position
# ============================================================

plt.figure(figsize=(8, 5))
plt.plot(t, x)
plt.xlabel("Temps t (s)")
plt.ylabel("Position x (m)")
plt.title("Oscillateur amorti - Position")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/position.png", dpi=300)
plt.show()


# ============================================================
# 8) Tracé vitesse
# ============================================================

plt.figure(figsize=(8, 5))
plt.plot(t, v)
plt.xlabel("Temps t (s)")
plt.ylabel("Vitesse v (m/s)")
plt.title("Oscillateur amorti - Vitesse")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/velocity.png", dpi=300)
plt.show()


# ============================================================
# 9) Tracé énergie
# ============================================================

plt.figure(figsize=(8, 5))
plt.plot(t, kinetic_energy, label="Énergie cinétique")
plt.plot(t, potential_energy, label="Énergie potentielle")
plt.plot(t, total_energy, label="Énergie totale")
plt.xlabel("Temps t (s)")
plt.ylabel("Énergie (J)")
plt.title("Oscillateur amorti - Énergies")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/energy.png", dpi=300)
plt.show()


# ============================================================
# 10) Interprétation
# ============================================================

print()
print("=== Interprétation ===")
print("Le système oscille autour de la position d'équilibre.")
print("L'amplitude diminue avec le temps à cause de l'amortissement.")
print("L'énergie totale décroît progressivement car une partie de")
print("l'énergie mécanique est dissipée par les frottements.")