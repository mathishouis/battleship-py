from tile import Tile

class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__draw__()
        
    def __draw__(self):
        self.tiles = []
        for x in range(self.x):
            if len(self.tiles) < x: tiles[x] = []
            for y in range(self.y):
                if len(self.tiles[x]) < y: tiles[x][y] = []
                tiles[x][y] = "cc"
                