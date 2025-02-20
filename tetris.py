import pygame
import random

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
largeur, hauteur = 300, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Tetris")

# Définir les couleurs
noir = (0, 0, 0)
blanc = (255, 255, 255)
rouge = (255, 0, 0)
vert = (0, 255, 0)
bleu = (0, 0, 255)

# Définir les formes des pièces pour chaque rotation
formes = [
    [
        [[1, 1, 1], [0, 1, 0]],  # T
        [[1, 0, 0], [1, 1, 0], [1, 0, 0]],
        [[0, 1, 0], [1, 1, 1]],
        [[0, 0, 1], [0, 1, 1], [0, 0, 1]]
    ],
    [
        [[1, 1, 1, 1]],  # I
        [[1], [1], [1], [1]],
        [[1, 1, 1, 1]],
        [[1], [1], [1], [1]]
    ],
    [
        [[1, 1], [1, 1]],  # O
        [[1, 1], [1, 1]],
        [[1, 1], [1, 1]],
        [[1, 1], [1, 1]]
    ],
    [
        [[0, 1, 1], [1, 1, 0]],  # S
        [[1, 0, 0], [1, 1, 0], [0, 1, 0]],
        [[0, 1, 1], [1, 1, 0]],
        [[1, 0, 0], [1, 1, 0], [0, 1, 0]]
    ],
    [
        [[1, 1, 0], [0, 1, 1]],  # Z
        [[0, 1, 0], [1, 1, 0], [1, 0, 0]],
        [[1, 1, 0], [0, 1, 1]],
        [[0, 1, 0], [1, 1, 0], [1, 0, 0]]
    ],
    [
        [[1, 1, 1], [1, 0, 0]],  # L
        [[1, 0, 0], [1, 0, 0], [1, 1, 0]],
        [[0, 0, 1], [1, 1, 1]],
        [[0, 1, 1], [0, 0, 1], [0, 0, 1]]
    ],
    [
        [[1, 1, 1], [0, 0, 1]],  # J
        [[0, 1, 0], [0, 1, 0], [1, 1, 0]],
        [[1, 0, 0], [1, 1, 1]],
        [[1, 1, 0], [1, 0, 0], [1, 0, 0]]
    ]
]

# Définir les couleurs des pièces
couleurs = [rouge, vert, bleu, (255, 255, 0), (255, 165, 0), (128, 0, 128), (0, 255, 255)]

# Définir la taille des blocs
taille_bloc = 30

# Initialiser le score et le niveau
score = 0
niveau = 1

# Définir les valeurs de score pour les lignes
scores_lignes = {1: 100, 2: 300, 3: 500, 4: 800}

# Fonction pour dessiner une pièce
def dessiner_piece(piece, offset):
    forme = formes[piece['forme']][piece['rotation']]
    couleur = couleurs[piece['forme']]
    for y, ligne in enumerate(forme):
        for x, bloc in enumerate(ligne):
            if bloc:
                pygame.draw.rect(fenetre, couleur, ((offset['x'] + x) * taille_bloc, (offset['y'] + y) * taille_bloc, taille_bloc, taille_bloc), 0)

# Fonction pour créer une nouvelle pièce
def nouvelle_piece():
    return {'forme': random.randint(0, len(formes) - 1), 'rotation': 0, 'x': largeur // taille_bloc // 2 - 1, 'y': 0}

# Fonction pour vérifier les collisions
def collision(piece, offset, blocs):
    forme = formes[piece['forme']][piece['rotation']]
    for y, ligne in enumerate(forme):
        for x, bloc in enumerate(ligne):
            if bloc:
                if (offset['x'] + x < 0 or offset['x'] + x >= largeur // taille_bloc or
                        offset['y'] + y >= hauteur // taille_bloc or
                        blocs[offset['y'] + y][offset['x'] + x]):
                    return True
    return False

# Fonction pour fusionner la pièce avec les blocs fixés
def fusionner_piece(piece, offset, blocs, blocs_couleurs):
    forme = formes[piece['forme']][piece['rotation']]
    couleur = couleurs[piece['forme']]
    for y, ligne in enumerate(forme):
        for x, bloc in enumerate(ligne):
            if bloc:
                blocs[offset['y'] + y][offset['x'] + x] = 1
                blocs_couleurs[offset['y'] + y][offset['x'] + x] = couleur

# Fonction pour supprimer les lignes complètes
def supprimer_lignes(blocs, blocs_couleurs):
    global score, niveau
    nouvelles_lignes = 0
    for y in range(len(blocs) - 1, -1, -1):
        if all(blocs[y]):
            del blocs[y]
            del blocs_couleurs[y]
            blocs.insert(0, [0 for _ in range(largeur // taille_bloc)])
            blocs_couleurs.insert(0, [noir for _ in range(largeur // taille_bloc)])
            nouvelles_lignes += 1
    if nouvelles_lignes > 0:
        score += scores_lignes[nouvelles_lignes] * niveau
        if score >= niveau * 1000:
            niveau += 1
    return nouvelles_lignes

# Fonction pour afficher le score et le niveau
def afficher_score_et_niveau():
    font = pygame.font.SysFont(None, 35)
    texte_score = font.render(f"Score: {score}", True, blanc)
    texte_niveau = font.render(f"Niveau: {niveau}", True, blanc)
    fenetre.blit(texte_score, (10, 10))
    fenetre.blit(texte_niveau, (10, 40))

# Initialiser la pièce actuelle
piece_actuelle = nouvelle_piece()
vitesse_chute = 500  # en millisecondes
derniere_chute = pygame.time.get_ticks()
blocs = [[0 for _ in range(largeur // taille_bloc)] for _ in range(hauteur // taille_bloc)]
blocs_couleurs = [[noir for _ in range(largeur // taille_bloc)] for _ in range(hauteur // taille_bloc)]

# Boucle principale du jeu
en_cours = True
while en_cours:
    fenetre.fill(noir)
    dessiner_piece(piece_actuelle, {'x': piece_actuelle['x'], 'y': piece_actuelle['y']})
    for y, ligne in enumerate(blocs):
        for x, bloc in enumerate(ligne):
            if bloc:
                pygame.draw.rect(fenetre, blocs_couleurs[y][x], (x * taille_bloc, y * taille_bloc, taille_bloc, taille_bloc), 0)
    afficher_score_et_niveau()
    pygame.display.flip()

    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False
        elif evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_LEFT:
                piece_actuelle['x'] -= 1
                if collision(piece_actuelle, {'x': piece_actuelle['x'], 'y': piece_actuelle['y']}, blocs):
                    piece_actuelle['x'] += 1
            elif evenement.key == pygame.K_RIGHT:
                piece_actuelle['x'] += 1
                if collision(piece_actuelle, {'x': piece_actuelle['x'], 'y': piece_actuelle['y']}, blocs):
                    piece_actuelle['x'] -= 1
            elif evenement.key == pygame.K_DOWN:
                piece_actuelle['y'] += 1
                if collision(piece_actuelle, {'x': piece_actuelle['x'], 'y': piece_actuelle['y']}, blocs):
                    piece_actuelle['y'] -= 1
            elif evenement.key == pygame.K_UP:
                piece_actuelle['rotation'] = (piece_actuelle['rotation'] + 1) % len(formes[piece_actuelle['forme']])
                if collision(piece_actuelle, {'x': piece_actuelle['x'], 'y': piece_actuelle['y']}, blocs):
                    piece_actuelle['rotation'] = (piece_actuelle['rotation'] - 1) % len(formes[piece_actuelle['forme']])

    # Faire tomber la pièce
    if pygame.time.get_ticks() - derniere_chute > vitesse_chute:
        piece_actuelle['y'] += 1
        derniere_chute = pygame.time.get_ticks()
        if collision(piece_actuelle, {'x': piece_actuelle['x'], 'y': piece_actuelle['y']}, blocs):
            piece_actuelle['y'] -= 1
            fusionner_piece(piece_actuelle, {'x': piece_actuelle['x'], 'y': piece_actuelle['y']}, blocs, blocs_couleurs)
            supprimer_lignes(blocs, blocs_couleurs)
            piece_actuelle = nouvelle_piece()
            if collision(piece_actuelle, {'x': piece_actuelle['x'], 'y': piece_actuelle['y']}, blocs):
                en_cours = False

# Quitter Pygame
pygame.quit()
