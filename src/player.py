import pygame
from setting import Settings

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('assets/images/player1.png'), (200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 300)
        self.speed = 5
        self.jump_speed = -15
        self.gravity = 1
        self.is_jumping = False
        self.vertical_speed = 0
        self.step_timer = 0
        self.step_interval = 20  # Time window for double input (in frames)
        self.step_direction = None
        self.double_input = False

    def update(self):
        keys = pygame.key.get_pressed()

        # Movement left and right
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            if self.step_direction == 'left' and self.step_timer > 0:
                self.perform_step('left')
            self.step_direction = 'left'
            self.step_timer = self.step_interval
        elif keys[pygame.K_d]:
            self.rect.x += self.speed
            if self.step_direction == 'right' and self.step_timer > 0:
                self.perform_step('right')
            self.step_direction = 'right'
            self.step_timer = self.step_interval
        else:
            self.step_timer = max(0, self.step_timer - 1)

        # Jump
        if not self.is_jumping and keys[pygame.K_w]:
            self.is_jumping = True
            self.vertical_speed = self.jump_speed

            # Check for diagonal jump
            if keys[pygame.K_a]:
                self.rect.x -= self.speed  # Adjust for diagonal jump left
            elif keys[pygame.K_d]:
                self.rect.x += self.speed  # Adjust for diagonal jump right

        # Apply gravity if jumping
        if self.is_jumping:
            self.vertical_speed += self.gravity
            self.rect.y += self.vertical_speed

            # Stop jumping when landing on ground
            if self.rect.bottom >= 300:  # Assuming ground level is y=300
                self.rect.bottom = 300
                self.is_jumping = False
                self.vertical_speed = 0

    def perform_step(self, direction):
        if direction == 'left':
            self.rect.x -= 30
        elif direction == 'right':
            self.rect.x += 30
        self.step_timer = 0  # Reset timer after step

    def draw(self):
        self.screen.blit(self.image, self.rect)
