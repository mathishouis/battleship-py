import pygame
import random


class Tile:
    def __init__(self, window, x, y):
        self.window = window
        self.x = x
        self.y = y
        self.width = 40
        self.height = 20
        print("cc")
        self.__draw__()

    def __draw__(self):
        pygame.draw.rect(self.window, (102, 204, 0), (self.x * self.width - self.x + 6, self.y * self.height - self.y + 6, self.width, self.height), 1)
        pygame.display.update()

    def click(self):
        if self.x * self.width + self.width > pygame.mouse.get_pos()[0] > self.x * self.width and self.y * self.height + self.height > pygame.mouse.get_pos()[1] > self.y * self.height:
            print("CLICK", self.x, self.y)
