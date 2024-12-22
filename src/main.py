import pygame
from game import Game

def main():
    pygame.init()

    # ゲームのインスタンスを作成
    game = Game()

    # ゲームループ
    while game.running:
        game.handle_events()
        game.update()
        game.render()

    pygame.quit()

if __name__ == "__main__":
    main()
