import pygame


class Upgrade:
    def __init__(self, name, power, price):
        self.name = name
        self.power = power
        self.number = 0
        self.price = price

    def get_name(self):
        return self.name

    def get_power(self):
        return self.power

    def get_number(self):
        return self.number

    def get_price(self):
        return self.price

    def increment(self, number, price_multiplier):
        self.number += number
        self.price = round(self.price * price_multiplier)
