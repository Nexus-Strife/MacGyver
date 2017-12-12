"""
P3: Réalisation d'un "escape game" avec pour personnage principal 
Mac Gyver. Jeu composé d'un seul level

Réalisé par D.B.
"""

# Import de pygame 
import pygame
from pygame.locals import *

# Import du fichier des variables constantes
from constantesM import *

# Import du fichier des Classes du jeu
from Classes import *

# Initialisation de pygame
pygame.init()

# Affichage de la fenêtre 
window = pygame.display.set_mode((cote_fenetre, cote_fenetre))

# Titrage de la fenêtre en utilisant la variable "Titre_jeu" contenu dans le fichier de constantes
pygame.display.set_caption(Titre_jeu)

# Chargement du fond
background = pygame.image.load("images/stone3.jpg").convert()

# Chargement de l'image personnage
Perso = pygame.image.load("images/maggy2.png").convert_alpha()


# Collage du fond dans la fenêtre
window.blit(background, (0,0))

# Collage du personnage dans la fenêtre
window.blit(Perso, (0,0))

# Rafraichissement 
pygame.display.flip()

# Bricolage obscure de variable 
level = Level(levelGame)

# Création du personnage /!\ Manque de sprite, à voir plus tard /!\
maggy = Personnage("images/maggy2.png", "images/maggy2.png", "images/maggy2.png", "images/maggy2.png", level)

# Etat du jeu. 1 = ouvert, 0 = fermeture 
continuer = 1

# Glissage sur le terrain ( deplacement )
pygame.key.set_repeat(5, 5)



# Boucle principale du jeu
while continuer:

	# Temps entre chaque rafraichissement 
	pygame.time.Clock().tick(5)
	# Controles du personnage	
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				continuer = 0
			elif event.key == K_DOWN:
				maggy.deplacer('bas')
			elif event.key == K_UP:
				maggy.deplacer('haut')
			elif event.key == K_LEFT:
				maggy.deplacer('gauche')
			elif event.key == K_RIGHT:
				maggy.deplacer('droite')
				
	level.generer()
	level.afficher(window)
	window.blit(background, (0,0))
	level.afficher(window)
	window.blit(maggy.direction, (maggy.x, maggy.y))
	pygame.display.flip()
	
	# Si Mac Gyver arrive jusqu'à Murloc, fin du jeu.
	if level.structure[maggy.case_y][maggy.case_x] == 'a':
			continuer = 0