# Pong Game in Python using Pygame

import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100

# Ball dimensions
BALL_WIDTH, BALL_HEIGHT = 15, 15

# Initialize paddles and ball positions
left_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_WIDTH // 2, HEIGHT // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT)

# Speed variables
paddle_speed = 5
ball_speed_x = 4
ball_speed_y = 4

# Score
score_left = 0
score_right = 0

# Font
font = pygame.font.Font(None, 74)

# Main game loop
def main():
    global ball_speed_x, ball_speed_y, score_left, score_right

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= paddle_speed
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += paddle_speed
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= paddle_speed
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += paddle_speed

        # Ball movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Ball collision with walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1

        # Ball collision with paddles
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_speed_x *= -1

        # Scoring
        if ball.left <= 0:
            score_right += 1
            ball.x, ball.y = WIDTH // 2, HEIGHT // 2
            ball_speed_x *= -1

        if ball.right >= WIDTH:
            score_left += 1
            ball.x, ball.y = WIDTH // 2, HEIGHT // 2
            ball_speed_x *= -1

        # Drawing everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, left_paddle)
        pygame.draw.rect(screen, WHITE, right_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        # Display scores
        left_text = font.render(str(score_left), True, WHITE)
        right_text = font.render(str(score_right), True, WHITE)
        screen.blit(left_text, (WIDTH // 4, 20))
        screen.blit(right_text, (WIDTH * 3 // 4, 20))

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Run the game
if __name__ == "__main__":
    main()

