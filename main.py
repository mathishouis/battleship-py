import pygame
from grid import Grid
from boat import Boat


class Main:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((403, 423))
        pygame.display.set_caption("Bataille Navale")
        self.font = pygame.font.Font("./assets/Volter_Goldfish.ttf", 9)

        self.placeableBoats = [
            Boat(self.window, "./assets/boat_2.png", 100, 100, 2, 1, 0),
            Boat(self.window, "./assets/boat_3.png", 100, 100, 3, 1, 0),
            Boat(self.window, "./assets/boat_3.png", 100, 100, 3, 1, 0),
            Boat(self.window, "./assets/boat_4.png", 100, 100, 4, 1, 0),
            Boat(self.window, "./assets/boat_5.png", 100, 100, 5, 1, 0)
        ]
        self.grid = Grid(self.window, 10, 10)
        self.running = True
        self.__loop__()
        print("Main")


    def __loop__(self):
        while self.running:
            pygame.time.delay(1)

            # Event Management

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.grid.stage == 0 and self.grid.selectedBoat != None:

                        for row in self.grid.tiles:
                            for tile in row:
                                if self.grid.selectedBoat != None and self.grid.selectedBoat.x == tile.x and self.grid.selectedBoat.y == tile.y:

                                    self.grid.addBoat(self.grid.selectedBoat)

                                    if len(self.grid.boats) == len(self.placeableBoats):
                                        self.grid.selectedBoat = None
                                        if self.grid.turn == 0:
                                            self.grid.turn = 1
                                        else:
                                            self.grid.turn = 0
                                            self.grid.stage = 1
                                        print("x")
                                    else:
                                        print(len(self.grid.boats))
                                        self.grid.selectedBoat = self.placeableBoats[len(self.grid.boats)]
                                        print("ccffff")
                                    break

                                else:
                                    tile.click()
                if event.type == pygame.MOUSEMOTION:
                    for row in self.grid.tiles:
                        for tile in row:
                            if tile.mouseover():
                                if self.grid.stage == 0:
                                    if self.grid.selectedBoat == None:
                                        self.grid.selectedBoat = self.placeableBoats[0]
                                    else:
                                        # Movement for direction 0
                                        if self.grid.x - self.grid.selectedBoat.width >= tile.x and self.grid.selectedBoat.direction == 0:
                                            self.grid.selectedBoat.move(tile.x, tile.y)
                                        elif self.grid.selectedBoat.direction == 0:
                                            self.grid.selectedBoat.move(self.grid.x - self.grid.selectedBoat.width, tile.y)

                                        # Movement for direction 1
                                        if self.grid.selectedBoat.width - 1 <= tile.y and self.grid.selectedBoat.direction == 1:
                                            self.grid.selectedBoat.move(tile.x, tile.y)
                                        elif self.grid.selectedBoat.direction == 1:
                                            self.grid.selectedBoat.move(tile.x, self.grid.selectedBoat.width - 1)

                                        # Movement for direction 2
                                        if self.grid.selectedBoat.width - 1 <= tile.x and self.grid.selectedBoat.direction == 2:
                                            self.grid.selectedBoat.move(tile.x, tile.y)
                                        elif self.grid.selectedBoat.direction == 2:
                                            self.grid.selectedBoat.move(self.grid.selectedBoat.width - 1, tile.y)

                                        # Movement for direction 3
                                        if self.grid.x - self.grid.selectedBoat.width >= tile.y and self.grid.selectedBoat.direction == 3:
                                            self.grid.selectedBoat.move(tile.x, tile.y)
                                        elif self.grid.selectedBoat.direction == 3:
                                            self.grid.selectedBoat.move(tile.x, self.grid.y - self.grid.selectedBoat.width)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        print("key")
                        self.grid.selectedBoat.rotate(self.grid.selectedBoat.direction + 1)
                if event.type == pygame.QUIT:
                    self.running = False

            self.window.fill(0)

            # Draw

            msg = self.font.render("Joueur 1, veuillez placer vos bateaux", True, (0, 204, 0))
            self.window.blit(msg, (9, 405))

            for row in self.grid.tiles:
                for tile in row:
                    tile.__draw__()

            for boat in self.grid.boats:
                boat.__draw__()

            if self.grid.selectedBoat != None:
                self.grid.selectedBoat.__draw__()

            for row in self.grid.tiles:
                for tile in row:
                    tile.__drawState__()

            pygame.display.flip()


game = Main()
