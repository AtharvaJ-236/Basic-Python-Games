import pygame, random, sys
pygame.init()

# Screen setup
W, H = 800, 600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Target Shooting Game")
font = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()

# Colors
WHITE, RED, BLACK = (255,255,255), (255,0,0), (0,0,0)

# Target
r = 30
x, y = random.randint(r, W-r), random.randint(r, H-r)
speed = [random.choice([-3, 3]), random.choice([-3, 3])]

score = 0
running = True

while running:
    clock.tick(60)
    win.fill(WHITE)

    # Move and bounce target
    x += speed[0]; y += speed[1]
    if x <= r or x >= W - r: speed[0] *= -1
    if y <= r or y >= H - r: speed[1] *= -1

    # Draw target & score
    pygame.draw.circle(win, RED, (x, y), r)
    win.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))

    # Event handling
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if ((mx - x)**2 + (my - y)**2)**0.5 <= r:
                score += 1
                x, y = random.randint(r, W-r), random.randint(r, H-r)
                speed = [random.choice([-3, 3]), random.choice([-3, 3])]

    pygame.display.flip()
