import pygame
from grid import Grid


class Main:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((480, 480))
        pygame.display.set_caption("Bataille Navale")
        self.grid = Grid(self.window, 10, 10)
        self.running = True
        self.__loop__()
        print("Main")

    def __loop__(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for row in self.grid.tiles:
                        for tile in row:
                            tile.click()
                if event.type == pygame.QUIT:
                    self.running = False


game = Main()
