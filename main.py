import pygame
from grid import Grid
from boat import Boat


class Main:
    def __init__(self):
        pygame.init()                                                          # Initialise pygame
        self.width = 10 # Largeur de la grille
        self.height = 10 # Hauteur de la grille
        self.tileWidth = 40 # Largeur des cases
        self.tileHeight = 40 # Hauteur des cases
        self.window = pygame.display.set_mode((self.width * self.tileWidth + 3, self.height * self.tileHeight + 23))                      # Création de la fenêtre
        pygame.display.set_caption("Bataille Navale")                          # Change le titre de la fenêtre
        self.font = pygame.font.Font("./assets/Volter_Goldfish.ttf", 9)        # Change la police d'écriture
        self.message = "Joueur 1, veuillez placer vos bateaux"                 # Texte qui sera affiché en bas de la fenêtre (indication joueur)
        self.placeableBoats = [                                                # Tableau contenant tous les bateaux qui peuvent être placé en début de partie
            Boat(self.window, "./assets/boat_2.png", 100, 100, self.tileWidth, self.tileHeight, 2, 1, 0),
            Boat(self.window, "./assets/boat_3.png", 100, 100, self.tileWidth, self.tileHeight, 3, 1, 0),
            Boat(self.window, "./assets/boat_3.png", 100, 100, self.tileWidth, self.tileHeight, 3, 1, 0),
            Boat(self.window, "./assets/boat_4.png", 100, 100, self.tileWidth, self.tileHeight, 4, 1, 0),
            Boat(self.window, "./assets/boat_5.png", 100, 100, self.tileWidth, self.tileHeight, 5, 1, 0)
        ]
        self.grid = Grid(self.window, self.width, self.height, self.tileWidth, self.tileHeight)                                  # Création de la grille de la bataille navale
        self.running = True                                                    #
        self.__loop__()                                                        # Démarrage de la boucle de rendu


    def __loop__(self):
        delay = False
        while self.running:
            pygame.time.delay(1)

            # Gestion des victoires
            if self.grid.stage == 1:
                touchedCount = 0
                tileBoatCount = 0

                for boat in self.grid.boats[1 - self.grid.turn]:
                    tileBoatCount += boat.width * boat.height

                for row in self.grid.tiles[1 - self.grid.turn]:
                    for tile in row:
                        if tile.state == 2:
                            touchedCount += 1
                if touchedCount == tileBoatCount:
                    self.grid.stage = 2
                    self.message = "Victoire du Joueur " + str(1 - self.grid.turn + 1)
            
            # Gestion des interactions
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:                                                                                      # Si le joueur clique sur la fenêtre
                    if self.grid.stage == 0 and self.grid.selectedBoat != None:                                                               # Vérifie si l'état de la partie est encore au placement des bateaux et si le bateau sélectionné n'est pas nul
           
                        for row in self.grid.tiles[self.grid.turn]:
                            for tile in row:
                                if self.grid.selectedBoat != None and self.grid.selectedBoat.x == tile.x and self.grid.selectedBoat.y == tile.y:                                 # Vérifie pour toutes les cases si leur position correspond à celle du bateau en cours de placement
                                    self.grid.addBoat(self.grid.turn, self.grid.selectedBoat)                                                 # Place le bateau sur la grille

                                    if len(self.grid.boats[self.grid.turn]) == len(self.placeableBoats):                                      # Si tous les bateaux placeables ont été posés
                                        self.grid.selectedBoat = None                                                                         # Alors on met le bateau sélectionné en nul
                                        if self.grid.turn == 0:                                                                               # Si c'était au tour du joueur 1 alors c'est désormais au tour du joueur 2 de placer ses bateaux
                                            self.message = "Joueur 2, veuillez placer vos bateaux"                                            # Change le texte qui sera affiché en bas de la fenêtre (indication joueur)
                                            self.placeableBoats = [                                                # Réinitialise les bateaux placeables
                                                Boat(self.window, "./assets/boat_2.png", 100, 100, self.tileWidth, self.tileHeight, 2, 1, 0),
                                                Boat(self.window, "./assets/boat_3.png", 100, 100, self.tileWidth, self.tileHeight, 3, 1, 0),
                                                Boat(self.window, "./assets/boat_3.png", 100, 100, self.tileWidth, self.tileHeight, 3, 1, 0),
                                                Boat(self.window, "./assets/boat_4.png", 100, 100, self.tileWidth, self.tileHeight, 4, 1, 0),
                                                Boat(self.window, "./assets/boat_5.png", 100, 100, self.tileWidth, self.tileHeight, 5, 1, 0)
                                            ]
                                            self.grid.turn = 1                                                                                # Au tour du joueur 2
                                        else:
                                            self.grid.turn = 0                                                                                # Au tour du joueur 1
                                            self.grid.stage = 1                                                                               # Fin du placement des bateaux, début de la partie
                                            self.message = "Joueur 1, veuillez bombarder une case"                                            # Change le texte qui sera affiché en bas de la fenêtre (indication joueur)
                                    else:
                                        self.grid.selectedBoat = self.placeableBoats[len(self.grid.boats[self.grid.turn])]                    # Sélectionne le prochain bateau à placer
                                    break

                    elif self.grid.stage == 1:                                                                                                # Sinon, si la partie est lancée
                        for row in self.grid.tiles[self.grid.turn]:
                            for tile in row:
                                if tile.mouseover() and tile.state == 0:                                                                      # Pour chaque cases de la grille on vérifie si la souris est dessus et si l'état de la case est à 0
                                    touched = False                                                                                           # Initialisation de la variable
                                    for boat in self.grid.boats[1 - self.grid.turn]:                                                                       # On vérifie si un la case est positionnée au niveau d'un bateau
                                        if tile.x >= boat.x and tile.x < boat.x + boat.width and tile.y == boat.y and boat.direction == 0:    # Vérification pour les bateaux avec une direction égale à 0
                                            touched = True
                                        elif tile.y <= boat.y and tile.y > boat.y - boat.width and tile.x == boat.x and boat.direction == 1:  # Vérification pour les bateaux avec une direction égale à 1
                                            touched = True
                                        elif tile.x <= boat.x and tile.x > boat.x - boat.width and tile.y == boat.y and boat.direction == 2:  # Vérification pour les bateaux avec une direction égale à 2
                                            touched = True
                                        elif tile.y >= boat.y and tile.y < boat.y + boat.width and tile.x == boat.x and boat.direction == 3:  # Vérification pour les bateaux avec une direction égale à 3
                                            touched = True
                                    if touched:                                                         # Si un bateau est sur la case, alors mettre l'état de la case à 2 (touché)
                                        tile.state = 2
                                    else:
                                        tile.state = 1                                                  # Sinon on met l'état de la case à 1 (loupé)

                                    delay = True
                        
                                    
                                    if self.grid.turn == 0:                                             # Au tour de l'autre joueur
                                        self.grid.turn = 1
                                    else:
                                        self.grid.turn = 0

                if event.type == pygame.MOUSEMOTION:                                                   # Si la souris est en mouvement sur la fenêtre
                    for row in self.grid.tiles[self.grid.turn]:
                        for tile in row:
                            if tile.mouseover():                                                       # Pour chaque case de la grille, vérifie si la souris est dessus
                                if self.grid.stage == 0:                                               # Vérifie si le placement des bateaux est toujours en cours
                                    if self.grid.selectedBoat == None:                                 # Si il n'y a pas de bateau en cours de placement
                                        self.grid.selectedBoat = self.placeableBoats[0]                # Alors on sélectionne le premier de la liste des bateaux placeable
                                    else:
                                        # Gestion des mouvements de la prévisualitation du bateau pour la direction 0
                                        if self.grid.x - self.grid.selectedBoat.width >= tile.x and self.grid.selectedBoat.direction == 0: # Vérifie si le bateau ne sors pas de la grille
                                            self.grid.selectedBoat.move(tile.x, tile.y)
                                        elif self.grid.selectedBoat.direction == 0:
                                            self.grid.selectedBoat.move(self.grid.x - self.grid.selectedBoat.width, tile.y)                # S'il sors, alors le placer à l'extrémité

                                        # Gestion des mouvements de la prévisualitation du bateau pour la direction 1
                                        if self.grid.selectedBoat.width - 1 <= tile.y and self.grid.selectedBoat.direction == 1:           # Vérifie si le bateau ne sors pas de la grille
                                            self.grid.selectedBoat.move(tile.x, tile.y)
                                        elif self.grid.selectedBoat.direction == 1:
                                            self.grid.selectedBoat.move(tile.x, self.grid.selectedBoat.width - 1)                          # S'il sors, alors le placer à l'extrémité

                                        # Gestion des mouvements de la prévisualitation du bateau pour la direction 2
                                        if self.grid.selectedBoat.width - 1 <= tile.x and self.grid.selectedBoat.direction == 2:           # Vérifie si le bateau ne sors pas de la grille
                                            self.grid.selectedBoat.move(tile.x, tile.y)
                                        elif self.grid.selectedBoat.direction == 2:
                                            self.grid.selectedBoat.move(self.grid.selectedBoat.width - 1, tile.y)                          # S'il sors, alors le placer à l'extrémité

                                        # Gestion des mouvements de la prévisualitation du bateau pour la direction 3
                                        if self.grid.x - self.grid.selectedBoat.width >= tile.y and self.grid.selectedBoat.direction == 3: # Vérifie si le bateau ne sors pas de la grille
                                            self.grid.selectedBoat.move(tile.x, tile.y)
                                        elif self.grid.selectedBoat.direction == 3:
                                            self.grid.selectedBoat.move(tile.x, self.grid.y - self.grid.selectedBoat.width)                # S'il sors, alors le placer à l'extrémité

                if event.type == pygame.KEYDOWN:                                                      # Si une touche a été pressée
                    if event.key == pygame.K_r:                                                       # Si il s'agit de la touche R
                        for row in self.grid.tiles[self.grid.turn]:
                            for tile in row:
                                if tile.mouseover():                                                       # Pour chaque case de la grille, vérifie si la souris est dessus
                                    if self.grid.stage == 0:                                                       # Vérifie si le placement des bateaux est toujours en cours
                                        self.grid.selectedBoat.rotate(self.grid.selectedBoat.direction + 1)       # Tourne le bateau en cours de placement
                                        # Gestion des mouvements de la prévisualitation du bateau pour la direction 0
                                        if self.grid.x - self.grid.selectedBoat.width >= tile.x and self.grid.selectedBoat.direction == 0: # Vérifie si le bateau ne sors pas de la grille
                                            self.grid.selectedBoat.move(tile.x, tile.y)
                                        elif self.grid.selectedBoat.direction == 0:
                                            self.grid.selectedBoat.move(self.grid.x - self.grid.selectedBoat.width, tile.y)                # S'il sors, alors le placer à l'extrémité

                                        # Gestion des mouvements de la prévisualitation du bateau pour la direction 1
                                        if self.grid.selectedBoat.width - 1 <= tile.y and self.grid.selectedBoat.direction == 1:           # Vérifie si le bateau ne sors pas de la grille
                                            self.grid.selectedBoat.move(tile.x, tile.y)
                                        elif self.grid.selectedBoat.direction == 1:
                                            self.grid.selectedBoat.move(tile.x, self.grid.selectedBoat.width - 1)                          # S'il sors, alors le placer à l'extrémité

                                        # Gestion des mouvements de la prévisualitation du bateau pour la direction 2
                                        if self.grid.selectedBoat.width - 1 <= tile.x and self.grid.selectedBoat.direction == 2:           # Vérifie si le bateau ne sors pas de la grille
                                            self.grid.selectedBoat.move(tile.x, tile.y)
                                        elif self.grid.selectedBoat.direction == 2:
                                            self.grid.selectedBoat.move(self.grid.selectedBoat.width - 1, tile.y)                          # S'il sors, alors le placer à l'extrémité

                                        # Gestion des mouvements de la prévisualitation du bateau pour la direction 3
                                        if self.grid.x - self.grid.selectedBoat.width >= tile.y and self.grid.selectedBoat.direction == 3: # Vérifie si le bateau ne sors pas de la grille
                                            self.grid.selectedBoat.move(tile.x, tile.y)
                                        elif self.grid.selectedBoat.direction == 3:
                                            self.grid.selectedBoat.move(tile.x, self.grid.y - self.grid.selectedBoat.width)                # S'il sors, alors le placer à l'extrémité
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

            self.window.fill(0)

            # Partie rendu des éléments
            
            msg = self.font.render(self.message, True, (0, 204, 0))          # Texte indiquant quel joueur doit jouer
            self.window.blit(msg, (9, self.height * self.tileHeight + 5))

            turn = self.grid.turn

            if delay:
                if turn == 1:
                    turn = 0
                    self.message = "Joueur 2, veuillez bombarder une case"
                elif turn == 0:
                    turn = 1
                    self.message = "Joueur 1, veuillez bombarder une case"

            for boat in self.grid.boats[1 - self.grid.turn]:
                destroyed = True
                if boat.direction == 0:
                    for x in range(boat.x, boat.x + boat.width):
                        if self.grid.tiles[self.grid.turn][x][boat.y].state != 2:
                            destroyed = False
                if boat.direction == 1:
                    for y in range(boat.y, boat.y + boat.width):
                        if self.grid.tiles[self.grid.turn][boat.x][y - boat.width + 1].state != 2:
                            destroyed = False
                if boat.direction == 2:
                    for x in range(boat.x, boat.x + boat.width):
                        if self.grid.tiles[self.grid.turn][x - boat.width + 1][boat.y].state != 2:
                            destroyed = False
                if boat.direction == 3:
                    for y in range(boat.y, boat.y + boat.width):
                        if self.grid.tiles[self.grid.turn][boat.x][y].state != 2:
                            destroyed = False
                if destroyed:
                    if boat.direction == 0:
                        for x in range(boat.x, boat.x + boat.width):
                            self.grid.tiles[self.grid.turn][x][boat.y].state = 3
                    if boat.direction == 1:
                        for y in range(boat.y, boat.y + boat.width):
                            self.grid.tiles[self.grid.turn][boat.x][y - boat.width + 1].state = 3
                    if boat.direction == 2:
                        for x in range(boat.x, boat.x + boat.width):
                            self.grid.tiles[self.grid.turn][x - boat.width + 1][boat.y].state = 3
                    if boat.direction == 3:
                        for y in range(boat.y, boat.y + boat.width):
                            self.grid.tiles[self.grid.turn][boat.x][y].state = 3

            for row in self.grid.tiles[turn]:
                for tile in row:
                    tile.__draw__()

            if self.grid.stage == 0 :
                for boat in self.grid.boats[self.grid.turn]:
                    boat.__draw__()

            if self.grid.selectedBoat != None:
                self.grid.selectedBoat.__draw__()

            for row in self.grid.tiles[turn]:
                for tile in row:
                    tile.__drawState__()

            pygame.display.flip()
            if delay:
                pygame.time.delay(1000)
                delay = False


game = Main()
