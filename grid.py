from tile import Tile


class Grid:
    def __init__(self, window, x, y, tileWidth, tileHeight):
        self.tiles = [
            [],
            []
        ]
        self.boats = [
            [],
            []
        ]
        self.selectedBoat = None
        self.window = window
        self.x = x
        self.y = y
        self.tileWidth = tileWidth
        self.tileHeight = tileHeight
        self.stage = 0
        self.turn = 0
        self.__generate__(0)
        self.__generate__(1)

    def __generate__(self, player):
        for x in range(self.x):
            if len(self.tiles[player]) - 1 < x: self.tiles[player].append([])
            for y in range(self.y):
                if len(self.tiles[player][x]) - 1 < y: self.tiles[player][x].append([])
                self.tiles[player][x][y] = Tile(self.window, x, y, self.tileWidth, self.tileHeight)

    def addBoat(self, player, boat):
        self.boats[player].append(boat)

