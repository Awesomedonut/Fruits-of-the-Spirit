from scripts.constants import *
from scripts.utils import *
import pygame

class Mario:
    
    def __init__(self):
        self.lives = 3
        self.mario_bros = load_all_images()["mario_bros"]
        
        self.status = "active"
        self.facing_right = True
        self.state = STAND

        self.x_vel = 0
        self.x_accel = 5
        self.y_vel = 0
        self.y_accel = 5
        self.MAX_X_SPEED = 20
        self.MAX_Y_SPEED = 20
        self.MAX_X_ACCEL = 7
        self.MAX_Y_ACCEL= 7
        self.gravity = 2

        self.jump_height = -30

        self.right_frames = []
        self.left_frames = []
        self.animation_index = MOV_DEFAULT
        
        self.load_from_sheet() #put correct images in right frames and left frame arrays

        self.image = self.right_frames[self.animation_index]
        self.rect = self.image.get_rect()
        self.rect.y = SCREEN_HEIGHT - 200
        self.rect.x = 0

    def update(self, keys_pressed, win):
        self.handle_state(keys_pressed)
        self.update_pos()
        self.animation()
        self.draw(win)

    def draw(self, win):
 
        win.blit(self.image, (self.rect.x, self.rect.y))

    def animation(self):
        
        if self.facing_right:
            self.image = self.right_frames[self.animation_index]
        else:
            self.image = self.left_frames[self.animation_index]

    def update_pos(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

    def handle_state(self, keys_pressed):
        if self.state == STAND:
            self.standing(keys_pressed)
        if self.state == WALK:
            self.walking(keys_pressed)
        if self.state == JUMP:
            self.jumping()

    def standing(self, keys_pressed):
        self.animation_index = MOV_DEFAULT
        if keys_pressed[pygame.K_w]:
            self.state = JUMP
            self.y_vel = self.jump_height
           

        if keys_pressed[pygame.K_a]:
            self.facing_right = False
            self.state = WALK
           
        if keys_pressed[pygame.K_d]:
            self.facing_right = True
            self.state = WALK

    def walking(self, keys_pressed):
        if self.animation_index > MOV_DEFAULT and self.animation_index < MOV_JUMP:
            if self.animation_index == MOV_WALK3:
                self.animation_index = MOV_WALK1
            else:
                self.animation_index += 1
        else:
            self.animation_index = MOV_WALK1

        if keys_pressed[pygame.K_a]:
            if self.x_vel > 0:
                self.animation_index = MOV_SKID
            self.facing_right = False
            if self.x_vel > -1 * self.MAX_X_SPEED:
                
                self.x_vel -= self.x_accel
            print(f"{self.x_vel} a")

        elif keys_pressed[pygame.K_d]:
            if self.x_vel < 0:
                self.animation_index = MOV_SKID
            self.facing_right = True
            if self.x_vel < self.MAX_X_SPEED:
               self.x_vel += self.x_accel
            print(f"{self.x_vel} d")

        else:
            if self.x_vel != 0:
                self.x_vel = self.x_vel * FRICTION_MU
                print(self.x_vel)

                if self.facing_right:
                    if self.x_vel < 0.55:
                        self.x_vel = 0
                else:
                    if self.x_vel > -0.55:
                        self.x_vel = 0
            else:
                self.state = STAND

        if keys_pressed[pygame.K_w]:
            self.y_vel = self.jump_height
            self.state = JUMP
        
        # if self.x_vel > 0 and self.facing_right == True:
        #     self.x_vel -= self.friction
        #     if self.x_vel < 0:
        #         self.x_vel = 0
        # elif self.x_vel < 0 and self.facing_right == False:
        #     self.x_vel += self.friction
        #     if self.x_vel > 0:
        #         self.x_vel = 0

    def jumping(self):
        self.animation_index = MOV_JUMP

        self.y_vel += self.gravity
        if (self.rect.bottom > SCREEN_HEIGHT - 200 + 96 ):
            if self.y_vel > 0:
                self.y_vel = 0
                self.state = WALK
            
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