# Experimental Data Analysis

Mini-projet Python d'analyse de données expérimentales.

## Objectif

Analyser un jeu de données contenant deux colonnes (x, y) :

- lecture des données
- statistiques de base
- visualisation
- ajustement d’un modèle
- interprétation des résultats

## Technologies

- Python
- NumPy
- SciPy
- Matplotlib

## Étapes de l'analyse

1. Lecture du fichier `data.txt`
2. Calcul des statistiques :
   - moyenne
   - écart-type
3. Tracé des données expérimentales
4. Ajustement d’un modèle linéaire
5. Visualisation du modèle ajusté

## Modèle utilisé

Modèle linéaire :

y = a x + b

Les paramètres sont estimés avec `scipy.optimize.curve_fit`.

## Résultat

Le graphique final montre :

- les données expérimentales
- la droite d’ajustement

## Lancer le projet

```bash
python analysis.py
