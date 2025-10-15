import pygame, random, sys
pygame.init()

# Setup
W, H = 800, 600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Shooter vs Target")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Colors
WHITE, RED, BLUE, BLACK = (255,255,255), (255,0,0), (0,0,255), (0,0,0)

# Shooter & Bullet
sx, sy, sw, sh, ss = W//2-25, H-60, 50, 50, 5
bullets, bs = [], 7

# Target
r = 30
tx, ty = random.randint(r, W-r), 100
ts = [3, 3]

score = 0
run = True

while run:
    clock.tick(60)
    win.fill(WHITE)

    # Events
    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit(); sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            bullets.append(pygame.Rect(sx+sw//2-2, sy, 5, 10))

    # Keys
    k = pygame.key.get_pressed()
    sx += (k[pygame.K_RIGHT]-k[pygame.K_LEFT]) * ss
    sx = max(0, min(W-sw, sx))

    # Target move
    tx += ts[0]; ty += ts[1]
    if tx<=r or tx>=W-r: ts[0]*=-1
    if ty<=r or ty>=H//2: ts[1]*=-1

    # Draw target & shooter
    pygame.draw.circle(win, RED, (tx, ty), r)
    pygame.draw.rect(win, BLUE, (sx, sy, sw, sh))

    # Bullets
    for b in bullets[:]:
        b.y -= bs
        if b.y < 0: bullets.remove(b); continue
        pygame.draw.rect(win, BLACK, b)
        if ((b.centerx-tx)**2+(b.centery-ty)**2)**0.5 <= r:
            bullets.remove(b)
            score += 1
            tx, ty = random.randint(r, W-r), random.randint(50, H//3)
            ts = [random.choice([-3,3]), random.choice([-3,3])]

    win.blit(font.render(f"Score: {score}", True, BLACK), (10, 10))
    pygame.display.flip()
