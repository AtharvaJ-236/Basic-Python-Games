import pygame, random, sys

pygame.init()
W, H, CELL = 400, 400, 20
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

BLACK, GREEN, RED, WHITE = (0,0,0), (0,255,0), (255,0,0), (255,255,255)

snake = [(5, 5)]
dir = (1, 0)
food = (random.randint(0, 19), random.randint(0, 19))
score = 0

def draw():
    screen.fill(BLACK)
    for s in snake:
        pygame.draw.rect(screen, GREEN, (s[0]*CELL, s[1]*CELL, CELL, CELL))
    pygame.draw.rect(screen, RED, (food[0]*CELL, food[1]*CELL, CELL, CELL))
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.flip()

while True:
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT: sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and dir != (0,1): dir = (0,-1)
            elif e.key == pygame.K_DOWN and dir != (0,-1): dir = (0,1)
            elif e.key == pygame.K_LEFT and dir != (1,0): dir = (-1,0)
            elif e.key == pygame.K_RIGHT and dir != (-1,0): dir = (1,0)

    head = (snake[0][0] + dir[0], snake[0][1] + dir[1])
    if head in snake or not (0 <= head[0] < W//CELL and 0 <= head[1] < H//CELL):
        print("Game Over! Final Score:", score)
        pygame.quit(); sys.exit()

    snake.insert(0, head)
    if head == food:
        score += 1
        while True:
            food = (random.randint(0, 19), random.randint(0, 19))
            if food not in snake: break
    else:
        snake.pop()

    draw()
