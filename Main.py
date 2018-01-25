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

# Import of the time's lib
import time

# Initialisation of pygame
pygame.init()

# Creation of the instance of the window
window = pygame.display.set_mode((w_window, w_window))

# Title of the game
pygame.display.set_caption(Game_title)

# Loading the backgound
Background = pygame.image.load("images/stone3.jpg").convert()

# Loading the sprite of the caracter
Chara = pygame.image.load("images/maggy2.png").convert_alpha()

# Apply the background in the window
window.blit(Background, (0, 0))

# Apply the caracter in the window
window.blit(Chara, (0, 0))

# Refresh the window the display the background and the character
pygame.display.flip()

# Create an instance of the Level
level = Level(levelGame)

# Creation of the character
maggy = MacGyver("images/maggy2.png", "images/maggy2.png",
                 "images/maggy2.png", "images/maggy2.png", level)

# State of the game. 1 = running, 0 = closed
Mainwhile = 1

# Set for de movements of the character
pygame.key.set_repeat(5, 5)

# Loading of the gameover's image
Gameover = pygame.image.load("images/gameove.png").convert_alpha()

# Loading of the Win's image
Win = pygame.image.load("images/win.jpg")

# Generation of the level
level.gen()

# Creation of the instance of items
ether = Ether("images/ether.png", level)
needle = Needle("images/needle.png", level)
tube = Tube("images/tube.png", level)

# Vars of items. When the character pick-up one of them, var pass to 1
Ethinv = 0
Needinv = 0
Tubinv = 0

# Font choosen for the txt ingame
police = pygame.font.SysFont("monospace", 15, bold=True)

# Txts about items
inventaire = police.render("Inventaire: ", 1, (255, 255, 255))
eth = police.render("Ether", 1, (255, 255, 255))
tub = police.render("Tube", 1, (255, 255, 255))
aig = police.render("Aiguille", 1, (255, 255, 255))

# Main loop of the game
while Mainwhile:

    # Refresh time
    pygame.time.Clock().tick(15)

    # Keys assignate to mov the character
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                Mainwhile = 0
            elif event.key == K_DOWN:
                maggy.move('down')
            elif event.key == K_UP:
                maggy.move('up')
            elif event.key == K_LEFT:
                maggy.move('left')
            elif event.key == K_RIGHT:
                maggy.move('right')

    window.blit(Background, (0, 0))
    window.blit(maggy.direction, (maggy.x, maggy.y))
    level.Show(window)

    # If item if was picked display it in the inventory at the top right of the window
    if Ethinv == 1:
        window.blit(eth, (350, 20))
        pygame.display.flip()
        pass
    elif Ethinv == 0:
        ether.display(window)

    if Needinv == 1:
        window.blit(aig, (350, 35))
        pygame.display.flip()
        pass
    elif Needinv == 0:
        needle.display(window)

    if Tubinv == 1:
        window.blit(tub, (350, 50))
        pygame.display.flip()
        pass
    elif Tubinv == 0:
        tube.display(window)

    # Display the "Inventaire" in the top right of the window
    window.blit(inventaire, (350, 5))
    pygame.display.flip()

    """ If Mac Gyver arrive at the end of maze and didn't collect one of the item,
        then the player loose """
    if level.structure[maggy.case_y][maggy.case_x] == 'a':
        if Ethinv == 0:
            window.blit(Gameover, (100, 100))
            pygame.display.flip()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    Mainwhile = 0
                elif event.key == K_ESCAPE:
                    Mainwhile = 0
                elif event.key == K_DOWN:
                    Mainwhile = 0
                elif event.key == K_UP:
                    Mainwhile = 0
                elif event.key == K_LEFT:
                    Mainwhile = 0
                elif event.key == K_RIGHT:
                    Mainwhile = 0

        if Needinv == 0:
            window.blit(Gameover, (100, 100))
            pygame.display.flip()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    Mainwhile = 0
                elif event.key == K_ESCAPE:
                    Mainwhile = 0
                elif event.key == K_DOWN:
                    Mainwhile = 0
                elif event.key == K_UP:
                    Mainwhile = 0
                elif event.key == K_LEFT:
                    Mainwhile = 0
                elif event.key == K_RIGHT:
                    Mainwhile = 0

        if Tubinv == 0:
            window.blit(Gameover, (100, 100))
            pygame.display.flip()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    Mainwhile = 0
                if event.key == K_ESCAPE:
                    Mainwhile = 0
                elif event.key == K_DOWN:
                    Mainwhile = 0
                elif event.key == K_UP:
                    Mainwhile = 0
                elif event.key == K_LEFT:
                    Mainwhile = 0
                elif event.key == K_RIGHT:
                    Mainwhile = 0

        # If the play collect every items at the end of maze then he Win
        if Ethinv == 1 and Needinv == 1 and Tubinv == 1:
            pygame.time.Clock().tick(3000)
            window.blit(Win, (100, 100))
            pygame.display.flip()
            if event.key == K_RETURN:
                Mainwhile = 0
            else:
                time.sleep(3)
                Mainwhile = 0

    """ If the position of the player is the same of one of the items,
    then increase the var correspunding """
    if level.structure[maggy.case_y][maggy.case_x] == "o1":
        Ethinv = 1

    if level.structure[maggy.case_y][maggy.case_x] == "o2":
        Needinv = 1

    if level.structure[maggy.case_y][maggy.case_x] == "o3":
        Tubinv = 1
