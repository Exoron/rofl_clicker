import pygame
from GameObjects import GameObject
from Geometry import surface_functions
from GameObjects.Upgrade import Upgrade


class ShopButton(GameObject.GameObject):
    def __init__(self, surface, rect, upgrade):
        self.upgrade = upgrade
        self.name_font = pygame.font.SysFont('Consolas', 45)
        self.number_font = pygame.font.SysFont('Consolas', 65)
        self.description_font = pygame.font.SysFont('Consolas', 35)
        self.surface = surface.subsurface(rect)

    def draw(self):
        self.surface.fill((200, 200, 200))

        number_text = self.number_font.render(
            '{}'.format(self.upgrade.get_number()),
            False, (0, 0, 0))

        # Размещает текст чуть правее левого края кнопки
        # По высоте текст ровно посередине кнопки
        self.surface.blit(
            number_text,
            (10, (self.get_height() - self.number_font.get_height()) // 2))

        name_text = self.name_font.render(
            '{}'.format(self.upgrade.get_name()),
            False, (0, 0, 0))

        name_text_height = 5

        # Размещает текст на кнопке чуть ниже её верхнего края
        # Отступ слева чуть больше высоты кнопки
        self.surface.blit(
            name_text, (self.get_height() + 10, name_text_height))

        price_text = self.description_font.render(
            'Price: {}'.format(self.upgrade.get_price()),
            False, (0, 0, 0))

        price_text_height = name_text_height + self.name_font.get_height() + 5

        # Размещает текст на кнопе чуть ниже её нижнего края
        # Отсуп слева на одном уровне с текстом названия
        self.surface.blit(
            price_text,
            (self.get_height() + 10,
             price_text_height))

        bonus_text = self.description_font.render(
            'Increase: {} p/s'.format(self.upgrade.get_power()),
            False, (0, 0, 0))

        bonus_text_height = (price_text_height +
                             self.description_font.get_height() + 5)

        self.surface.blit(
            bonus_text,
            (self.get_height() + 10,
             bonus_text_height)
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return surface_functions.collides_surface(self.surface,
                                                      pygame.mouse.get_pos())

    def get_width(self):
        return self.surface.get_rect().width

    def get_height(self):
        return self.surface.get_rect().height
