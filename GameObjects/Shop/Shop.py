import pygame
from GameObjects import GameObject
from GameObjects.ShopButton import ShopButton
from GameObjects.Upgrade import Upgrade


class Shop(GameObject.GameObject):
    def __init__(self, surface, customer):
        self.customer = customer
        self.button_width = 500
        self.button_height = 100

        self.price_multiplier = 1.3
        self.surface = surface.subsurface(
            pygame.Rect(
                surface.get_width() - self.button_width - 10,
                10, self.button_width, surface.get_height() - 20
            )
        )
        self.upgrades = []

    def draw(self):
        self.surface.fill((100, 100, 100))
        for index in range(len(self.upgrades)):
            self.upgrades[index]['button'].draw()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for upgrade in self.upgrades:
                if upgrade['button'].handle_event(event):
                    if self.customer.buy_upgrade(upgrade['upgrade']):
                        upgrade['upgrade'].increment(1, self.price_multiplier)

    def add_upgrade(self, name, price, power):
        indent = 10
        y = (self.button_height + indent) * len(self.upgrades) + indent

        upgrade = Upgrade.Upgrade(name, power, price)
        self.upgrades.append({
            'upgrade': upgrade,
            'button': ShopButton.ShopButton(
                self.surface,
                pygame.Rect(0, y, self.button_width, self.button_height),
                upgrade
            )
        })
