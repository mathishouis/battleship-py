import pygame
from grid import Grid
from boat import Boat


class Main:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((203, 203))
        pygame.display.set_caption("Bataille Navale")
        self.grid = Grid(self.window, 10, 10)
        self.grid.addBoat(Boat(self.window, "./assets/boat_5.png", 2, 3, 5, 1, 0))
        self.grid.addBoat(Boat(self.window, "./assets/boat_4.png", 2, 4, 4, 1, 0))
        self.grid.addBoat(Boat(self.window, "./assets/boat_3.png", 2, 5, 3, 1, 0))
        self.grid.addBoat(Boat(self.window, "./assets/boat_2.png", 2, 6, 2, 1, 0))
        self.running = True
        self.__loop__()
        print("Main")

    def __loop__(self):
        while self.running:
            pygame.time.delay(1)

            # Event Management

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for row in self.grid.tiles:
                        for tile in row:
                            tile.click()
                if event.type == pygame.MOUSEMOTION:
                    for row in self.grid.tiles:
                        for tile in row:
                            if tile.mouseover():
                                # Movement for direction 0
                                if self.grid.x - self.grid.boats[0].width >= tile.x and self.grid.boats[0].direction == 0:
                                    self.grid.boats[0].move(tile.x, tile.y)
                                elif self.grid.boats[0].direction == 0:
                                    self.grid.boats[0].move(self.grid.x - self.grid.boats[0].width, tile.y)
                                # Movement for direction 1
                                if self.grid.boats[0].width - 1 <= tile.y and self.grid.boats[0].direction == 1:
                                    self.grid.boats[0].move(tile.x, tile.y)
                                elif self.grid.boats[0].direction == 1:
                                    self.grid.boats[0].move(tile.x, self.grid.boats[0].width - 1)
                                # Movement for direction 2
                                if self.grid.boats[0].width - 1 <= tile.x and self.grid.boats[0].direction == 2:
                                    self.grid.boats[0].move(tile.x, tile.y)
                                elif self.grid.boats[0].direction == 2:
                                    self.grid.boats[0].move(self.grid.boats[0].width - 1, tile.y)
                                # Movement for direction 3
                                if self.grid.x - self.grid.boats[0].width >= tile.y and self.grid.boats[0].direction == 3:
                                    self.grid.boats[0].move(tile.x, tile.y)
                                elif self.grid.boats[0].direction == 3:
                                    self.grid.boats[0].move(tile.x, self.grid.y - self.grid.boats[0].width)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        print("key")
                        self.grid.boats[0].rotate(self.grid.boats[0].direction + 1)
                if event.type == pygame.QUIT:
                    self.running = False

            self.window.fill(0)

            # Draw

            for row in self.grid.tiles:
                for tile in row:
                    tile.__draw__()

            for boat in self.grid.boats:
                boat.__draw__()

            for row in self.grid.tiles:
                for tile in row:
                    tile.__drawState__()

            pygame.display.flip()



game = Main()
