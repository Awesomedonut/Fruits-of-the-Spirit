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
        self.y = 10
        self.x = 0
        self.x_vel = 0
        self.x_accel = 5
        self.y_vel = 0
        self.y_accel = 5
        self.MAX_X_SPEED = 20
        self.MAX_Y_SPEED = 20
        self.MAX_X_ACCEL = 7
        self.MAX_Y_ACCEL= 7
        self.gravity = 1
        self.right_frames = []
        

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
        #if self.rect.y < 600:
        self.rect.y += self.y_vel

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
            print("a has been detected")
            self.facing_right = False
       
          #  self.x_vel = -10
          
            if self.x_vel > -1 * self.MAX_X_SPEED:
                
                self.x_vel -= self.x_accel
            print(f"{self.x_vel} a")
        if keys_pressed[pygame.K_d]:
            self.facing_right = True
       
            if self.x_vel < self.MAX_X_SPEED:
               self.x_vel += self.x_accel
            print(f"{self.x_vel} d")
        if keys_pressed[pygame.K_w]:

            self.y_vel = -10
            self.state = JUMP
            

    def jumping(self):
        print(f"jumping has been called {self.rect.bottom}")
        self.y_vel += self.gravity
        if(self.rect.bottom > 600):
            if self.y_vel > 0:
                self.y_vel = 0
            print(f"y vel is {self.y_vel}")
            self.state = STAND

    def load_from_sheet(self):
        self.right_frames.append(self.get_image(178, 32, 12, 16))
        


    # def handle_gravity(self):
    #     if(self.rect.bottom < 600):
    #         self.y_vel += self.gravity
    #     else:
    #         if self.y_vel > 0:
    #             self.y_vel = 0
    #         self.state = STAND
    #     print(f"y vel is {self.y_vel}")

    
            
    