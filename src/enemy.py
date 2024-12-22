import pygame

class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('assets/images/player2.png'), (200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = (700, 300)
        self.speed = 3

    def update(self):
        # 簡単なAIロジック（プレイヤーに向かって動くなど）
        if self.rect.x < 400:
            self.rect.x += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)
