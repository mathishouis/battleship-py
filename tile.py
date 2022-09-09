import pygame
import random


class Tile:
    def __init__(self, window, x, y):
        self.window = window
        self.x = x
        self.y = y
        self.tileWidth = 20
        self.tileHeight = 20
        self.state = 0
        print("cc")
        self.__draw__()

    def __draw__(self):
        pygame.draw.rect(self.window, (102, 204, 0), (self.x * self.tileWidth - self.x + 6, self.y * self.tileHeight - self.y + 6, self.tileWidth, self.tileHeight), 1)

    def __drawState__(self):
        if self.state == 1:
            checkmark = pygame.image.load("./assets/checkmark.png")
            self.window.blit(checkmark, (self.x * self.tileWidth - self.x + 6, self.y * self.tileHeight - self.y + 6))
        if self.state == 2:
            checkmark = pygame.image.load("./assets/explosion_1.png")
            self.window.blit(checkmark, (self.x * self.tileWidth - self.x + 6, self.y * self.tileHeight - self.y + 6))

        if self.state == 3:
            checkmark = pygame.image.load("./assets/explosion_2.png")
            self.window.blit(checkmark, (self.x * self.tileWidth - self.x + 6, self.y * self.tileHeight - self.y + 6))

    def mouseover(self):
        return 6 + self.x * self.tileWidth + self.tileWidth - self.x > pygame.mouse.get_pos()[0] > 6 + self.x * self.tileWidth - self.x and 6 + self.y * self.tileHeight + self.tileHeight - self.y > pygame.mouse.get_pos()[1] > 6 + self.y * self.tileHeight - self.y

    def click(self):
        if self.mouseover():
            rand = random.randint(1, 3)
            self.state = rand
            print("CLICK", self.x, self.y)
