# Class

import pygame
from pygame.locals import *
from constantesM import *
import random


# This class create the level
class Level:
    def __init__(self, fichier):
        self.fichier = fichier
        # Very important /!\ THE ARRAY MUST BE EMPTY /!\
        self.structure = []

    # Method that generate the level from the levelGame.txt
    def gen(self):
        # Open the file
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            # Reading the lines in file
            for ligne in fichier:
                ligne_niveau = []
                # Reading every letters in file
                for sprite in ligne:
                    # Ignoring the last sprite to continue with the next line
                    if sprite != '\n':
                        # Adding every letters to the array
                        ligne_niveau.append(sprite)
                # Adding every lines the the array
                structure_niveau.append(ligne_niveau)
            # Then the method save the entire structure of the level
            self.structure = structure_niveau

    # This method display the level into the window
    def afficher(self, fenetre):

        # Load the img of the structure of the level
        mur = pygame.image.load("images/mur.png").convert()
        arrivee = pygame.image.load(garde).convert_alpha()

        # Read the entire structure
        num_ligne = 0
        for ligne in self.structure:
            # Read every line
            num_case = 0
            for sprite in ligne:
                # Calculate the real position of the sprite
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'm':  # m = Wall
                    fenetre.blit(mur, (x, y))
                elif sprite == "a":  # a = Exit of the maze
                    fenetre.blit(arrivee, (x, y))
                num_case += 1
            num_ligne += 1


# That class create the character
class MacGyver:

    def __init__(self, droite, gauche, haut, bas, level):

        # Sprites of the character (need to get improve)
        self.droite = pygame.image.load(droite).convert_alpha()
        self.gauche = pygame.image.load(gauche).convert_alpha()
        self.haut = pygame.image.load(haut).convert_alpha()
        self.bas = pygame.image.load(bas).convert_alpha()

        # Initial position of the character
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

        # Initial position of Mac Gyver. Need to be improve with the sprite
        self.direction = self.droite
        self.level = level

    # This method allow the player to move Mac Gyver
    def deplacer(self, direction):

        # Move to the right
        if direction == 'droite':
            # To not get out of the window
            if self.case_x < (nombre_sprite_cote - 1):
                # Check if the next iteration isn't a wall
                if self.level.structure[self.case_y][self.case_x + 1] != 'm':
                    # Move 1 square
                    self.case_x += 1
                    # Calculate the real position
                    self.x = self.case_x * taille_sprite
            # Display the right sprite in fonction of movement
            self.direction = self.droite

        # Move to the left
        if direction == 'gauche':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * taille_sprite
            self.direction = self.gauche

        # Move to the top
        if direction == 'haut':
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.haut

        # Move to the bottom
        if direction == 'bas':
            if self.case_y < (nombre_sprite_cote - 1):
                if self.level.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.bas


# Class to create one of the items
class Ether:

    def __init__(self, obj, level):

        # Load the sprite of the item
        self.obj = pygame.image.load(obj).convert_alpha

        # Initial settings for the item
        self.level = level
        self.case_x, self.case_y = self.randpos()
        self.x = self.case_x * taille_sprite
        self.y = self.case_y * taille_sprite

    # Method that calculate a random pos to pop the item
    def randpos(self):
        count_max = 1
        count = 0

        # A loop to check of the position picked by random is a freespace
        while count < count_max:
            self.case_x = int(random.randint(0, 14))
            self.case_y = int(random.randint(0, 14))

            # If the sprite is a freespace
            if self.level.structure[self.case_y][self.case_x] == '0':

                # then change it to a mark where the program gonna pop the item.
                self.level.structure[self.case_y][self.case_x] = "o1"

                # And quit the loop
                count += 1
                break
        return self.case_x, self.case_y

    # Method that display the item on the map
    def display(self, fenetre):

        # Load the sprite
        c_ether = pygame.image.load("images/ether.png").convert_alpha()

        # Display the item on screen
        fenetre.blit(c_ether, (self.x, self.y))


# Class to create one of the items
class Needle:
    def __init__(self, obj, level):
        self.obj = pygame.image.load(obj).convert_alpha
        self.level = level
        self.case_x, self.case_y = self.randpos()
        self.x = self.case_x * taille_sprite
        self.y = self.case_y * taille_sprite

    def randpos(self):
        count_max = 1
        count = 0
        while count < count_max:
            self.case_x = int(random.randint(0, 14))
            self.case_y = int(random.randint(0, 14))
            if self.level.structure[self.case_y][self.case_x] == '0':
                self.level.structure[self.case_y][self.case_x] = "o2"
                count += 1
                break
        return self.case_x, self.case_y

    def display(self, fenetre):
        c_needle = pygame.image.load("images/needle.png").convert_alpha()
        fenetre.blit(c_needle, (self.x, self.y))


# Class to create one of the items
class Tube:
    def __init__(self, obj, level):
        self.obj = pygame.image.load(obj).convert_alpha
        self.level = level
        self.case_x, self.case_y = self.randpos()
        self.x = self.case_x * taille_sprite
        self.y = self.case_y * taille_sprite

    def randpos(self):
        count_max = 1
        count = 0
        while count < count_max:
            self.case_x = int(random.randint(0, 14))
            self.case_y = int(random.randint(0, 14))
            if self.level.structure[self.case_y][self.case_x] == '0':
                self.level.structure[self.case_y][self.case_x] = "o3"
                count += 1
                break
        return self.case_x, self.case_y

    def display(self, fenetre):
        c_tube = pygame.image.load("images/tube.png").convert_alpha()
        fenetre.blit(c_tube, (self.x, self.y))
