# Mon Tetris en Python

Ce projet est une implémentation simple du jeu classique Tetris en utilisant Pygame.

## Fonctionnalités

- Interface graphique basée sur Pygame
- Système de score et de niveau
- 7 pièces Tetris classiques
- Rotation des pièces
- Détection de collision
- Suppression des lignes complètes

## Prérequis

- Python 3.x
- Pygame

## Installation

1. Clonez ce dépôt : 

git clone https://github.com/votre-nom-utilisateur/mon-tetris.git

2. Installez les dépendances : pip install pygame


## Utilisation

Exécutez le fichier `tetris.py` :

![Tetris](tetris_aperçu.png)



## Règles de base

- Les pièces tombent du haut de l'écran
- Le joueur peut déplacer les pièces latéralement et les faire pivoter
- L'objectif est de créer des lignes horizontales complètes
- Lorsqu'une ligne est complétée, elle disparaît et le joueur gagne des points
- Le jeu se termine lorsque les pièces atteignent le haut de l'écran

## Système de score

- 1 ligne : 100 points
- 2 lignes : 300 points
- 3 lignes : 500 points
- 4 lignes (Tetris) : 800 points

Le score est multiplié par le niveau actuel.

## Niveaux

Le niveau augmente tous les 1000 points. Chaque niveau accélère la chute des pièces.

## Contrôles

- Flèche gauche : Déplacer la pièce à gauche
- Flèche droite : Déplacer la pièce à droite
- Flèche bas : Accélérer la chute de la pièce
- Flèche haut : Rotation de la pièce

Bonne chance et amusez-vous bien !

# Tetris
