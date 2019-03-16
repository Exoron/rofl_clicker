import pygame


pygame.init()
win = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("Rofl clicker")

sprite = pygame.image.load('sprites/Nastya.svg.png')


def draw_window():
    win.fill((128, 0, 255))
    win.blit(sprite, (100, 100))
    pygame.display.update()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_window()

pygame.quit()
