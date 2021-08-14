import pygame
from scripts.mario import Mario

class Controller:

    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((1500, 500))
        self.keys_pressed = pygame.key.get_pressed()
        self.mario = Mario()

    def event_loop(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.keys_pressed = pygame.key.get_pressed()
                # if event.key == pygame.K_SPACE:
                #     mario.y -= 15
            elif event.type == pygame.KEYUP:
                self.keys_pressed = pygame.key.get_pressed()
            

    def update(self):
        self.mario.update(self.keys_pressed, self.win)

    def main(self):

        
 
        while True: #always running
            pygame.time.Clock().tick(60) 
            self.event_loop()
            self.update()
            pygame.display.update()