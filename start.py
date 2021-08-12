import pygame
from scripts.main import main
from scripts.utils import load_all_images
    
if __name__ == "__main__":

    main()
    
    
    for key,value in load_all_images().items():
        print(key, value)
    
    pygame.quit()