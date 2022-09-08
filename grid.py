from tile import Tile

class Grid:
    def __init__(self, x, y):
        self.tiles = []
        self.x = x
        self.y = y
        self.__draw__()
        
    def __draw__(self):
        for x in range(self.x):
            if len(self.tiles) - 1 < x: self.tiles.append([])
            for y in range(self.y):
                if len(self.tiles[x]) - 1 < y: self.tiles[x].append([])
                self.tiles[x][y] = Tile(x, y)

        print(self.tiles)
                