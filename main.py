import pygame

pygame.init()
pygame.font.init()

font_consolas = pygame.font.SysFont('Consolas', 40)
win = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("Rofl clicker")


class Nastya(object):
    def __init__(self):
        self.sprite = pygame.image.load('sprites/Nastya.svg.png')
        self.x = 100
        self.y = 100
        self.width = 300
        self.height = 431

    def draw(self, surface):
        surface.blit(self.sprite, (self.x, self.y))


nastya = Nastya()


def draw_window():
    win.fill((128, 0, 255))
    nastya.draw(win)
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
