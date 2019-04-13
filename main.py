import pygame
from GameObjects.ClickObjects import ClickObject
from GameObjects.Shop import Shop


def init():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Rofl clicker")


def draw_window():
    win.fill((128, 0, 255))
    nastya.draw()
    shop.draw()

    pygame.display.update()


init()

win = pygame.display.set_mode((1800, 900))
nastya = ClickObject.ClickObject(win)
shop = Shop.Shop(win, nastya)
shop.add_upgrade('Jupiter', 10, 1)
shop.add_upgrade('Anaconda VM', 100, 10)
shop.add_upgrade('PyPy VM', 1000, 50)

close = False
delay = 20
while __name__ == '__main__':
    pygame.time.delay(delay)
    pygame.event.post(pygame.event.Event(pygame.USEREVENT,
                                         {'action': 'NEW_FRAME',
                                          'delay': delay}))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
            break
        nastya.handle_event(event)
        shop.handle_event(event)
    if close:
        break

    draw_window()

pygame.quit()
