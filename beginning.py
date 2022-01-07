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
        self.screen.blit(self.font.render('START', True, (0, 0, 0)), (50, 50))
        # кнопка правила
        continue_button = pygame.draw.rect(self.screen, (57, 255, 20), (20, 130, 150, 50))
        self.continue_button = continue_button
        self.screen.blit(self.font.render('RULES', True, (0, 0, 0)), (50, 140))
        # кнопка выход
        quit_button = pygame.draw.rect(self.screen, (57, 255, 20), (20, 220, 150, 50))
        self.quit_button = quit_button
        self.screen.blit(self.font.render('EXIT', True, (0, 0, 0)), (50, 230))
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
        self.screen.blit(self.font.render('RETURN', True, (0, 0, 0)), (600, 490))
        pygame.display.update()
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 730 >= pygame.mouse.get_pos()[0] >= 580 and 530 >= pygame.mouse.get_pos()[1] >= 480:
                        # запускаем функцию создания меню
                        self.moving()

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


# создание элементов для 2 меню
screen = pygame.display.set_mode((640, 480))
color_inactive = pygame.Color((0, 255, 0))
color_active = pygame.Color('dodgerblue2')
font = pygame.font.Font(None, 32)


# класс 2 меню, поле ввода время игры
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color_inactive
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False

    # функция для создания поля ввода
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = color_active if self.active else color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    # проверка введенного текста
                    # текст должен быть целым числом от 5 до 25 минут
                    # если текст не проходит проверку, то окно ввода очищается
                    if not self.text.isdigit() or len(self.text) > 2:
                        self.text = ''
                    elif int(self.text) < 5 or int(self.text) > 25:
                        self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(70, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        screen.blit(font.render('Время игры (в минутах):', True, (57, 255, 20)), (30, 415))
        screen.blit(font.render('Выберите уровень игры:', True, (57, 255, 20)), (20, 15))
        pygame.draw.rect(screen, self.color, self.rect, 2)

        self.lever_drawing()

    def lever_drawing(self):
        self.leve_one = pygame.Rect(30, 50, 100, 100)
        c_i = pygame.Color((0, 255, 0))
        c_a = pygame.Color('dodgerblue2')
        self.c = c_i
        self.a = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if self.leve_one.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.a = not self.a
                else:
                    self.a = False
                # Change the current color of the input box.
                self.c = c_a if self.a else c_i
        pygame.draw.rect(screen, self.c, self.leve_one, 2)



def main():
    clock = pygame.time.Clock()
    input_box1 = InputBox(300, 400, 140, 50)
    # список полей ввода
    input_boxes = [input_box1]
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:

                box.handle_event(event)
        for box in input_boxes:
            box.update()
        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)
        pygame.display.flip()
        clock.tick(30)


a = Menu()
