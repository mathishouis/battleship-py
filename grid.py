from tile import Tile


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

    def tiles(self):
        return self.tiles
