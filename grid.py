from tile import Tile
from boat import Boat


class Grid:
    def __init__(self, window, x, y):
        self.tiles = []
        self.window = window
        self.x = x
        self.y = y
        self.__generate__()

    def __generate__(self):
        for x in range(self.x):
            if len(self.tiles) - 1 < x: self.tiles.append([])
            for y in range(self.y):
                if len(self.tiles[x]) - 1 < y: self.tiles[x].append([])
                self.tiles[x][y] = Tile(self.window, x, y)

        print(self.tiles)
        Boat(self.window, "./assets/boat_5.png", 2, 3, 5, 1, 0)
        Boat(self.window, "./assets/boat_4.png", 2, 4, 4, 1, 0)
        Boat(self.window, "./assets/boat_3.png", 2, 5, 3, 1, 0)
        Boat(self.window, "./assets/boat_2.png", 2, 6, 2, 1, 0)

    def tiles(self):
        return self.tiles
