import pygame
from scripts.mario import Mario
from scripts.constants import *
from scripts.utils import *

class Controller:

    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.keys_pressed = pygame.key.get_pressed()
        self.mario = Mario()
        self.bg = load_all_images()["level_1"]
        self.bg_rect = self.bg.get_rect()
        self.bg = pygame.transform.scale(self.bg, (self.bg_rect.width * BG_MULTIPLIER, self.bg_rect.height * BG_MULTIPLIER))

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.keys_pressed = pygame.key.get_pressed()
            elif event.type == pygame.KEYUP:
                self.keys_pressed = pygame.key.get_pressed()
            
    def update(self):
        
        pygame.display.get_surface().blit(self.bg, self.bg_rect)
        self.mario.update(self.keys_pressed, self.win)

    def camera(self):
        self.bg_rect.x = self.bg_rect.x - 1

    def main(self):
        while True: #always running
            pygame.time.Clock().tick(60) 
            self.event_loop()
            self.update()
            self.camera()
            pygame.display.update()
