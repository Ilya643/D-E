import pygame
import sqlite3
from random import sample

pygame.init()

# передает значение о выбранном уровне
level = 0
# передает значение о выбранном времени
time = 0

dt = 0
# передает значение о выбранном скине
skin = 0
# меню игры D&E
# создание самого первого окна меню


class Menu:
    def __init__(self):
        screen = pygame.display.set_mode((640, 480))
        self.screen = screen
        pygame.display.set_caption("menu")
        self.font = pygame.font.SysFont('Arial', 35)
        # вставляем изображении черепашки в меню)
        turtole = pygame.image.load('img_D&E.bmp')
        turtole.set_colorkey((255, 255, 255))
        turtole_rect = turtole.get_rect(center=(750 // 2, 720 // 2))
        screen.blit(turtole, turtole_rect)
        # создание кнопок меню
        # кнопка старт
        start_button = pygame.draw.rect(self.screen, (57, 255, 20), (20, 40, 150, 50))
        self.start_button = start_button
        self.screen.blit(self.font.render('Начать', True, (0, 0, 0)), (50, 50))
        # кнопка правила
        continue_button = pygame.draw.rect(self.screen, (57, 255, 20), (20, 130, 150, 50))
        self.continue_button = continue_button
        self.screen.blit(self.font.render('Правила', True, (0, 0, 0)), (40, 135))
        # кнопка рекордов
        record_button = pygame.draw.rect(self.screen, (57, 255, 20), (20, 220, 150, 50))
        self.record_button = record_button
        self.screen.blit(self.font.render('Рекорды', True, (0, 0, 0)), (40, 225))
        # кнопка выход
        quit_button = pygame.draw.rect(self.screen, (57, 255, 20), (20, 310, 150, 50))
        self.quit_button = quit_button
        self.screen.blit(self.font.render('Выход', True, (0, 0, 0)), (50, 320))
        pygame.display.update()
        pygame.display.flip()
        self.moving()

    # функция создания меню
    def moving(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 90 >= pygame.mouse.get_pos()[1] >= 40:
                        # запускаем функцию старт
                        self.start()
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 180 >= pygame.mouse.get_pos()[1] >= 130:
                        # запускаем функцию правила
                        self.rules()
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 270 >= pygame.mouse.get_pos()[1] >= 220:
                        # запускаем функцию рекордов
                        self.record()
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 360 >= pygame.mouse.get_pos()[1] >= 310:
                        # выход из игры
                        exit()

    def rules(self):
        # в это функии мы выводим правила с помощью работы с файлами
        self.screen = pygame.display.set_mode((1120, 700))
        self.screen.fill('black')
        pygame.display.set_caption("Rules")
        # создаем кнопку возвращения, чтобы после прочтения правил можно было вернуться в главное меню
        return_button = pygame.draw.rect(self.screen, (57, 255, 20), (900, 620, 150, 50))
        self.return_button = return_button
        self.screen.blit(self.font.render('Вернуться', True, (0, 0, 0)), (905, 620))
        document = open('pravila_D&E.txt', encoding='utf8')
        document2 = document.readlines()
        # проверяем есть ли такой файл на устройстве пользователя
        try:
            document = open('pravila_D&E.txt')
        # если нет, то выдаем предупреждение об этом
        except IOError as _:
            font = pygame.font.SysFont('Arial', 40)
            txt = font.render('Файл с правилами игры не найден на вашем устройстве.', True, (57, 255, 20))
            self.screen.blit(txt, (22, 22))
            txt = font.render('Пожалуйста завершите установку.', True, (57, 255, 20))
            self.screen.blit(txt, (22, 102))
        else:
            # проверка на тот случай если файл с правилами оказался пустым
            if len(document2) == 0:
                font = pygame.font.SysFont('Arial', 50)
                txt = font.render('Файл с правилами игры пустой.', True, (57, 255, 20))
                self.screen.blit(txt, (22, 22))
                txt = font.render('Рекомендуем заново установить файл.', True, (57, 255, 20))
                self.screen.blit(txt, (22, 102))
            # если все хорошо то:
            else:
                y = 0
                # работа с файлом
                for el in document2:
                    el = el.replace('\n', '')
                    font = pygame.font.SysFont('Arial', 20)
                    txt = font.render(el, True, (57, 255, 20))
                    self.screen.blit(txt, (22, y))
                    y += 24
        pygame.display.update()
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 1050 >= pygame.mouse.get_pos()[0] >= 900 and 670 >= pygame.mouse.get_pos()[1] >= 620:
                        # запускаем функцию создания меню
                        # делаем это через создание нового элемента класса
                        Menu()

    def record(self):
        self.screen.fill('black')
        pygame.display.set_caption("Records")
        return_button2 = pygame.draw.rect(self.screen, (57, 255, 20), (460, 420, 150, 50))
        self.return_button2 = return_button2
        self.screen.blit(self.font.render('Вернуться', True, (0, 0, 0)), (465, 425))
        # делаем запрос в бд на рекорды
        con = sqlite3.connect('база_данных007.db')
        cur = con.cursor()
        result = cur.execute('''SELECT * FROM Records''')

        rec = []
        for el in result:
            rec.append(el)
        # изменеям список, так чтобы всегда брать последнии 5 рекордов из бд
        if len(rec) == 0:
            font = pygame.font.SysFont('Arial', 50)
            txt = font.render('Пока что рекордов нет', True, (57, 255, 20))
            self.screen.blit(txt, (30, 30))
        else:
            if len(rec) > 5:
                rec = rec[(len(rec) - 5):]
            x = 30
            y = 20
            for el in rec:
                el = ' '.join(el)
                el = str(el).replace('(', '').replace(')', '').replace(',', '')
                font = pygame.font.SysFont('Arial', 75)
                txt = font.render(str(el), True, (57, 255, 20))
                self.screen.blit(txt, (x, y))
                y += 80

        con.close()
        pygame.display.update()
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 610 >= pygame.mouse.get_pos()[0] >= 460 and 470 >= pygame.mouse.get_pos()[1] >= 420:
                        # запускаем функцию создания меню
                        # делаем это через создание нового элемента класса
                        Menu()

    def start(self):
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
class Level_Button(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, font, text):
        super().__init__()
        self.font = font
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

    def setLevelButtons(self, buttons):
        self.buttons = buttons

    def update(self, event_list):
        global level
        hover = self.rect.collidepoint(pygame.mouse.get_pos())
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # уровень 1
                if 400 >= pygame.mouse.get_pos()[0] >= 50 and 99 >= pygame.mouse.get_pos()[1] >= 40:
                    level = 1
                    if __name__ == '__main__':
                        mn()
                    exit()
                # уровень 2
                elif 400 >= pygame.mouse.get_pos()[0] >= 50 and 180 >= pygame.mouse.get_pos()[1] >= 120:
                    level = 2
                    if __name__ == '__main__':
                        mn()
                    exit()
                # уровень 3
                elif 400 >= pygame.mouse.get_pos()[0] >= 50 and 260 >= pygame.mouse.get_pos()[1] >= 200:
                    level = 3
                    if __name__ == '__main__':
                        mn()
                    exit()
                # возврат в главное меню
                elif 600 >= pygame.mouse.get_pos()[0] >= 450 and 440 >= pygame.mouse.get_pos()[1] >= 380:
                    if __name__ == '__main__':
                        Menu()
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
    font50 = pygame.font.SysFont('Arial', 50)
    level_buttons = [
        Level_Button(50, 40, 350, 60, font50, "Первый уровень"),
        Level_Button(50, 120, 350, 60, font50, "Второй уровень"),
        Level_Button(50, 200, 350, 60, font50, "Третий уровень"),
        # создаем еще одну кнопку, чтобы пользователь мог вернуться в главное меню
        # после выбора уровня
        Level_Button(450, 380, 150, 60, font50, "Назад")
    ]
    for rb in level_buttons:
        rb.setLevelButtons(level_buttons)
    level_buttons[0].clicked = False

    group = pygame.sprite.Group(level_buttons)

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


font = pygame.font.SysFont('Arial', 35)
pygame.display.set_caption('menu_continue')


# функция, запускающаяся после выбора уровня
def mn():
    global skin
    global time
    # меняем размер экрана для удобства
    screen = pygame.display.set_mode((640, 580))
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    input_box = pygame.Rect(370, 10, 140, 52)
    input_box2 = pygame.Rect(370, 100, 140, 52)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    # цвет кнопки начать игру, при активном состоянии
    b_color = pygame.Color('YellowGreen')
    # текст для кнопки запуска игры
    b_text = 'Начать игру'
    active = False
    text = '10'
    time_hod = 'Error'
    # цвета кнопок выбора скина
    turtole_color = pygame.Color('Silver')
    crab_color = pygame.Color('Silver')
    octupos_color = pygame.Color('Silver')
    # ddded показывает выбрат ли какой-то скин, если она равна 0, то нельзя начать игру
    ddded = 0
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # кнопка возврата
                # на тот случай если пользователь захочет вернуться к выбору уровня игры
                if 160 >= pygame.mouse.get_pos()[0] >= 20 and 540 >= pygame.mouse.get_pos()[1] >= 470:
                    main()
                # если пользователь выбрал скин краба, меняем цвет прямоугольника
                if (170 >= pygame.mouse.get_pos()[0] >= 30 or 166 >= pygame.mouse.get_pos()[0] >= 40) \
                        and (270 >= pygame.mouse.get_pos()[1] >= 230 or 430 >= pygame.mouse.get_pos()[1] >= 327):
                    crab_color = pygame.Color('DeepPink')
                    turtole_color = pygame.Color('Silver')
                    octupos_color = pygame.Color('Silver')
                    ddded += 1
                    skin = 'crab'

                # если пользователь выбрал скин осьминога, меняем цвет прямоугольника
                if (385 >= pygame.mouse.get_pos()[0] >= 245 or 397 >= pygame.mouse.get_pos()[0] >= 238) \
                        and (270 >= pygame.mouse.get_pos()[1] >= 230 or 430 >= pygame.mouse.get_pos()[1] >= 287):
                    crab_color = pygame.Color('Silver')
                    turtole_color = pygame.Color('Silver')
                    octupos_color = pygame.Color('DeepPink')
                    ddded += 1
                    skin = 'octupos'

                # если пользователь выбрал скин черепахи, меняем цвет прямоугольника
                if 600 >= pygame.mouse.get_pos()[0] >= 460 \
                        and (270 >= pygame.mouse.get_pos()[1] >= 230 or 440 >= pygame.mouse.get_pos()[1] >= 280):
                    crab_color = pygame.Color('Silver')
                    turtole_color = pygame.Color('DeepPink')
                    octupos_color = pygame.Color('Silver')
                    ddded += 1
                    skin = 'turtole'
                # кнопка начать игру
                # должно открываться игровое поле
                # начало игры
                if 620 >= pygame.mouse.get_pos()[0] >= 440 and 540 >= pygame.mouse.get_pos()[1] >= 470:
                    # если все правильно введено, то кнопка начать игру работает
                    # осуществляем проверку с помощью переменной time_hod
                    if time_hod != 'Error' and ddded > 0:
                        time = int(text)
                        # выходим из меню и запускаем игровое поле
                        # переменные для таймера игры
                        timer = time * 60
                        t_move = int(timer) * 15 // 100

                        size = 900, 700
                        pygame.display.set_caption('D&E')
                        screen = pygame.display.set_mode(size)

                        myfont = pygame.font.SysFont(None, 30)
                        clock = pygame.time.Clock()
                        dt = 0

                        indent = 70
                        part = 20
                        units_peek = (700, 0, 900, 700)
                        cell_size = 70
                        coords_unit = 0
                        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
                        letters_r = ['H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

                        fps = 100

                        con = sqlite3.connect('база_данных007.db')
                        cur = con.cursor()
                        result = cur.execute(f"""SELECT * FROM Figures
                                                WHERE Skin = '{skin}'""").fetchall()
                        con.close()
                        board_units_f = []
                        board_units_e = []
                        for i in result:
                            if i[1] == 'f':
                                board_units_f.append([i[2], (int(i[3].split(',')[0]), int(i[3].split(',')[1])), i[4]])
                            else:
                                board_units_e.append([i[2], (int(i[3].split(',')[0]), int(i[3].split(',')[1])), i[4]])

                        felled_figures_f = {1: 0, 2: 0, 3: 0, 4: 0}
                        felled_figures_e = {1: 0, 2: 0, 3: 0, 4: 0}

                        moves = []

                        cells = [(0, 2), (0, 3), (0, 4), (0, 5),
                                 (1, 2), (1, 3), (1, 4), (1, 5),
                                 (2, 2), (2, 3), (2, 4), (2, 5),
                                 (3, 2), (3, 3), (3, 4), (3, 5),
                                 (4, 2), (4, 3), (4, 4), (4, 5),
                                 (5, 2), (5, 3), (5, 4), (5, 5),
                                 (6, 2), (6, 3), (6, 4), (6, 5),
                                 (7, 2), (7, 3), (7, 4), (7, 5)]

                        move = True
                        unit = (board_units_f, board_units_e)

                        if level == 1:
                            cells = []
                        elif level == 2:
                            cells = sample(cells, 2)
                        else:
                            cells = sample(cells, 4)
                        if skin == 'turtole':
                            un = ['Cyber_Turtle_Friendly_Executioner.png', 'Cyber_Turtle_Friendly_Defender.png',
                                  'Cyber_Turtle_Friendly_King.png', 'Cyber_Turtle_Friendly_Jumper.png',
                                  'Cyber_Turtle_Enemy_Executioner.png', 'Cyber_Turtle_Enemy_Defender.png',
                                  'Cyber_Turtle_Enemy_King.png', 'Cyber_Turtle_Enemy_Jumper.png']
                        elif skin == 'crab':
                            un = ['Cyber_Crab_Friendly_Defender.png', 'Cyber_Crab_Friendly_Executioner.png',
                                  'Cyber_Crab_Friendly_King.png', 'Cyber_Crab_Friendly_Jumper.png',
                                  'Cyber_Crab_Enemy_Defender.png', 'Cyber_Crab_Enemy_Executioner.png',
                                  'Cyber_Crab_Enemy_King.png', 'Cyber_Crab_Friendly_Jumper.png']
                        else:
                            un = ['Cyber_Octopus_Friendly_Defender.png', 'Cyber_Octopus_Friendly_Executioner.png',
                                  'Cyber_Octopus_Friendly_King.png', 'Cyber_Octopus_Friendly_Jumper.png',
                                  'Cyber_Octopus_Enemy_Defender.png', 'Cyber_Octopus_Enemy_Executioner.png',
                                  'Cyber_Octopus_Enemy_King.png', 'Cyber_Octopus_Enemy_Jumper.png']

                        class Board:
                            def __init__(self, width, height, timer, t_move):
                                self.width = width
                                self.height = height
                                self.slovar_with_coords = {}
                                self.board = []
                                self.timer = timer
                                self.t_move = t_move
                                n = 0
                                for _ in range(self.height):
                                    stroka = []
                                    for x in range(self.width):
                                        if x % 2 == 0:
                                            stroka.append((0 + n) % 2)
                                        else:
                                            stroka.append((1 + n) % 2)
                                    n += 1
                                    if n == 2:
                                        n = 0
                                    self.board.append(stroka)

                            def render(self):
                                for y in range(self.height):
                                    for x in range(self.width):
                                        if self.board[y][x] == 1:
                                            pygame.draw.rect(screen, pygame.Color("saddlebrown"),
                                                             (indent + x * cell_size, indent + y * cell_size,
                                                              cell_size, cell_size), 0)
                                        else:
                                            pygame.draw.rect(screen, pygame.Color(255, 170, 0),
                                                             (indent + x * cell_size, indent + y * cell_size,
                                                              cell_size, cell_size), 0)
                                        self.slovar_with_coords[x, y] = (
                                            x * cell_size + indent, y * cell_size + indent, cell_size,
                                            cell_size)

                                pygame.draw.rect(screen, pygame.Color('black'), (indent - 4, indent - 4,
                                                                                 cell_size * 8 + 8,
                                                                                 cell_size * 8 + 8), 4)
                                pygame.draw.rect(screen, pygame.Color(255, 170, 0),
                                                 (indent - part - 4, indent - part - 4,
                                                  cell_size * 8 + part * 2 + 8,
                                                  cell_size * 8 + part * 2 + 8), part)
                                pygame.draw.rect(screen, pygame.Color('darkslategray4'),
                                                 units_peek)

                                y1 = 15
                                for i in un[4:]:
                                    self.image = pygame.image.load(i).convert_alpha()
                                    self.image = pygame.transform.rotate(self.image, 180)
                                    screen.blit(pygame.transform.scale(self.image, (75, 75)), (710, y1))
                                    y1 += 80

                                y1 += 10
                                for i in un[:4]:
                                    self.image = pygame.image.load(i).convert_alpha()
                                    screen.blit(pygame.transform.scale(self.image, (75, 75)), (710, y1))
                                    y1 += 80

                                numbers_e = [felled_figures_e[1], felled_figures_e[2], felled_figures_e[3],
                                             felled_figures_e[4]]
                                numbers_f = [felled_figures_f[1], felled_figures_f[2], felled_figures_f[3],
                                             felled_figures_f[4]]

                                y1 = 45
                                for i in numbers_e:
                                    textsurface = myfont.render(str(i), False, (0, 0, 0))
                                    screen.blit(textsurface, (810, y1))
                                    y1 += 80

                                y1 += 10
                                for i in numbers_f:
                                    textsurface = myfont.render(str(i), False, (0, 0, 0))
                                    screen.blit(textsurface, (810, y1))
                                    y1 += 80

                                y1 = 585
                                if move == 1:
                                    for i in range(1, 9):
                                        textsurface = myfont.render(str(i), False, (0, 0, 0))
                                        screen.blit(textsurface, (52, y1))
                                        y1 -= 70
                                else:
                                    for i in range(8, 0, -1):
                                        textsurface = myfont.render(str(i), False, (0, 0, 0))
                                        screen.blit(textsurface, (52, y1))
                                        y1 -= 70

                                x1 = 95
                                if move == 1:
                                    for i in letters:
                                        textsurface = myfont.render(i, False, (0, 0, 0))
                                        screen.blit(textsurface, (x1, 635))
                                        x1 += 70
                                else:
                                    for i in letters_r:
                                        textsurface = myfont.render(i, False, (0, 0, 0))
                                        screen.blit(textsurface, (x1, 635))
                                        x1 += 70

                                textsurface = myfont.render('До конца игры:', False, pygame.Color('dodgerblue'))
                                screen.blit(textsurface, (45, 20))
                                textsurface = myfont.render('До конца хода:', False, pygame.Color('dodgerblue'))
                                screen.blit(textsurface, (275, 20))

                            def check(self, x, y):
                                for i in self.slovar_with_coords:
                                    coords = self.slovar_with_coords.get(i)
                                    if coords[0] <= x <= coords[0] + coords[2] and coords[1] <= y <= coords[1]\
                                            + coords[3]:
                                        return [True, i]
                                return None

                            def check_piece(self, index):
                                if index == 1:
                                    return Pawn_1
                                if index == 2:
                                    return Pawn_2
                                if index == 3:
                                    return Queen
                                if index == 4:
                                    return Square

                            def update(self):
                                for i in board_units_f:
                                    screen.blit(pygame.transform.scale(
                                        pygame.image.load(i[0]).convert_alpha(), (60, 60)),
                                        (5 + indent + i[1][0] * cell_size,
                                         5 + indent + i[1][1] * cell_size))

                                for i in board_units_e:
                                    screen.blit(pygame.transform.scale(
                                        pygame.image.load(i[0]).convert_alpha(), (60, 60)),
                                        (5 + indent + i[1][0] * cell_size,
                                         5 + indent + i[1][1] * cell_size))

                                for i in moves:
                                    pygame.draw.circle(screen, pygame.Color(4, 255, 0),
                                                       (35 + indent + i[0][0] * cell_size,
                                                        35 + indent + i[0][1] * cell_size), 8)

                            def moving(self, coords):
                                del moves[:]
                                self.t_move = (int(time) * 60) * 15 // 100
                                for i in unit[0]:
                                    if coords_unit in i:
                                        m = unit[0].index(i)
                                        a = unit[0].pop(m)
                                        if coords in cells:
                                            cells.pop(cells.index(coords))
                                        else:
                                            a.pop(1)
                                            a.insert(1, coords)
                                            unit[0].insert(m, a)
                                        break
                                for i in unit[1]:
                                    if coords in i:
                                        ind = unit[1].pop(unit[1].index(i))[-1]
                                        if unit[1] == board_units_e:
                                            felled_figures_e[ind] = felled_figures_e.get(ind) + 1
                                        else:
                                            felled_figures_f[ind] = felled_figures_f.get(ind) + 1
                                        break

                            def time(self):
                                global dt
                                self.timer -= dt
                                self.t_move -= dt

                                if self.timer > 0:
                                    if len(str(round(self.timer) % 60)) == 2:
                                        t = str(round(self.timer) // 60) + ':' + str(round(self.timer) % 60)
                                    else:
                                        t = str(round(self.timer) // 60) + ':' + '0' + str(round(self.timer) % 60)

                                    txt = myfont.render(t, True, pygame.Color('dodgerblue'))
                                    screen.blit(txt, (210, 20))

                                    if self.t_move > 0:
                                        t = str(round(self.t_move))
                                        txt = myfont.render(t, True, pygame.Color('dodgerblue'))
                                        screen.blit(txt, (440, 20))
                                    else:
                                        if move:
                                            # когда синии упустили свой ход
                                            sc = pygame.display.set_mode((640, 480))
                                            pygame.display.set_caption("end")
                                            sc.fill('red')
                                            font = pygame.font.SysFont('Arial', 60)
                                            txt = font.render('Синии упустили свой ход.', True, (255, 255, 255))
                                            sc.blit(txt, (32, 20))
                                            txt = font.render('Красные выиграли!!!', True, (255, 255, 255))
                                            sc.blit(txt, (32, 150))
                                            pygame.display.update()
                                            pygame.display.flip()

                                        else:
                                            # когда красные упустили свой ход
                                            sc = pygame.display.set_mode((640, 480))
                                            pygame.display.set_caption("end")
                                            sc.fill('blue')
                                            font = pygame.font.SysFont('Arial', 50)
                                            txt = font.render('Красные упустили свой ход.', True, (255, 255, 255))
                                            sc.blit(txt, (32, 20))
                                            txt = font.render('Синии выиграли!!!', True, (255, 255, 255))
                                            sc.blit(txt, (32, 150))
                                            pygame.display.update()
                                            pygame.display.flip()

                                    pygame.display.flip()
                                    dt = clock.tick(30) / 1000
                                else:
                                    blui = felled_figures_f[1] + felled_figures_f[2] + felled_figures_f[3] +\
                                           felled_figures_f[4]
                                    red = felled_figures_e[1] + felled_figures_e[2] + felled_figures_e[3] +\
                                          felled_figures_e[4]
                                    if blui < red:
                                        sc = pygame.display.set_mode((640, 480))
                                        pygame.display.set_caption("end")
                                        sc.fill('blue')
                                        font = pygame.font.SysFont('Arial', 80)
                                        txt = font.render('Синии выиграли!!!', True, (255, 255, 255))
                                        sc.blit(txt, (32, 150))
                                        pygame.display.update()
                                        pygame.display.flip()
                                    elif red < blui:
                                        sc = pygame.display.set_mode((640, 480))
                                        pygame.display.set_caption("end")
                                        sc.fill('red')
                                        font = pygame.font.SysFont('Arial', 70)
                                        txt = font.render('Красные выиграли!!!', True, (255, 255, 255))
                                        sc.blit(txt, (32, 150))
                                        pygame.display.update()
                                        pygame.display.flip()
                                    else:
                                        sc = pygame.display.set_mode((640, 480))
                                        pygame.display.set_caption("end")
                                        sc.fill('green')
                                        font = pygame.font.SysFont('Arial', 60)
                                        txt = font.render('Ничья!', True, (255, 255, 255))
                                        sc.blit(txt, (32, 150))
                                        txt = font.render('Все проиграли', True, (255, 255, 255))
                                        sc.blit(txt, (32, 250))
                                        pygame.display.update()
                                        pygame.display.flip()

                            def move_flip(self):
                                for i in board_units_f:
                                    x, y = 7 - i[1][0], 7 - i[1][1]
                                    m = board_units_f.index(i)
                                    board_units_f[m].pop(1)
                                    n = board_units_f[m].pop(0)
                                    if move == False:
                                        n = n[:-4] + '2' + n[-4:]
                                    else:
                                        n = n[:-5] + n[-4:]
                                    board_units_f[m].insert(0, n)
                                    board_units_f[m].insert(1, (x, y))

                                for i in board_units_e:
                                    x, y = 7 - i[1][0], 7 - i[1][1]
                                    m = board_units_e.index(i)
                                    board_units_e[m].pop(1)
                                    n = board_units_e[m].pop(0)
                                    if move == False:
                                        n = n[:-4] + '2' + n[-4:]
                                    else:
                                        n = n[:-5] + n[-4:]
                                    board_units_e[m].insert(0, n)
                                    board_units_e[m].insert(1, (x, y))


                        class Pawn_1:
                            def __init__(self, coords):
                                self.x, self.y = coords[0], coords[1] - 1
                                self.move()

                            def move(self):
                                del moves[:]
                                if self.y != -1:
                                    m = True
                                    for i in unit[1]:
                                        if (self.x, self.y) in i:
                                            m = False
                                            break
                                    for i in unit[0]:
                                        if (self.x, self.y) in i:
                                            m = False
                                            break
                                    if m:
                                        moves.append([(self.x, self.y), 1])
                                moving = []
                                if 0 < self.x < 7:
                                    moving.append((self.x - 1, self.y))
                                    moving.append((self.x + 1, self.y))
                                    moving.append((self.x - 1, self.y + 1))
                                    moving.append((self.x + 1, self.y + 1))
                                elif 0 < self.x:
                                    moving.append((self.x - 1, self.y))
                                    moving.append((self.x - 1, self.y + 1))
                                else:
                                    moving.append((self.x + 1, self.y))
                                    moving.append((self.x + 1, self.y + 1))

                                for i in unit[1]:
                                    for j in moving:
                                        if j in i:
                                            moves.append([j, 1])

                        class Pawn_2:
                            def __init__(self, coords):
                                self.x, self.y = coords[0], coords[1] - 1
                                self.move()

                            def move(self):
                                del moves[:]
                                if self.y != -1:
                                    m = True
                                    for i in unit[1]:
                                        if (self.x, self.y) in i:
                                            m = False
                                            break
                                    for i in unit[0]:
                                        if (self.x, self.y) in i:
                                            m = False
                                            break
                                    if m:
                                        moves.append([(self.x, self.y), 1])
                                moving = []
                                if 0 < self.x < 7:
                                    moving.append((self.x - 1, self.y))
                                    moving.append((self.x + 1, self.y))
                                elif 0 < self.x:
                                    moving.append((self.x - 1, self.y))
                                else:
                                    moving.append((self.x + 1, self.y))

                                for i in unit[1]:
                                    for j in moving:
                                        if j in i:
                                            moves.append([j, 1])

                        class Queen:
                            def __init__(self, coords):
                                self.x, self.y = coords[0], coords[1]
                                self.move()

                            def move(self):
                                del moves[:]
                                if self.y != 0:
                                    y = self.y
                                    play = True
                                    while play:
                                        for i in unit[0]:
                                            if (self.x, y - 1) in i:
                                                play = False
                                                break
                                        if play:
                                            if y != 0:
                                                moves.append([(self.x, y - 1), 3])
                                            else:
                                                break
                                            for i in unit[1]:
                                                if (self.x, y - 1) in i:
                                                    play = False
                                                    break
                                            y -= 1

                                    if self.x != 0:
                                        x, y = self.x, self.y
                                        play = True
                                        while play:
                                            for i in unit[0]:
                                                if (x - 1, y - 1) in i:
                                                    play = False
                                                    break
                                            if play:
                                                if x != 0 and y != 0:
                                                    moves.append([(x - 1, y - 1), 3])
                                                else:
                                                    break
                                                for i in unit[1]:
                                                    if (x - 1, y - 1) in i:
                                                        play = False
                                                        break
                                                y -= 1
                                                x -= 1

                                    if self.x != 7:
                                        x, y = self.x, self.y
                                        play = True
                                        while play:
                                            for i in unit[0]:
                                                if (x + 1, y - 1) in i:
                                                    play = False
                                                    break
                                            if play:
                                                if x != 7 and y != 0:
                                                    moves.append([(x + 1, y - 1), 3])
                                                else:
                                                    break
                                                for i in unit[1]:
                                                    if (x + 1, y - 1) in i:
                                                        play = False
                                                        break
                                                y -= 1
                                                x += 1

                                if self.y != 7:
                                    y = self.y
                                    play = True
                                    while play:
                                        for i in unit[0]:
                                            if (self.x, y + 1) in i:
                                                play = False
                                                break
                                        if play:
                                            if y != 7:
                                                moves.append([(self.x, y + 1), 3])
                                            else:
                                                break
                                            for i in unit[1]:
                                                if (self.x, y + 1) == i[1]:
                                                    play = False
                                                    break
                                            y += 1

                                    if self.x != 0:
                                        x, y = self.x, self.y
                                        play = True
                                        while play:
                                            for i in unit[0]:
                                                if (x - 1, y + 1) in i:
                                                    play = False
                                                    break
                                            if play:
                                                if x != 0 and y != 7:
                                                    moves.append([(x - 1, y + 1), 3])
                                                else:
                                                    break
                                                for i in unit[1]:
                                                    if (x - 1, y + 1) in i:
                                                        play = False
                                                        break
                                                y += 1
                                                x -= 1

                                    if self.x != 7:
                                        x, y = self.x, self.y
                                        play = True
                                        while play:
                                            for i in unit[0]:
                                                if (x + 1, y + 1) in i:
                                                    play = False
                                                    break
                                            if play:
                                                if x != 7 and y != 7:
                                                    moves.append([(x + 1, y + 1), 3])
                                                else:
                                                    break
                                                for i in unit[1]:
                                                    if (x + 1, y + 1) in i:
                                                        play = False
                                                        break
                                                y += 1
                                                x += 1

                                if self.x != 0:
                                    x = self.x
                                    play = True
                                    while play:
                                        for i in unit[0]:
                                            if (x - 1, self.y) in i:
                                                play = False
                                                break
                                        if play:
                                            if x != 0:
                                                moves.append([(x - 1, self.y), 3])
                                            else:
                                                break
                                            for i in unit[1]:
                                                if (x - 1, self.y) == i[1]:
                                                    play = False
                                                    break
                                            x -= 1

                                if self.x != 7:
                                    x = self.x
                                    play = True
                                    while play:
                                        for i in unit[0]:
                                            if (x + 1, self.y) in i:
                                                play = False
                                                break
                                        if play:
                                            if x != 7:
                                                moves.append([(x + 1, self.y), 3])
                                            else:
                                                break
                                            for i in unit[1]:
                                                if (x + 1, self.y) == i[1]:
                                                    play = False
                                                    break
                                            x += 1

                        class Square:
                            def __init__(self, coords):
                                self.x, self.y = coords[0], coords[1]
                                self.move()

                            def move(self):
                                del moves[:]
                                if self.y != 0:
                                    x, y = self.x, self.y
                                    m = True
                                    for i in unit[0]:
                                        if (x, y - 1) in i:
                                            m = False
                                            break
                                    if m:
                                        moves.append([(x, y - 1), 4])

                                    if self.x != 0:
                                        x, y = self.x, self.y
                                        m = True
                                        for i in unit[0]:
                                            if (x - 1, y - 1) in i:
                                                m = False
                                                break
                                        if m:
                                            moves.append([(x - 1, y - 1), 4])

                                    if self.x != 7:
                                        x, y = self.x, self.y
                                        m = True
                                        for i in unit[0]:
                                            if (x + 1, y - 1) in i:
                                                m = False
                                                break
                                        if m:
                                            moves.append([(x + 1, y - 1), 4])

                                if self.y != 7:
                                    x, y = self.x, self.y
                                    m = True
                                    for i in unit[0]:
                                        if (x, y + 1) in i:
                                            m = False
                                            break
                                    if m:
                                        moves.append([(x, y + 1), 4])

                                    if self.x != 0:
                                        x, y = self.x, self.y
                                        m = True
                                        for i in unit[0]:
                                            if (x - 1, y + 1) in i:
                                                m = False
                                                break
                                        if m:
                                            moves.append([(x - 1, y + 1), 4])

                                    if self.x != 7:
                                        x, y = self.x, self.y
                                        m = True
                                        for i in unit[0]:
                                            if (x + 1, y + 1) in i:
                                                m = False
                                                break
                                        if m:
                                            moves.append([(x + 1, y + 1), 4])

                                if self.x != 0:
                                    x, y = self.x, self.y
                                    m = True
                                    for i in unit[0]:
                                        if (x - 1, y) in i:
                                            m = False
                                            break
                                    if m:
                                        moves.append([(x - 1, y), 4])

                                if self.x != 7:
                                    x, y = self.x, self.y
                                    m = True
                                    for i in unit[0]:
                                        if (x + 1, y) in i:
                                            m = False
                                            break
                                    if m:
                                        moves.append([(x + 1, y), 4])

                        board = Board(8, 8, timer, t_move)
                        running = True
                        arrow = pygame.image.load("arrow.png")
                        pygame.mouse.set_visible(False)

                        while running:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                                if board_units_e == []:
                                    l = level
                                    t = time * 60
                                    # создаем новые данны в бд
                                    con = sqlite3.connect('база_данных007.db')
                                    cur = con.cursor()
                                    cur.execute(f'''INSERT INTO Records VALUES ({l}, {t})''')
                                    con.commit()
                                    con.close()

                                    end_blue()
                                    exit()

                                if board_units_f == []:
                                    l = level
                                    t = time * 60 - timer
                                    # создаем новые данны в бд
                                    con = sqlite3.connect('база_данных007.db')
                                    cur = con.cursor()
                                    cur.execute(f'''INSERT INTO Records VALUES ({l}, {t})''')
                                    con.commit()
                                    con.close()
                                    end_red()
                                    exit()

                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    x, y = event.pos
                                    check = board.check(x, y)
                                    k = True
                                    if check:
                                        for i in unit[0]:
                                            if i[1] == check[1]:
                                                n = i[2]
                                                k = False
                                                coords_unit = (i[1])
                                                board.check_piece(n)(check[1])
                                                break

                                        if k:
                                            for i in moves:
                                                if check[1] in i:
                                                    board.moving(check[1])
                                                    if move:
                                                        move = False
                                                        unit = (board_units_e, board_units_f)
                                                    else:
                                                        move = True
                                                        unit = (board_units_f, board_units_e)

                                                    board.move_flip()

                            screen.fill(pygame.Color('gray19'))
                            board.render()
                            board.update()
                            if pygame.mouse.get_focused():
                                x, y = pygame.mouse.get_pos()
                                screen.blit(arrow, (x, y))
                            board.time()
                            pygame.display.update()

                            clock.tick(fps)

                        exit()
                    else:
                        # меняем цвет кнопки запуска, на неактивный
                        b_color = pygame.Color('Silver')
                        # убираем тект начала игры
                        b_text = 'Начать игру'
                # Если пользователь нажал на время игры
                # окно время хода пользователь редактировать не может
                if input_box.collidepoint(event.pos):
                    # меняем цвет
                    active = not active
                else:
                    active = False
                # изменение цвета в отрисовке
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
        # скин краба
        crab = pygame.image.load('img_crab.bmp')
        crab.set_colorkey((255, 255, 255))
        crab_rect = crab.get_rect(center=(250 // 2, 790 // 2))
        screen.blit(crab, crab_rect)
        # кнопка названия краба
        pygame.draw.rect(screen, crab_color, (30, 230, 140, 40))
        screen.blit(font.render('Краб', True, (0, 0, 0)), (50, 230))
        # скин осьминога
        octopus = pygame.image.load('img_Octopus.bmp')
        octopus.set_colorkey((255, 255, 255))
        octopus_rect = octopus.get_rect(center=(590 // 2, 820 // 2))
        screen.blit(octopus, octopus_rect)
        # кнопка названия осьминога
        pygame.draw.rect(screen, octupos_color, (245, 230, 140, 40))
        screen.blit(font.render('Осьминог', True, (0, 0, 0)), (249, 230))
        # скин черепахи
        turtole2 = pygame.image.load('img_turtel2.bmp')
        turtole2.set_colorkey((255, 255, 255))
        turtole2_rect = turtole2.get_rect(center=(950 // 2, 820 // 2))
        screen.blit(turtole2, turtole2_rect)
        # кнопка названия черепахи
        pygame.draw.rect(screen, turtole_color, (460, 230, 140, 40))
        screen.blit(font.render('Черепаха', True, (0, 0, 0)), (460, 230))

        # прямоугольник для кнопки возврата
        pygame.draw.rect(screen, (57, 255, 20), (20, 470, 140, 70))
        # прямоугольник для кнопки начать игру
        pygame.draw.rect(screen, b_color, (440, 470, 180, 70))
        screen.blit(font.render('Вернуться', True, (0, 0, 0)), (20, 480))
        screen.blit(font.render('Время игры (в минутах):', True, (57, 255, 20)), (10, 10))
        screen.blit(font.render('Время хода (в секундах):', True, (57, 255, 20)), (10, 100))
        screen.blit(font.render(b_text, True, (0, 0, 0)), (450, 480))
        # Размещаем текст в окне
        # эта проверка не позволит пользователю, выйти за рамки окна ввода
        # если текст превышает длинну окна, то у него отрезаются первые 10 символов
        if len(text) > 10:
            text = text[0: 10]
        txt_surface = font.render(text, True, color)
        # проверка время хода
        # что бы не было ошибок при вводе времени игры
        if text.isdigit() and 25 >= int(text) >= 5:
            # если все оказалось верно, то берем 15% от всего времени игры
            # переменная для обозначения время хода игры
            time_hod = str(int(text) * 60 * 0.15)
            txt_surface2 = font.render(time_hod, True, color)
        else:
            # если текст неправильный, то сообщение об ошибке
            time_hod = 'Error'
            txt_surface2 = font.render(time_hod, True, color)
        # Удлиняем поле ввода, если вводимый текст слишком длинный
        width = 220
        input_box.w = width
        # отражаем текст в окнах
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.draw.rect(screen, color, input_box2, 2)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(30)


# поздравление синих
def end_blue():
    sc = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("end")
    sc.fill('blue')
    pygame.display.update()
    pygame.display.flip()
    fn = pygame.font.SysFont('Arial', 70)
    txt = fn.render('Синии выиграли!!!', True, (255, 255, 255))
    sc.blit(txt, (32, 150))
    pygame.display.update()
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


# поздравление красных
def end_red():
    sc = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("end")
    sc.fill('red')
    pygame.display.update()
    pygame.display.flip()
    fn = pygame.font.SysFont('Arial', 70)
    txt = fn.render('Красные выиграли!!!', True, (255, 255, 255))
    sc.blit(txt, (32, 150))
    pygame.display.update()
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


a = Menu()
