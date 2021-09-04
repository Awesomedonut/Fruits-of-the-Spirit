import pygame

class Gadget:
    def __init__(self, x, y, width, height):
        self.collider = pygame.Surface((width, height)).convert()
        self.rect = self.collider.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collider.fill((255, 0, 0))
        pygame.display.get_surface().blit(self.collider, (x, y))

