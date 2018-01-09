"""
P3: Realisation d'un "escape game" avec pour personnage principal
Mac Gyver. Jeu compose d'un seul level
Réalisé par D.B.
"""

# Import of pygame
import pygame

from pygame.locals import *

# Import of constants vars
from constantesM import *

# Import of classes
from Classes import *

# Initialisation of pygame
pygame.init()

# Creation of the instance of the window
window = pygame.display.set_mode((cote_fenetre, cote_fenetre))

# Title of the game
pygame.display.set_caption(Titre_jeu)

# Loading the backgound
background = pygame.image.load("images/stone3.jpg").convert()

# Loading the img of the caracter
Perso = pygame.image.load("images/maggy2.png").convert_alpha()

# Apply the background in the window
window.blit(background, (0, 0))

# Apply the caracter in the window
window.blit(Perso, (0, 0))

# Refresh the window the display the background and the character
pygame.display.flip()

# Create an instance of the Level
level = Level(levelGame)

# Creation of the character
maggy = Personnage("images/maggy2.png", "images/maggy2.png",
                   "images/maggy2.png", "images/maggy2.png", level)

# State of the game. 1 = running, 0 = closed
continuer = 1

# Set for de movements of the character
pygame.key.set_repeat(5, 5)

# Loading of the gameover's image
gameover = pygame.image.load("images/gameove.png").convert_alpha()

# Loading of the win's image
win = pygame.image.load("images/win.jpg")

# Generation of the level
level.generer()

# Creation of the instance of items
ether = Ether("images/ether.png", level)
needle = Needle("images/needle.png", level)
tube = Tube("images/tube.png", level)

# Vars of items. When the character pick-up one of them, var pass to 1
obj1recup = 0
obj2recup = 0
obj3recup = 0

# Var witch count how much item the character picked-up
nbrobj = 0

# Font choosen for the txt ingame
police = pygame.font.SysFont("monospace", 15, bold=True)

# Txts about items
inventaire = police.render("Inventaire: ", 1, (255, 255, 255))
eth = police.render("Ether", 1, (255, 255, 255))
tub = police.render("Tube", 1, (255, 255, 255))
aig = police.render("Aiguille", 1, (255, 255, 255))

# Main loop of the game
while continuer:

    # Refresh time
    pygame.time.Clock().tick(15)

    # Keys assignate to mov the character
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

    window.blit(background, (0, 0))
    window.blit(maggy.direction, (maggy.x, maggy.y))
    level.afficher(window)

    # If item if was picked display it in the inventory at the top right of the window
    if obj1recup == 1:
        window.blit(eth, (350, 20))
        pygame.display.flip()
        pass
    elif obj1recup == 0:
        ether.display(window)

    if obj2recup == 1:
        window.blit(aig, (350, 35))
        pygame.display.flip()
        pass
    elif obj2recup == 0:
        needle.display(window)

    if obj3recup == 1:
        window.blit(tub, (350, 50))
        pygame.display.flip()
        pass
    elif obj3recup == 0:
        tube.display(window)

    # Display the "Inventaire" in the top right of the window
    window.blit(inventaire, (350, 5))
    pygame.display.flip()

    """ If Mac Gyver arrive at the end of maze and didn't collect one of the item,
        then the player loose """
    if level.structure[maggy.case_y][maggy.case_x] == 'a':
        if obj1recup == 0:
            window.blit(gameover, (100, 100))
            pygame.display.flip()
            if event.key == K_RETURN:
                continuer = 0
        if obj2recup == 0:
            window.blit(gameover, (100, 100))
            pygame.display.flip()
            if event.key == K_RETURN:
                continuer = 0
        if obj3recup == 0:
            window.blit(gameover, (100, 100))
            pygame.display.flip()
            if event.key == K_RETURN:
                continuer = 0

        # If the play collect every items at the end of maze then he win
        if obj1recup == 1 and obj2recup == 1 and obj3recup == 1:
            pygame.time.Clock().tick(3000)
            window.blit(win, (100, 100))
            pygame.display.flip()
            if event.key == K_RETURN:
                continuer = 0

    """ If the position of the player is the same of one of the items,
    then increase the var correspunding """
    if level.structure[maggy.case_y][maggy.case_x] == "o1":
        obj1recup = 1

    if level.structure[maggy.case_y][maggy.case_x] == "o2":
        obj2recup = 1

    if level.structure[maggy.case_y][maggy.case_x] == "o3":
        obj3recup = 1
