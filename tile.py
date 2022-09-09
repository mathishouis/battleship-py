import pygame
import random


class Tile:
    def __init__(self, window, x, y):
        self.window = window
        self.x = x
        self.y = y
        self.tileWidth = 20
        self.tileHeight = 20
        print("cc")
        self.__draw__()

    def __draw__(self):
        pygame.draw.rect(self.window, (102, 204, 0), (self.x * self.tileWidth - self.x + 6, self.y * self.tileHeight - self.y + 6, self.tileWidth, self.tileHeight), 1)
        pygame.display.update()

    def __mouseover__(self):
        return 6 + self.x * self.tileWidth + self.tileWidth - self.x > pygame.mouse.get_pos()[0] > 6 + self.x * self.tileWidth - self.x and 6 + self.y * self.tileHeight + self.tileHeight - self.y > pygame.mouse.get_pos()[1] > 6 + self.y * self.tileHeight - self.y

    def click(self):
        if self.__mouseover__():
            rand = random.randint(0, 2)
            if rand == 0:
                checkmark = pygame.image.load("./assets/checkmark.png")
            if rand == 1:
                checkmark = pygame.image.load("./assets/explosion_1.png")
            if rand == 2:
                checkmark = pygame.image.load("./assets/explosion_2.png")

            self.window.blit(checkmark, (self.x * self.tileWidth - self.x + 6, self.y * self.tileHeight - self.y + 6))
            pygame.display.flip()
            print("CLICK", self.x, self.y)

    def mouseover(self):
        if self.__mouseover__():
            print("MOVE", self.x, self.y)
