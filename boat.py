import pygame


class Boat:
    def __init__(self, window, image, x, y, tileWidth, tileHeight, width, height, direction):
        self.window = window
        self.imagePath = image
        self.x = x
        self.y = y
        self.tileWidth = tileWidth
        self.tileHeight = tileHeight
        self.width = width
        self.height = height
        self.direction = direction
        self.__draw__()

    def __draw__(self):
        # pygame.draw.rect(self.window, (102, 204, 255), (self.x * self.tileWidth - self.x + 6, self.y * self.tileHeight - self.y + 6, self.width * self.tileWidth - self.width + 1, self.height * self.tileHeight - self.height + 1), 1)
        # pygame.display.update()
        self.image = pygame.image.load(self.imagePath)
        self.image = pygame.transform.rotate(self.image, self.direction * 90)
        x = self.x * self.tileWidth - self.x + 6
        y = self.y * self.tileHeight - self.y + 6
        if self.direction == 1:
            y = y - (self.width - 1) * self.tileHeight + 4
        if self.direction == 2:
            x = x - (self.width - 1) * self.tileWidth + 4
        self.window.blit(self.image, (x, y))

    def move(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, direction):
        if direction > 3: direction = 0
        self.direction = direction
