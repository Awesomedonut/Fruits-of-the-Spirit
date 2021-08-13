import os
import pygame


def load_all_images():
    graphics = {}
    dirs = os.listdir(os.path.join("resources", "graphics"))
    for file in dirs:
        file_name, _ = os.path.splitext(file)
       # print(os.path.splitext(file))
       # print(file_name)
        file_image = pygame.image.load(os.path.join("resources", "graphics", file))
        graphics[file_name] = file_image
        
    return graphics

def draw(win, mario):
    mario_bros = load_all_images()["mario_bros"]
    
    layer = pygame.Surface([12, 16]).convert()
    rect = layer.get_rect()

    layer.blit(mario_bros, (0, 0), (178, 32, 12, 16))
  
    layer = pygame.transform.scale(layer, (48, 64))
    win.fill((200, 12, 12))
    win.blit(layer, (mario.x, mario.y))

def load_all_music():
    music = {}
    dirs = os.listdir(os.path.join("resources", "music"))
    for file in dirs:
        file_name, _ = os.path.splitext(file)
        print(os.path.splitext(file))
        print(file_name)
        music[file_name] = os.path.join("resources", "music", file)
    return music
    
def load_all_sound_effects():
    sounds = {}
    dirs = os.listdir(os.path.join("resources", "sound"))
    for file in dirs:
        file_name, _ = os.path.splitext(file)
        print(os.path.splitext(file))
        print(file_name)
        sounds[file_name] = os.path.join("resources", "sound", file)
    return sounds

def event_loop():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
            else:
                draw(win, mario)
                mario.move()
        
                pygame.display.update()