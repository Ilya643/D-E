import pygame

pygame.init()


# меню игры D&E
# создание самого первого окна меню
class Menu:
    def __init__(self):
        screen = pygame.display.set_mode((640, 480))
        self.screen = screen
        pygame.display.set_caption("menu")
        self.font = pygame.font.SysFont('Arial', 35)
        # создание кнопок меню
        # кнопка старт
        start_button = pygame.draw.rect(self.screen, (57, 255, 20), (20, 40, 150, 50))
        self.start_button = start_button
        self.screen.blit(self.font.render('Начать', True, (0, 0, 0)), (50, 50))
        # кнопка правила
        continue_button = pygame.draw.rect(self.screen, (57, 255, 20), (20, 130, 150, 50))
        self.continue_button = continue_button
        self.screen.blit(self.font.render('Правила', True, (0, 0, 0)), (40, 140))
        # кнопка выход
        quit_button = pygame.draw.rect(self.screen, (57, 255, 20), (20, 220, 150, 50))
        self.quit_button = quit_button
        self.screen.blit(self.font.render('Выход', True, (0, 0, 0)), (50, 230))
        pygame.display.update()
        pygame.display.flip()
        self.moving()

    # функция создания меню
    def moving(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 90 >= pygame.mouse.get_pos()[1] >= 40:
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 90 >= pygame.mouse.get_pos()[1] >= 40:
                        # запускаем функцию старт
                        self.start()
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 180 >= pygame.mouse.get_pos()[1] >= 130:
                        # запускаем функцию правила
                        self.rules()
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 270 >= pygame.mouse.get_pos()[1] >= 220:
                        # выход из игры
                        exit()

    def rules(self):
        # в это функии мы выводим правила по запросу из бд
        self.screen = pygame.display.set_mode((750, 550))
        self.screen.fill('black')
        pygame.display.set_caption("Rules")
        # создаем кнопку возвращения, чтобы после прочтения правил можно было вернуться в главное меню
        return_button = pygame.draw.rect(self.screen, (57, 255, 20), (580, 480, 150, 50))
        self.return_button = return_button
        self.screen.blit(self.font.render('Вернуться', True, (0, 0, 0)), (585, 490))
        pygame.display.update()
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 730 >= pygame.mouse.get_pos()[0] >= 580 and 530 >= pygame.mouse.get_pos()[1] >= 480:
                        # запускаем функцию создания меню
                        # делаем это через создание нового элемента класса
                        b = Menu()

    def start(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill('black')
        pygame.display.set_caption("menu_continue")
        pygame.display.update()
        pygame.display.flip()
        # запускаем функцию настройки
        if __name__ == '__main__':
            main()
        exit()

# класс для выбора уровня
# продолжения менюхи
class RadioButton(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, font, text):
        super().__init__()
        self.font = None
        self.screen = pygame.display.set_mode((640, 480))
        text_surf = font.render(text, True, (0, 0, 0))
        self.button_image = pygame.Surface((w, h))
        self.button_image.fill((169, 169, 169))

        self.button_image.blit(text_surf, text_surf.get_rect(center=(w // 2, h // 2)))
        self.hover_image = pygame.Surface((w, h))
        self.hover_image.fill((169, 169, 169))
        self.hover_image.blit(text_surf, text_surf.get_rect(center=(w // 2, h // 2)))
        pygame.draw.rect(self.hover_image, (255, 99, 71), self.hover_image.get_rect(), 3)
        self.clicked_image = pygame.Surface((w, h))
        self.clicked_image.fill((255, 99, 71))
        self.clicked_image.blit(text_surf, text_surf.get_rect(center=(w // 2, h // 2)))
        self.image = self.button_image
        self.rect = pygame.Rect(x, y, w, h)
        self.clicked = False
        self.buttons = None



    def setRadioButtons(self, buttons):
        self.buttons = buttons

    def update(self, event_list):
        hover = self.rect.collidepoint(pygame.mouse.get_pos())
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # уровень 1
                if 400 >= pygame.mouse.get_pos()[0] >= 50 and 99 >= pygame.mouse.get_pos()[1] >= 40:
                    if __name__ == '__main__':
                        mn()
                    exit()
                # уровень 2
                elif 400 >= pygame.mouse.get_pos()[0] >= 50 and 180 >= pygame.mouse.get_pos()[1] >= 120:
                    if __name__ == '__main__':
                        mn()
                    exit()
                # уровень 3
                elif 400 >= pygame.mouse.get_pos()[0] >= 50 and 260 >= pygame.mouse.get_pos()[1] >= 200:
                    if __name__ == '__main__':
                        mn()
                    exit()
                if hover and event.button == 1:
                    for rb in self.buttons:
                        rb.clicked = False
                    self.clicked = True

        self.image = self.button_image
        if self.clicked:
            self.image = self.clicked_image
        elif hover:
            self.image = self.hover_image




def main():
    pygame.init()
    window = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    font50 = pygame.font.SysFont(None, 50)

    radioButtons = [
        RadioButton(50, 40, 350, 60, font50, "Первый уровень"),
        RadioButton(50, 120, 350, 60, font50, "Второй уровень"),
        RadioButton(50, 200, 350, 60, font50, "Третий уровень")
    ]
    for rb in radioButtons:
        rb.setRadioButtons(radioButtons)
    radioButtons[0].clicked = True

    group = pygame.sprite.Group(radioButtons)

    run = True
    while run:
        clock.tick(60)
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False

        group.update(event_list)

        window.fill(0)
        group.draw(window)
        pygame.display.flip()

    pygame.quit()
    exit()

# функция, запускающаяся после выбора уровня
def mn():
    screen = pygame.display.set_mode((640, 480))
    screen.fill((0, 0, 0))
    pygame.display.set_caption('menu_continue')
    font = pygame.font.SysFont('Arial', 35)
    # прямоугольник для кнопки возврата
    returning = pygame.draw.rect(screen, (57, 255, 20), (20, 370, 140, 70))
    screen.blit(font.render('Вернуться', True, (0, 0, 0)), (20, 380))
    screen.blit(font.render('Время игры (в минутах):', True, (57, 255, 20)), (10, 20))

    clock = pygame.time.Clock()
    input_box = pygame.Rect(370, 10, 140, 52)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # кнопка возврата
                # на тот случай если пользователь захочет вернуться к выбору уровня игры
                if 160 >= pygame.mouse.get_pos()[0] >= 20 and 440 >= pygame.mouse.get_pos()[1] >= 370:
                    main()
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if not text.isdigit() or len(text) > 2 or int(text) < 5 or int(text) > 25:
                            text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        screen.fill((0, 0, 0))
        returning = pygame.draw.rect(screen, (57, 255, 20), (20, 370, 140, 70))
        screen.blit(font.render('Вернуться', True, (0, 0, 0)), (20, 380))
        screen.blit(font.render('Время игры (в минутах):', True, (57, 255, 20)), (10, 10))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)

a = Menu()



