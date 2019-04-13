import pygame
from GameObjects import GameObject
from Geometry import surface_functions


class ClickObject(GameObject.GameObject):
    def __init__(self, surface):
        self.sprite = pygame.image.load('sprites/Nastya.svg.png')
        # TODO remove hardcoded size
        x = 100
        y = 100
        width = 300
        height = 431
        self.face_surface = surface.subsurface(pygame.Rect(x, y,
                                                           width, height))
        self.text_surface = surface.subsurface(pygame.Rect(x, y - 50,
                                                           width, 50))
        self.speed_surface = surface.subsurface(pygame.Rect(x, y + height +
                                                            10, width, 100))
        self.score = 0
        self.score_font = pygame.font.SysFont('Consolas', 40)
        self.speed_font = pygame.font.SysFont('Consolas', 35)
        self.click_power = 1
        self.speed = 0

    def draw(self):
        self.face_surface.blit(self.sprite, (0, 0))
        score_text = self.score_font.render(
            'Score: {}'.format(round(self.score)),
            False, (0, 0, 0))
        self.text_surface.blit(score_text, (0, 0))

        speed_caption_text = self.speed_font.render(
            'Generation per second:'.format(self),
            False, (0, 0, 0)
        )
        speed_value_text = self.speed_font.render(
            '{}'.format(self.speed),
            False, (0, 0, 0)
        )

        self.speed_surface.blit(speed_caption_text, (0, 0))
        self.speed_surface.blit(speed_value_text,
                                (0, self.speed_font.get_height() + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if surface_functions.collides_surface(self.face_surface, mouse_pos):
                self.score += self.click_power
        elif event.type == pygame.USEREVENT:
            if event.action == 'NEW_FRAME':
                self.score += (self.speed * event.delay) / 1000

    def buy_upgrade(self, upgrade):
        if upgrade.get_price() <= self.score:
            self.score -= upgrade.get_price()
            self.speed += upgrade.get_power()
            return True
        else:
            return False
