#  Practice Games Setup

import pygame

WIDTH = 1200
HEIGHT = 600


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scrolling")
clock = pygame.time.Clock()
running = True
dt = 1
image = pygame.image.load(r"Temp.bmp")
IMAGE_SIZE = (100, 100)
image = pygame.transform.scale(image, IMAGE_SIZE)
player_pos = pygame.Vector2((screen.get_width() - image.get_width()) / 2, (screen.get_height() - image.get_height()) / 2)

bg = pygame.image.load("Temp-bg.png").convert()
bg_pos = pygame.Vector2(
    (screen.get_width() - bg.get_width()), 
    (screen.get_height() - bg.get_height()))
scroll = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # print(player_pos[0], player_pos[1])

    # screen.fill((255,255,255))

    key = pygame.key.get_pressed()
    # print(key[pygame.K_w])
    if key[pygame.K_w]:
        pass
        # player_pos.y -= 10 * dt
        # screen.scroll(0, int(1000 * dt))
        # screen.blit(bg, (bg.get_width(), 0))
    if key[pygame.K_s]:
        pass
        # player_pos.y += 10 * dt
        # screen.scroll(0, int(-1000 * dt))
    if key[pygame.K_a]:
        scroll -= 5

        # player_pos.x -= 10 * dt
        # screen.scroll(int(10 * dt), 0)
    if key[pygame.K_d]:
        scroll += 5
        # player_pos.x += 10 * dt
        # screen.scroll(int(-10 * dt), 0)
    
    if abs(scroll) > bg.get_width():
        if scroll < 0:
            scroll = screen.get_width()
        else:
            scroll = - screen.get_width()
    print(scroll)
    screen.blit(bg, (bg_pos[0] - scroll, bg_pos[1] - 0))
    screen.blit(image, player_pos)
    # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(player_pos[0], player_pos[1], 60, 60))


    # screen.set_at((player_pos[0], player_pos[1]), 2)
    # screen.subsurface()

    # print(player_pos)

    # pygame.display.flip()
    pygame.display.update()

    clock.tick(60)

pygame.quit()