import pygame
from setting import Settings

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('assets/images/player1.png'), (200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 300)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)
