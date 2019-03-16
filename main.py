import pygame

pygame.init()
pygame.font.init()

font_consolas = pygame.font.SysFont('Consolas', 40)
win = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("Rofl clicker")

click_power = 1

class Nastya(object):
    def __init__(self):
        self.sprite = pygame.image.load('sprites/Nastya.svg.png')
        self.x = 100
        self.y = 100
        self.width = 300
        self.height = 431

    def draw(self, surface):
        surface.blit(self.sprite, (self.x, self.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            global score
            mouse_pos = pygame.mouse.get_pos()

            if self.x <= mouse_pos[0] <= self.x + self.width\
                    and self.y <= mouse_pos[1] <= self.y + self.height:
                score += click_power


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
        nastya.handle_event(event)

    draw_window()

pygame.quit()
