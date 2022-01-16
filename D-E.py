from random import sample
import pygame
import sqlite3

pygame.init()
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

level = 2
time = 10
skin = 'turtole'
timer = time * 60
t_move = timer * 15 // 100
FPS = 60

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
felled_figures_e = {1: 0, 2: 0}
moves = []

cells = [(0, 2), (0, 3), (0, 4), (0, 5),
         (1, 2), (1, 3), (1, 4), (1, 5),
         (2, 2), (2, 3), (2, 4), (2, 5),
         (3, 2), (3, 3), (3, 4), (3, 5),
         (4, 2), (4, 3), (4, 4), (4, 5),
         (5, 2), (5, 3), (5, 4), (5, 5),
         (6, 2), (6, 3), (6, 4), (6, 5),
         (7, 2), (7, 3), (7, 4), (7, 5)]

cells = sample(cells, 8)
if level == 1:
    cells = [cells[4:6], cells[6:], cells[:4]]
elif level == 2:
    cells = [cells[2:4], cells[4:], cells[:2]]
else:
    cells = [cells[:2], cells[2:]]
print(cells)



class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.slovar_with_coords = {}
        self.board = []
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
        pygame.draw.rect(screen, pygame.Color(255, 170, 0), (indent - part - 4, indent - part - 4,
                                                        cell_size * 8 + part * 2 + 8,
                                                        cell_size * 8 + part * 2 + 8), part)
        pygame.draw.rect(screen, pygame.Color('darkslategray4'),
                         units_peek)

        self.image = pygame.image.load('Cyber_Turtle_Enemy_Executioner.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image, 180)
        screen.blit(pygame.transform.scale(self.image, (80, 80)), (710, 60))

        self.image = pygame.image.load('Cyber_Turtle_Enemy_Duke.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image, 180)
        screen.blit(pygame.transform.scale(self.image, (80, 80)), (710, 150))


        self.image = pygame.image.load('Cyber_Turtle_Friendly_Executioner.png').convert_alpha()
        screen.blit(pygame.transform.scale(self.image, (80, 80)), (710, 270))

        self.image = pygame.image.load('Cyber_Turtle_Friendly_Defender.png').convert_alpha()
        screen.blit(pygame.transform.scale(self.image, (80, 80)), (710, 360))

        self.image = pygame.image.load('Cyber_Turtle_Friendly_King.png').convert_alpha()
        screen.blit(pygame.transform.scale(self.image, (80, 80)), (710, 450))

        self.image = pygame.image.load('Cyber_Turtle_Friendly_Jumper.png').convert_alpha()
        screen.blit(pygame.transform.scale(self.image, (80, 80)), (710, 540))

        numbers_e = [felled_figures_e[1], felled_figures_e[2]]
        numbers_f = [felled_figures_f[1], felled_figures_f[2], felled_figures_f[3], felled_figures_f[4]]

        y1 = 95
        for i in numbers_e:
            textsurface = myfont.render(str(i), False, (0, 0, 0))
            screen.blit(textsurface, (810, y1))
            y1 += 90

        y1 += 30
        for i in numbers_f:
            textsurface = myfont.render(str(i), False, (0, 0, 0))
            screen.blit(textsurface, (810, y1))
            y1 += 90

        y1 = 585
        for i in range(1, 9):
            textsurface = myfont.render(str(i), False, (0, 0, 0))
            screen.blit(textsurface, (52, y1))
            y1 -= 70

        x1 = 95
        for i in letters:
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
            if coords[0] <= x <= coords[0] + coords[2] and coords[1] <= y <= coords[1] + coords[3]:
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
                pygame.image.load(i[0]).convert_alpha(), (60, 60)), (5 + indent + i[1][0] * cell_size,
                                                                     5 + indent + i[1][1] * cell_size))

        for i in board_units_e:
            screen.blit(pygame.transform.scale(
                pygame.image.load(i[0]).convert_alpha(), (60, 60)), (5 + indent + i[1][0] * cell_size,
                                                                     5 + indent + i[1][1] * cell_size))

        for i in moves:
            pygame.draw.circle(screen, pygame.Color(4, 255, 0), (35 + indent + i[0][0] * cell_size,
                                                                 35 + indent + i[0][1] * cell_size), 8)

    def moving(self, coords):
        del moves[:]
        global t_move
        t_move = (time * 60) * 15 // 100
        for i in board_units_f:
            if coords_unit in i:
                m = board_units_f.index(i)
                a = board_units_f.pop(m)
                if coords in cells[1]:
                    cells[1].pop(cells[1].index(coords))
                    print('Вы наступили на плохую клетку! ИИ ходит два раза')
                elif coords in cells[0]:
                    cells[0].pop(cells[0].index(coords))
                    print('Вы наступили на плохую клетку! Ваша фигура умерла')
                    break
                elif len(cells) == 3 and coords in cells[2]:
                    cells[2].pop(cells[2].index(coords))
                    print('Вы наступили на хорошую клетку! Вам выдан дополнительный ход')
                a.pop(1)
                a.insert(1, coords)
                board_units_f.insert(m, a)
                break
        for i in board_units_e:
            if coords in i:
                ind = board_units_e.pop(board_units_e.index(i))[-1]
                felled_figures_e[ind] = felled_figures_e.get(ind) + 1
                break

    def time(self):
        global timer, t_move, dt
        timer -= dt
        t_move -= dt

        if timer > 0:
            if len(str(round(timer) % 60)) == 2:
                t = str(round(timer) // 60) + ':' + str(round(timer) % 60)
            else:
                t = str(round(timer) // 60) + ':' + '0' + str(round(timer) % 60)

            txt = myfont.render(t, True, pygame.Color('dodgerblue'))
            screen.blit(txt, (210, 20))

            if t_move > 0:
                t = str(round(t_move))
                txt = myfont.render(t, True, pygame.Color('dodgerblue'))
                screen.blit(txt, (440, 20))
            pygame.display.flip()
            dt = clock.tick(30) / 1000



class Pawn_1:
    def __init__(self, coords):
        self.x, self.y = coords[0], coords[1] - 1
        self.move()

    def move(self):
        del moves[:]
        if self.y != -1:
            m = True
            for i in board_units_e:
                if (self.x, self.y) in i:
                    m = False
                    break
            for i in board_units_f:
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

        for i in board_units_e:
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
            for i in board_units_e:
                if (self.x, self.y) in i:
                    m = False
                    break
            for i in board_units_f:
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

        for i in board_units_e:
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
                for i in board_units_f:
                    if (self.x, y - 1) in i:
                        play = False
                        break
                if play:
                    if y != 0:
                        moves.append([(self.x, y - 1), 3])
                    else:
                        break
                    for i in board_units_e:
                        if (self.x, y - 1) in i:
                            play = False
                            break
                    y -= 1

            if self.x != 0:
                x, y = self.x, self.y
                play = True
                while play:
                    for i in board_units_f:
                        if (x - 1, y - 1) in i:
                            play = False
                            break
                    if play:
                        if x != 0 and y != 0:
                            moves.append([(x - 1, y - 1), 3])
                        else:
                            break
                        for i in board_units_e:
                            if (x - 1, y - 1) in i:
                                play = False
                                break
                        y -= 1
                        x -= 1

            if self.x != 7:
                x, y = self.x, self.y
                play = True
                while play:
                    for i in board_units_f:
                        if (x + 1, y - 1) in i:
                            play = False
                            break
                    if play:
                        if x != 7 and y != 0:
                            moves.append([(x + 1, y - 1), 3])
                        else:
                            break
                        for i in board_units_e:
                            if (x + 1, y - 1) in i:
                                play = False
                                break
                        y -= 1
                        x += 1

        if self.y != 7:
            y = self.y
            play = True
            while play:
                for i in board_units_f:
                    if (self.x, y + 1) in i:
                        play = False
                        break
                if play:
                    if y != 7:
                        moves.append([(self.x, y + 1), 3])
                    else:
                        break
                    for i in board_units_e:
                        if (self.x, y + 1) == i[1]:
                            play = False
                            break
                    y += 1

            if self.x != 0:
                x, y = self.x, self.y
                play = True
                while play:
                    for i in board_units_f:
                        if (x - 1, y + 1) in i:
                            play = False
                            break
                    if play:
                        if x != 0 and y != 7:
                            moves.append([(x - 1, y + 1), 3])
                        else:
                            break
                        for i in board_units_e:
                            if (x - 1, y + 1) in i:
                                play = False
                                break
                        y += 1
                        x -= 1

            if self.x != 7:
                x, y = self.x, self.y
                play = True
                while play:
                    for i in board_units_f:
                        if (x + 1, y + 1) in i:
                            play = False
                            break
                    if play:
                        if x != 7 and y != 7:
                            moves.append([(x + 1, y + 1), 3])
                        else:
                            break
                        for i in board_units_e:
                            if (x + 1, y + 1) in i:
                                play = False
                                break
                        y += 1
                        x += 1

        if self.x != 0:
            x = self.x
            play = True
            while play:
                for i in board_units_f:
                    if (x - 1, self.y) in i:
                        play = False
                        break
                if play:
                    if x != 0:
                        moves.append([(x - 1, self.y), 3])
                    else:
                        break
                    for i in board_units_e:
                        if (x - 1, self.y) == i[1]:
                            play = False
                            break
                    x -= 1

        if self.x != 7:
            x = self.x
            play = True
            while play:
                for i in board_units_f:
                    if (x + 1, self.y) in i:
                        play = False
                        break
                if play:
                    if x != 7:
                        moves.append([(x + 1, self.y), 3])
                    else:
                        break
                    for i in board_units_e:
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
            for i in board_units_f:
                if (x, y - 1) in i:
                    m = False
                    break
            if m:
                moves.append([(x, y - 1), 4])

            if self.x != 0:
                x, y = self.x, self.y
                m = True
                for i in board_units_f:
                    if (x - 1, y - 1) in i:
                        m = False
                        break
                if m:
                    moves.append([(x - 1, y - 1), 4])

            if self.x != 7:
                x, y = self.x, self.y
                m = True
                for i in board_units_f:
                    if (x + 1, y - 1) in i:
                        m = False
                        break
                if m:
                    moves.append([(x + 1, y - 1), 4])

        if self.y != 7:
            x, y = self.x, self.y
            m = True
            for i in board_units_f:
                if (x, y + 1) in i:
                    m = False
                    break
            if m:
                moves.append([(x, y + 1), 4])

            if self.x != 0:
                x, y = self.x, self.y
                m = True
                for i in board_units_f:
                    if (x - 1, y + 1) in i:
                        m = False
                        break
                if m:
                    moves.append([(x - 1, y + 1), 4])

            if self.x != 7:
                x, y = self.x, self.y
                m = True
                for i in board_units_f:
                    if (x + 1, y + 1) in i:
                        m = False
                        break
                if m:
                    moves.append([(x + 1, y + 1), 4])

        if self.x != 0:
            x, y = self.x, self.y
            m = True
            for i in board_units_f:
                if (x - 1, y) in i:
                    m = False
                    break
            if m:
                moves.append([(x - 1, y), 4])

        if self.x != 7:
            x, y = self.x, self.y
            m = True
            for i in board_units_f:
                if (x + 1, y) in i:
                    m = False
                    break
            if m:
                moves.append([(x + 1, y), 4])


board = Board(8, 8)
running = True
arrow = pygame.image.load("arrow.png")
pygame.mouse.set_visible(False)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            check = board.check(x, y)
            k = True
            if check:
                for i in board_units_f:
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

    screen.fill(pygame.Color('gray19'))
    board.render()
    board.update()
    if pygame.mouse.get_focused():
        x, y = pygame.mouse.get_pos()
        screen.blit(arrow, (x, y))
    board.time()
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
