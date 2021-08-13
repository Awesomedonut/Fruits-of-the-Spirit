from scripts.constants import *
from scripts.utils import *

import pygame

class Mario:
    
    def __init__(self):
        self.lives = 3
        self.mario_bros = load_all_images()["mario_bros"]
        self.rect = self.mario_bros.get_rect()
        self.status = "active"
        self.facing_right = True
        self.state = STAND
        self.y = 0
        self.x = 0
        self.x_vel = 0
        self.x_accel = 0
        self.y_vel = 0
        self.y_accel = 0
        self.MAX_X_SPEED = 10
        self.MAX_Y_SPEED = 10
        self.MAX_X_ACCEL = 10
        self.MAX_Y_ACCEL= 10
        self.gravity = 1
        

    def update(self, keys_pressed, win):
        self.handle_state(keys_pressed)
        
        self.update_pos()
        self.draw(win)


    def draw(self, win):
        
        
        layer = pygame.Surface([12, 16]).convert()
       # rect = layer.get_rect()

        layer.blit(self.mario_bros, (0, 0), (178, 32, 12, 16))
    
        layer = pygame.transform.scale(layer, (48, 64))
        win.fill((200, 12, 12))
        win.blit(layer, (self.rect.x, self.rect.y))
 

    def animation():
        pass

    def update_pos(self):

        # if pygame.key.get_pressed()[pygame.K_w]:
        #     self.y -= 5
        # if pygame.key.get_pressed()[pygame.K_s]:
        #     self.y += 5
        # if pygame.key.get_pressed()[pygame.K_a]:
        #     self.x -= 5
        # if pygame.key.get_pressed()[pygame.K_d]:
        #     self.x += 5

        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        #print("update pos has been called")


    def handle_state(self, keys_pressed):
        if self.state == STAND:
            self.standing(keys_pressed)
        if self.state == WALK:
            self.walking(keys_pressed)
        if self.state == JUMP:
            self.jumping()


    def standing(self, keys_pressed):
        if keys_pressed[pygame.K_w]:
            self.state = JUMP
            self.y_vel = -10
            print("w has been detected")

        if keys_pressed[pygame.K_a]:
            self.facing_right = False
            self.state = WALK
           
        if keys_pressed[pygame.K_d]:
            self.facing_right = True
            self.state = WALK

    def walking(self, keys_pressed):
        if keys_pressed[pygame.K_a]:
            self.facing_right = False
            self.state = WALK
            self.x_vel =+ self.x_accel
           
        if keys_pressed[pygame.K_d]:
            self.facing_right = True
            self.state = WALK

        if keys_pressed[pygame.K_w]:
            self.state = JUMP

    def jumping(self):
        self.y_vel += self.gravity
        if(self.rect.bottom > 600):
            self.y_vel = 0
            self.state = STAND


    
            
    