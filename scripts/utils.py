import os
import pygame

def load_all_images():
    graphics = {}
    dirs = os.listdir(os.path.join("resources", "graphics"))
    for file in dirs:
        file_name, _ = os.path.splitext(file)
        print(os.path.splitext(file))
        print(file_name)
        file_image = pygame.image.load(os.path.join("resources", "graphics", file))
        graphics[file_name] = file_image
        
    return graphics
    

    