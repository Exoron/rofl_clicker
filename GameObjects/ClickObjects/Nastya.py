import pygame
from GameObjects import GameObject


class Nastya(GameObject.GameObject):
    def __init__(self):
        self.sprite = pygame.image.load('sprites/Nastya.svg.png')
        self.x = 100
        self.y = 100
        self.width = 300
        self.height = 431
        self.score = 0
        self.score_font = pygame.font.SysFont('Consolas', 40)
        self.click_power = 1

    def draw(self, surface, coords=(200, 50)):
        surface.blit(self.sprite, (self.x, self.y))
        score_text = self.score_font.render('Score: {}'.format(self.score),
                                            False, (0, 0, 0))
        surface.blit(score_text, coords)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if self.x <= mouse_pos[0] <= self.x + self.width \
                    and self.y <= mouse_pos[1] <= self.y + self.height:
                self.score += self.click_power
