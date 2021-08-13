import pygame
from scripts.main import main
from scripts.utils import load_all_images, load_all_music, load_all_sound_effects, draw

if __name__ == "__main__":
    pygame.init()
   # main()
   
    # for key, value in load_all_images().items():
    #     print(key, value)
    # for key, value in load_all_music().items():
    #     print(key, value)
    # for key, value in load_all_sound_effects().items():
    #     print(key, value)
    win = pygame.display.set_mode((500, 300))
 
    while True: #always running
        pygame.time.Clock().tick(60) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            else:
                draw(win)
        
                pygame.display.update()

    