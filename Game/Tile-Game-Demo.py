#  Tile-Game
#  Creator: Me
#  Complete:  False

import pygame

class Game:
    WIDTH = 1200
    HEIGHT = 900
    SIZE = WIDTH, HEIGHT
    file = ""
    BG = pygame.image.load("Temp-bg.png")
    Tiles = (8, 8)  # 8 by 8
    rescale = 60
    Black_Tile = pygame.image.load("Black-Tile.png")
    White_Tile = pygame.image.load("White-Tile.png")
    Black_Tile = pygame.transform.scale(Black_Tile, [rescale, rescale])
    White_Tile = pygame.transform.scale(White_Tile, [rescale, rescale])
    SCALE = 1
    MARGIN = 5
    Current_Board = {}
    PAWN = pygame.image.load("Chess-Pawn.png")

    def __init__(self, sizes=(32, 32)):
        pygame.init()
        pygame.display.set_caption("Chess")
        self.running = True
        self.sizes = sizes
        tiles = []
        self.screen = pygame.display.set_mode(Game.SIZE)
        self.BG_pos = pygame.Vector2((self.screen.get_width() - self.BG.get_width()) / 2, ((self.screen.get_height() - self.BG.get_height())) / 2)
        print(self.BG_pos)
        pygame.display.update()
    
    def tileSet(self, col, row):
        if col > 0:
            y = ((Game.rescale * col) * Game.SCALE) + (Game.MARGIN * col)
        else:
            y = (Game.rescale * col) * Game.SCALE
        if row > 0:
            x = ((Game.rescale * row) * Game.SCALE) + (Game.MARGIN * row)
        else:
            x = (Game.rescale * row) * Game.SCALE
        return x, y

    def tileMap(self):
        rows = {}
        white_tiles = []
        black_tiles = []
        self.tile_start_index = 0
        for x in range(self.tile_start_index, Game.Tiles[0]):
            for y in range(self.tile_start_index, Game.Tiles[1]):
                if (y+x) % 2 == 0:
                    # row += {self.tileSet(y, x) : Game.Black_Tile}
                    # row[self.tileSet(y, x)] = Game.Black_Tile
                    white_tiles += self.tileSet(y, x)
                    # print(0)
                else:
                    # row += {self.tileSet(y, x) : Game.White_Tile}
                    # row[self.tileSet(y, x)] = Game.White_Tile
                    black_tiles += self.tileSet(y, x)
                Game.Current_Board[(y, x)] = None
        rows[Game.White_Tile] = white_tiles
        rows[Game.Black_Tile] = black_tiles

        #  Didn't work, as it requires a deep copy.
        # white_tiles.sort()
        # black_tiles.sort()
        self.lowest_pos = white_tiles[0] if white_tiles[0] < black_tiles[0] else black_tiles[0]
        self.highest_pos = white_tiles[-1] if white_tiles[-1] > black_tiles[-1] else black_tiles[-1]
        # print(pygame.display.get_window_size())
        return rows
    
    def centerize(self):
        # first = Game.rescale * start_index
        # scale = Game.Tiles
        height = self.highest_pos
        center = pygame.display.get_window_size()  # x, y (Width, Height)
        center = [(center[0] / 2) - (height / 2) - self.rescale,
                (center[1] / 2) - (height / 2) - self.rescale]
        print(center)
        return center
        # pass

    def game_start(self):
        self.screen.blit(Game.BG, self.BG_pos)
        self.Tiles = self.tileMap()
        print(self.Tiles)
        # for x in range(0, len(self.Tiles), 4):
        #     self.screen.blit(Game.White_Tile, (self.Tiles[x], self.Tiles[x + 1]))
        #     self.screen.blit(Game.Black_Tile, (self.Tiles[x + 2], self.Tiles[x + 3]))

        center = self.centerize()

        print(center)
        for color in self.Tiles.keys():
            for x in range(0, len(self.Tiles[color]), 2):
                 self.screen.blit(color,   #  Color
                                  (center[0] + self.Tiles[color][x], center[1] + self.Tiles[color][x + 1]))  #  Placement.
        pygame.display.update()
        print(Game.Current_Board)
        while self.running:
            for event in pygame.event.get():
                # print(event.type)
                if event.type == pygame.QUIT:
                    self.running = False
        pygame.quit()

game = Game()
game.game_start()