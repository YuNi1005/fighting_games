import pygame
import sys
from setting import Settings
from player import Player
from enemy import Enemy

class Game:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        self.title = pygame.display.set_caption(self.settings.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(self.screen)
        self.enemy = Enemy(self.screen)
        self.background = pygame.image.load('assets/images/background.png')  # 背景画像の読み込み
        self.background = pygame.transform.scale(self.background, (self.settings.WIDTH, 200))  # 画面サイズに合わせてリサイズ

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update()
        self.enemy.update()

    def render(self):
        # 背景画像を描画
        self.screen.fill(self.settings.BACKGROUNDCOLOR)
        self.screen.blit(self.background, (0, 450))
        
        self.player.draw()
        self.enemy.draw()
        
        pygame.display.flip()  # 画面を更新
        self.clock.tick(self.settings.FPS)  # フレームレートを設定
