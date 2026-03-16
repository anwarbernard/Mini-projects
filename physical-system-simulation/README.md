# Physical System Simulation — Damped Oscillator

Projet Python de simulation d’un système physique : **oscillateur amorti**.

## Objectif

Simuler numériquement le mouvement d’un système masse-ressort-amortisseur et analyser son comportement au cours du temps.

L’équation étudiée est :

m x'' + c x' + k x = 0

avec :
- `m` : masse
- `c` : coefficient d’amortissement
- `k` : raideur du ressort

## Fonctionnalités

- résolution numérique avec `scipy.integrate.solve_ivp`
- tracé de la position `x(t)`
- tracé de la vitesse `v(t)`
- calcul des énergies :
  - cinétique
  - potentielle
  - totale
- interprétation physique des résultats

## Technologies utilisées

- Python
- NumPy
- SciPy
- Matplotlib

## Structure du projet

```bash
physical-system-simulation/
│
├── simulation.py
├── README.md
├── requirements.txt
└── figures/
    ├── position.png
    ├── velocity.png
    └── energy.png
