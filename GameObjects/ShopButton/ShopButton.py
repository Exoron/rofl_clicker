import pygame
from GameObjects import GameObject


class ShopButton(GameObject.GameObject):
    def __init__(self, name, price):
        self.height = 60
        self.width = 500
        self.number = 0
        self.name = name
        self.price = price
        self.name_font = pygame.font.SysFont('Consolas', 45)
        self.number_font = pygame.font.SysFont('Consolas', 65)

    def draw(self, surface, coords):
        pygame.draw.rect(surface, (200, 200, 200), (coords[0], coords[1],
                                                    self.width,
                                                    self.height))
        button_text = self.name_font.render('{}'.format(self.name),
                                            False,
                                            (0, 0, 0))
        # Размещает текст на кнопке
        # Отступ слева чуть больше высоты кнопки
        # По высоте текст размещается ровно посередине кнопки
        surface.blit(button_text,
                     (coords[0] + self.height + 10, coords[1] +
                      (self.height - self.name_font.get_height()) // 2))

        number_text = self.number_font.render('{}'.format(self.number),
                                              False, (0, 0, 0))

        surface.blit(number_text,
                     (coords[0] + 10, coords[1] +
                      (self.height - self.number_font.get_height()) // 2))

    def handle_event(self, event):
        pass

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
