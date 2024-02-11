import pygame
import random


WIDTH = 800
HEIGHT = 600
BALL_RADIUS = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Dgame:
    def __init__(self):
        self.running = False

    def start_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ding Dong Game")

        self.clock = pygame.time.Clock()
        self.running = True
        self.initialize_game()

    def initialize_game(self):
        
        self.player_paddle = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.ai_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

        
        self.ball = pygame.Rect(WIDTH//2 - BALL_RADIUS, HEIGHT//2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.ball_speed_x = 5 * random.choice((1, -1))
        self.ball_speed_y = 5 * random.choice((1, -1))

        self.game_loop()

    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and self.player_paddle.top > 0:
                self.player_paddle.y -= PADDLE_SPEED
            if keys[pygame.K_DOWN] and self.player_paddle.bottom < HEIGHT:
                self.player_paddle.y += PADDLE_SPEED

            
            if self.ball.y < self.ai_paddle.y + self.ai_paddle.height // 2:
                self.ai_paddle.y -= PADDLE_SPEED
            elif self.ball.y > self.ai_paddle.y + self.ai_paddle.height // 2:
                self.ai_paddle.y += PADDLE_SPEED

            
            self.update_ball()

            
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def update_ball(self):
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y
        
        
        if self.ball.top <= 0 or self.ball.bottom >= HEIGHT:
            self.ball_speed_y *= -1
        if self.ball.left <= 0 or self.ball.right >= WIDTH:
            self.ball_speed_x *= -1

        
        if self.ball.colliderect(self.player_paddle) or self.ball.colliderect(self.ai_paddle):
            self.ball_speed_x *= -1

    def draw(self):
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, WHITE, self.player_paddle)
        pygame.draw.rect(self.screen, WHITE, self.ai_paddle)
        pygame.draw.ellipse(self.screen, WHITE, self.ball)

