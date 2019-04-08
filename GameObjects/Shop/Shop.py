import pygame
from GameObjects import GameObject
from GameObjects.ShopButton import ShopButton


class Shop(GameObject.GameObject):
    def __init__(self, surface):
        self.button_width = 500
        self.surface = surface.subsurface(pygame.Rect(surface.get_width() -
                                                      self.button_width - 10,
                                                      10, self.button_width,
                                                      surface.get_height() -
                                                      20))

        self.buttons = [ShopButton.ShopButton('shop_button', 10),
                        ShopButton.ShopButton('shop_button', 10),
                        ShopButton.ShopButton('shop_button', 10)]

    def draw(self, surface, coords):
        self.surface.fill((100, 100, 100))
        for index in range(len(self.buttons)):
            indent = 70 * index
            y = indent + 10

            self.buttons[index].draw(self.surface, (0, y))

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)
