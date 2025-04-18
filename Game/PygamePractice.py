#  PygamePractice
#  https://pygame.readthedocs.io/en/latest/tiles/tiles.html#create-a-tileset

import pygame
from pygame import *
import numpy as np

file = "Temp.bmp"

class Game:
    W = 640
    H = 240
    SIZE = W, H

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Game.SIZE)  #  Sets the size of the screen.
        pygame.display.set_caption("Pygame Tile Demo")   # Sets windows title
        self.running = True
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                
                elif event.type == KEYDOWN:
                    if event.key == K_1:
                        self.load_image(file)

        pygame.quit()

    def load_image(self, file):
        self.file = file
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()  #  Size of rect. divide H and W by 2 to get center.

        self.screen = pygame.display.set_mode(self.rect.size)  #  Sets screen size. Additional parameters affect screen.
        pygame.display.set_caption(f'size:{self.rect.size}')
        self.screen.blit(self.image, self.rect)  # Draws one image on another.
        pygame.display.update()  #  Updates display

class Tileset:
    def __init__(self, file, size=(32, 32), margin=1, spacing=1):
        self.file = file
        self.size = size
        self.margin = margin
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = []
        self.spacing = spacing
        self.load()
    
    def load(self):
        self.tiles = []
        x0 = y0 = self.margin
        w, h = self.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing

        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tile = pygame.Surface(self.size)
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                self.tiles.append(tile)
    
    def __str__(self):
        return f'{self.__class__.__name__} file:{self.file} tile:{self.size}'
    
class Tilemap:
    def __init__(self, tileset, size=(10, 10), rect=None):
        self.size = size
        self.tileset = tileset
        self.map = np.zeros(size, dtype=int)    #  Creates array filled with the type, while zero values.

        h, w = self.size
        self.image = pygame.surface((32*w, 32*h))
        if rect:
            self.rect = pygame.Rect(rect)  #  Gets the height, width, and placement of Rect.
        else:
            self.rect = self.image.get_rect()
    
    def render(self):
        m, n = self.map.shape
        for i in range(m):
            for j in range(n):
                tile = self.tileset.tiles[self.map[i, j]]
                self.image.blit(tile, (j*32, i*32))
    
    def set_zero(self):
        self.map = np.zeros(self.size, dtype=int)  #  Creates array filled with the type, while zero values.
        print(self.map)
        print(self.map.shape)
        self.render()

    def set_random(self):
        n = len(self.tileset.tiles)  
        self.map = np.random.randint(n, size=self.size)  #  Random values with the same shape as size. Creates
        print(self.map)
        self.render()

    def __str__(self):
        return f'{self.__class__.__name__} {self.size}'
    
game= Game()
game.run()