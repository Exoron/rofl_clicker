import pygame

pygame.init()
pygame.font.init()

font_consolas = pygame.font.SysFont('Consolas', 40)
win = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("Rofl clicker")

sprite = pygame.image.load('sprites/Nastya.svg.png')


def draw_window():
    win.fill((128, 0, 255))
    win.blit(sprite, (100, 100))
    score_text = font_consolas.render('Score: {}'.format(score), False, (0, 0,
                                                                         0))
    win.blit(score_text, (200, 50))
    pygame.display.update()


score = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            score += 1

    draw_window()

pygame.quit()
