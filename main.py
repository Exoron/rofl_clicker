import pygame
from GameObjects.ClickObjects import Nastya
from GameObjects.Shop import Shop


pygame.init()
pygame.font.init()
pygame.display.set_caption("Rofl clicker")


def draw_window():
    win.fill((128, 0, 255))
    nastya.draw(win)
    shop.draw(win, (0, 0))

    pygame.display.update()


win = pygame.display.set_mode((1800, 900))
shop = Shop.Shop(win)
nastya = Nastya.Nastya()

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
