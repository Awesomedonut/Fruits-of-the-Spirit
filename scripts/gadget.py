import pygame

class Gadget:
    def __init__(self, x, y, width, height):
        self.collider = pygame.Surface((width, height)).convert()
        self.rect = self.collider.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.collider.fill((255, 0, 0))

    def draw(self):
        pygame.display.get_surface().blit(self.collider, (self.rect.x, self.rect.y))

