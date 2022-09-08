import pygame


class Boat:
    def __init__(self, window, image, x, y, width, height, direction):
        self.window = window
        self.image = image
        self.x = x
        self.y = y
        self.tileWidth = 20
        self.tileHeight = 20
        self.width = width
        self.height = height
        self.direction = direction
        self.__draw__()

    def __draw__(self):
        pygame.draw.rect(self.window, (102, 204, 255), (self.x * self.tileWidth - self.x + 6, self.y * self.tileHeight - self.y + 6, self.width * self.tileWidth - self.width + 1, self.height * self.tileHeight - self.height + 1), 1)
        pygame.display.update()
        boat = pygame.image.load(self.image)
        self.window.blit(boat, (self.x * self.tileWidth - self.x + 6, self.y * self.tileHeight - self.y + 6))
        pygame.display.flip()
