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
        self.gravity = 5
        self.right_frames = []
        self.left_frames = []
        self.animation_index = R_DEFAULT
        
        self.load_from_sheet() #put correct images in right frames and left frame arrays

        self.image = self.right_frames[self.animation_index]


    def update(self, keys_pressed, win):
        self.handle_state(keys_pressed)
        
        self.update_pos()
        self.animation()
        self.draw(win)


    def draw(self, win):
        win.fill((12, 12, 200))    
        win.blit(self.image, (self.rect.x, self.rect.y))

    def animation(self):
        
        if self.facing_right:
            self.image = self.right_frames[self.animation_index]
        else:
            self.image = self.left_frames[self.animation_index]


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
        self.animation_index = R_DEFAULT
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
        self.animation_index = R_WALK1
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
        self.animation_index = R_JUMP
        print(f"jumping has been called {self.rect.bottom}")
        self.y_vel += self.gravity
        if(self.rect.bottom > 600):
            if self.y_vel > 0:
                self.y_vel = 0
            print(f"y vel is {self.y_vel}")
            self.state = STAND

    def get_image(self, x, y, width, height):
        layer = pygame.Surface([width, height]).convert()
        rect = layer.get_rect()
        layer.blit(self.mario_bros, (0, 0), (x, y, width, height))
        layer.set_colorkey((0, 0, 0))
        layer = pygame.transform.scale(layer, (rect.width * SIZE_MULTIPLIER, rect.height * SIZE_MULTIPLIER))
        
        return layer

    def load_from_sheet(self):
        self.right_frames.append(self.get_image(178, 32, 12, 16)) #right
        self.right_frames.append(self.get_image(80, 32, 15, 16)) #r walk 1
        self.right_frames.append(self.get_image(99, 32, 15, 16)) #r walk 2
        self.right_frames.append(self.get_image(114, 32, 15, 16)) #r walk 3
        self.right_frames.append(self.get_image(144, 32, 16, 16)) #r jump
        self.right_frames.append(self.get_image(130, 32, 14, 16)) #r skid

        for frame in self.right_frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            self.left_frames.append(flipped_frame)



            
    