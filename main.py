import pygame
from ShopButton import ShopButton
from ClickObjects import Nastya

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((1800, 900))

pygame.display.set_caption("Rofl clicker")


shop_buttons = [ShopButton.ShopButton('shop_button', 10),
                ShopButton.ShopButton('shop_button', 10),
                ShopButton.ShopButton('shop_button', 10)]

nastya = Nastya.Nastya()


def draw_window():
    win.fill((128, 0, 255))
    nastya.draw(win)
    for index in range(len(shop_buttons)):
        shop_buttons[index].draw(win, 70 * index)

    pygame.display.update()


score = 0

close = False
while __name__ == '__main__':
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
            break
        nastya.handle_event(event)
    if close:
        break

    draw_window()

pygame.quit()
