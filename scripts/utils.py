import os
import pygame


def load_all_images():
    graphics = {}
    dirs = os.listdir(os.path.join("resources", "graphics"))
    for file in dirs:
        file_name, _ = os.path.splitext(file)
        file_image = pygame.image.load(os.path.join("resources", "graphics", file))
        graphics[file_name] = file_image
        
    return graphics


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

