# this file was created by Sean Lennon
# thanks Chris Bradfield from Kids Can Code

import pygame as pg
import random
from settings import *
from sprites import *


class Game:
    def _init_(self):
        # init game window, try:
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("jumpy")
        self.clock = pg.time.Clock()
        self.running = True

        #init pygame and create...
   
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()
        # create new player object
    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update
            self.draw()
    def update(self):
        self.all_sprites,update()
        # update things
    def events(self):
        
        # listening for events
        for event in pg.event.get():
            if event.type  == pg.QUIT:
                if self.playing:
                    self.playing = False
                 self.running - False
    def draw(self):
        self.screen.fill(REDDISH)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass
g = Game()
g.show_start_screen()

while g.running:
        g.new()
        g.show_go_screen