import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Rofl clicker")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((128, 0, 255))
    pygame.display.update()

pygame.quit()
