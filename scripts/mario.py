import pygame

class Mario:
    
    def __init__(self):
        self.lives = 3
       # self.image =
      #  self.rect = self.image.get_rect()
        self.status = "active"
        self.facing_right = True
        self.y = 0
        self.x = 0

    def move(self):
        if pygame.key.get_pressed()[pygame.K_w]:
            self.y -= 5
        if pygame.key.get_pressed()[pygame.K_s]:
            self.y += 5
        if pygame.key.get_pressed()[pygame.K_a]:
            self.x -= 5
        if pygame.key.get_pressed()[pygame.K_d]:
            self.x += 5
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.y -= 15
        
