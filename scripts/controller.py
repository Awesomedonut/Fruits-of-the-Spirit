import pygame
from scripts.mario import Mario
from scripts.constants import *
from scripts.utils import *
from scripts.gadget import *

class Controller:

    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.keys_pressed = pygame.key.get_pressed()
        self.mario = Mario()
        self.bg = load_all_images()["level_1"]
        self.bg_rect = self.bg.get_rect()
        self.bg = pygame.transform.scale(self.bg, (int(self.bg_rect.width * BG_MULTIPLIER), int(self.bg_rect.height * BG_MULTIPLIER)))
        self.camera_shift = 0
        self.pipes = []
        self.setup_pipes()

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
        for pipe in self.pipes:
            pipe.draw()
        self.mario.update(self.keys_pressed, self.win)
        print(self.check_collisions_between_mario_and_pipes())

    def camera(self):
        if self.mario.rect.x > SCREEN_WIDTH // 2:
            self.camera_shift = self.mario.rect.x - (SCREEN_WIDTH // 2)
            
        else:
            self.camera_shift = 0
       # if self.mario.state == WALK:
        self.bg_rect.x = self.bg_rect.x - self.camera_shift
        for pipe in self.pipes:
            pipe.rect.x -= self.camera_shift
        self.mario.rect.x -= self.camera_shift

    def setup_pipes(self):
        self.pipes.append(Gadget(1202, 452, 83, 82))
        self.pipes.append(Gadget(1631, 409, 83, 140))
        self.pipes.append(Gadget(1973, 366, 83, 170))
        self.pipes.append(Gadget(2445, 366, 83, 170))
        self.pipes.append(Gadget(6989, 452, 83, 82))
        # last pipe near the end self.pipes.append(Gadget(6989, 452, 83, 82))

    def check_collisions_between_mario_and_pipes(self):
        for pipe in self.pipes:
            if self.mario.rect.x + self.mario.width > pipe.rect.x and self.mario.rect.x < pipe.rect.x + pipe.width and self.mario.rect.y + self.mario.height > pipe.rect.y:
                    return True

            # if self.mario.rect.y > pipe.rect.y:
            #     self.mario.rect.x < pipe.rect.x + pipe.width
            #     return True

        return False
        


    def main(self):
        while True: #always running
            pygame.time.Clock().tick(60) 
            self.event_loop()
            self.update()
            self.camera()
            pygame.display.update()
