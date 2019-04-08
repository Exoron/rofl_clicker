import pygame

pygame.init()
pygame.font.init()

score_font = pygame.font.SysFont('Consolas', 40)
shop_button_font = pygame.font.SysFont('Consolas', 45)
win = pygame.display.set_mode((1800, 900))

pygame.display.set_caption("Rofl clicker")

click_power = 1


class Nastya(object):
    def __init__(self):
        self.sprite = pygame.image.load('sprites/Nastya.svg.png')
        self.x = 100
        self.y = 100
        self.width = 300
        self.height = 431

    def draw(self, surface):
        surface.blit(self.sprite, (self.x, self.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            global score
            mouse_pos = pygame.mouse.get_pos()

            if self.x <= mouse_pos[0] <= self.x + self.width \
                    and self.y <= mouse_pos[1] <= self.y + self.height:
                score += click_power


class ShopButton(object):
    def __init__(self, name, price):
        self.height = 60
        self.width = 500
        self.number = 0
        self.name = name
        self.price = price

    def draw(self, surface, indent):
        x = win.get_width() - self.width - 10
        y = indent + self.height + 10
        pygame.draw.rect(surface, (200, 200, 200), (x, y, self.width,
                                                    self.height))
        button_text = shop_button_font.render('{}'.format(self.name), False,
                                              (0, 0, 0))
        #Размещает текст на кнопке
        #Отступ слева чуть больше высоты кнопки
        #По высоте текст размещается ровно посередине кнопки
        surface.blit(button_text, (x + self.height + 10,
                                   y + (self.height -
                                        shop_button_font.get_height()) // 2))

    def handle_event(self, event):
        pass


shop_buttons = [ShopButton('shop_button', 10), ShopButton('shop_button',
                                                          10),
                ShopButton('shop_button', 10)]

nastya = Nastya()


def draw_window():
    win.fill((128, 0, 255))
    nastya.draw(win)
    for index in range(len(shop_buttons)):
        shop_buttons[index].draw(win, 70 * index)
    score_text = score_font.render('Score: {}'.format(score), False, (0, 0,
                                                                      0))
    win.blit(score_text, (200, 50))
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
