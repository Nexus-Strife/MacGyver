# Class

import pygame
from pygame.locals import *
from constantesM import *
import random


# This class create the level
class Level:
    def __init__(self, file):
        self.file = file
        # Very important /!\ THE ARRAY MUST BE EMPTY /!\
        self.structure = []

    # Method that generate the level from the levelGame.txt
    def gen(self):
        # Open the file
        with open(self.file, "r") as file:
            structure_level = []
            # Reading the lines in file
            for line in file:
                line_of_level = []
                # Reading every letters in file
                for sprite in line:
                    # Ignoring the last sprite to continue with the next line
                    if sprite != '\n':
                        # Adding every letters to the array
                        line_of_level.append(sprite)
                # Adding every lines the the array
                structure_level.append(line_of_level)
            # Then the method save the entire structure of the level
            self.structure = structure_level

    # This method display the level into the window
    def Show(self, Window):

        # Load the img of the structure of the level
        Wall = pygame.image.load("images/mur.png").convert()
        Escape = pygame.image.load(garde).convert_alpha()

        # Read the entire structure
        num_ligne = 0
        for line in self.structure:
            # Read every line
            num_case = 0
            for sprite in line:
                # Calculate the real position of the sprite
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'm':  # m = Wall
                    Window.blit(Wall, (x, y))
                elif sprite == "a":  # a = Exit of the maze
                    Window.blit(Escape, (x, y))
                num_case += 1
            num_ligne += 1


# That class create the character
class MacGyver:

    def __init__(self, right, left, up, down, level):

        # Sprites of the character (need to get improve)
        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.up = pygame.image.load(up).convert_alpha()
        self.down = pygame.image.load(down).convert_alpha()

        # Initial position of the character
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

        # Initial position of Mac Gyver. Need to be improve with the sprite
        self.direction = self.right
        self.level = level

    # This method allow the player to move Mac Gyver
    def move(self, direction):

        # Move to the right
        if direction == 'right':
            # To not get out of the window
            if self.case_x < (nombre_sprite_cote - 1):
                # Check if the next iteration isn't a wall
                if self.level.structure[self.case_y][self.case_x + 1] != 'm':
                    # Move 1 square
                    self.case_x += 1
                    # Calculate the real position
                    self.x = self.case_x * taille_sprite
            # Display the right sprite in fonction of movement
            self.direction = self.right

        # Move to the left
        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * taille_sprite
            self.direction = self.left

        # Move to the top
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.up

        # Move to the bottom
        if direction == 'down':
            if self.case_y < (nombre_sprite_cote - 1):
                if self.level.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.down


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
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)

            # If the sprite is a freespace
            if self.level.structure[self.case_y][self.case_x] == '0':

                # then change it to a mark where the program gonna pop the item.
                self.level.structure[self.case_y][self.case_x] = "o1"

                # And quit the loop
                count += 1
                break
        return self.case_x, self.case_y

    # Method that display the item on the map
    def display(self, Window):

        # Load the sprite
        c_ether = pygame.image.load("images/ether.png").convert_alpha()

        # Display the item on screen
        Window.blit(c_ether, (self.x, self.y))


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
            self.case_x = random.randint(0,14)
            self.case_y = random.randint(0,14)
            if self.level.structure[self.case_y][self.case_x] == '0':
                self.level.structure[self.case_y][self.case_x] = "o2"
                count += 1
                break
        return self.case_x, self.case_y

    def display(self, Window):
        c_needle = pygame.image.load("images/needle.png").convert_alpha()
        Window.blit(c_needle, (self.x, self.y))


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
            self.case_x = random.randint(0,14)
            self.case_y = random.randint(0,14)
            if self.level.structure[self.case_y][self.case_x] == '0':
                self.level.structure[self.case_y][self.case_x] = "o3"
                count += 1
                break
        return self.case_x, self.case_y

    def display(self, Window):
        c_tube = pygame.image.load("images/tube.png").convert_alpha()
        Window.blit(c_tube, (self.x, self.y))
