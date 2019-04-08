import pygame


class ShopButton(object):
    def __init__(self, name, price):
        self.height = 60
        self.width = 500
        self.number = 0
        self.name = name
        self.price = price
        self.font = pygame.font.SysFont('Consolas', 45)

    def draw(self, surface, indent):
        x = surface.get_width() - self.width - 10
        y = indent + self.height + 10
        pygame.draw.rect(surface, (200, 200, 200), (x, y, self.width,
                                                    self.height))
        button_text = self.font.render('{}'.format(self.name),
                                       False,
                                       (0, 0, 0))
        # Размещает текст на кнопке
        # Отступ слева чуть больше высоты кнопки
        # По высоте текст размещается ровно посередине кнопки
        surface.blit(button_text, (x + self.height + 10,
                                   y + (self.height -
                                        self.font.get_height()) // 2))

    def handle_event(self, event):
        pass
