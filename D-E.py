

import pygame

pygame.init()
size = 900, 700
pygame.display.set_caption('D&E')
screen = pygame.display.set_mode(size)

indent = 70
part = 20
units_peek = (700, 0, 900, 700)
cell_size = 70
coords_unit = 0

board_units_f = [['cyber_Turtle_frendly.png', (0, 6), 1], ['cyber_Turtle_frendly.png', (1, 6), 1],
                 ['cyber_Turtle_frendly.png', (2, 6), 1], ['cyber_Turtle_frendly.png', (3, 6), 2],
                 ['cyber_Turtle_frendly.png', (4, 6), 2], ['cyber_Turtle_frendly.png', (5, 6), 1],
                 ['cyber_Turtle_frendly.png', (6, 6), 1], ['cyber_Turtle_frendly.png', (7, 6), 1],
                 ['cyber_Turtle_frendly.png', (3, 7), 3], ['cyber_Turtle_frendly.png', (4, 7), 4]]
board_units_e = [['cyber_Turtle_enemy.png', (1, 1)], ['cyber_Turtle_enemy.png', (2, 1)],
                 ['cyber_Turtle_enemy.png', (3, 1)], ['cyber_Turtle_enemy.png', (4, 1)],
                 ['cyber_Turtle_enemy.png', (5, 1)], ['cyber_Turtle_enemy.png', (6, 1)],
                 ['cyber_Turtle_enemy.png', (2, 0)], ['cyber_Turtle_enemy.png', (3, 0)],
                 ['cyber_Turtle_enemy.png', (4, 0)], ['cyber_Turtle_enemy.png', (5, 0)]]
moves = []



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
                    pygame.draw.rect(screen, pygame.Color("gold"),
                                     (indent + x * cell_size, indent + y * cell_size,
                                      cell_size, cell_size), 0)
                self.slovar_with_coords[x, y] = (
                    x * cell_size + indent, y * cell_size + indent, cell_size,
                    cell_size)

        pygame.draw.rect(screen, pygame.Color('black'), (indent - 4, indent - 4,
                                                         cell_size * 8 + 8,
                                                         cell_size * 8 + 8), 4)
        pygame.draw.rect(screen, pygame.Color("gold"), (indent - part - 4, indent - part - 4,
                                                        cell_size * 8 + part * 2 + 8,
                                                        cell_size * 8 + part * 2 + 8), part)
        pygame.draw.rect(screen, pygame.Color('darkslategray4'),
                         units_peek)

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
            pygame.draw.circle(screen, pygame.Color('darkslategray4'), (35 + indent + i[0][0] * cell_size,
                                                                        35 + indent + i[0][1] * cell_size), 8)

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


    def moving(self, coords):
        del moves[:]
        for i in board_units_f:
            if coords_unit in i:
                m = board_units_f.index(i)
                a = board_units_f.pop(m)
                a.pop(1)
                a.insert(1, coords)
                board_units_f.insert(m, a)
                break
        for i in board_units_e:
            if coords in i:
                board_units_e.pop(board_units_e.index(i))
                break


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


    def moving(self, coords):
        del moves[:]
        for i in board_units_f:
            if coords_unit in i:
                m = board_units_f.index(i)
                a = board_units_f.pop(m)
                a.pop(1)
                a.insert(1, coords)
                board_units_f.insert(m, a)
                break
        for i in board_units_e:
            if coords in i:
                board_units_e.pop(board_units_e.index(i))
                break


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
                if play:
                    if y != 0:
                        moves.append([(self.x, y - 1), 3])
                    else:
                        break
                    for i in board_units_e:
                        if (self.x, y - 1) in i:
                            play = False
                    y -= 1

            if self.x != 0:
                x, y = self.x, self.y
                play = True
                while play:
                    for i in board_units_f:
                        if (x - 1, y - 1) in i:
                            play = False
                    if play:
                        if x != 0 and y != 0:
                            moves.append([(x - 1, y - 1), 3])
                        else:
                            break
                        for i in board_units_e:
                            if (x - 1, y - 1) in i:
                                play = False
                        y -= 1
                        x -= 1

            if self.x != 7:
                x, y = self.x, self.y
                play = True
                while play:
                    for i in board_units_f:
                        if (x + 1, y - 1) in i:
                            play = False
                    if play:
                        if x != 7 and y != 0:
                            moves.append([(x + 1, y - 1), 3])
                        else:
                            break
                        for i in board_units_e:
                            if (x + 1, y - 1) in i:
                                play = False
                        y -= 1
                        x += 1

        if self.y != 7:
            y = self.y
            play = True
            while play:
                for i in board_units_f:
                    if (self.x, y + 1) in i:
                        play = False
                if play:
                    if y != 7:
                        moves.append([(self.x, y + 1), 3])
                    else:
                        break
                    for i in board_units_e:
                        if (self.x, y + 1) == i[1]:
                            play = False
                    y += 1

            if self.x != 0:
                x, y = self.x, self.y
                play = True
                while play:
                    for i in board_units_f:
                        if (x - 1, y + 1) in i:
                            play = False
                    if play:
                        if x != 0 and y != 7:
                            moves.append([(x - 1, y + 1), 3])
                        else:
                            break
                        for i in board_units_e:
                            if (x - 1, y + 1) in i:
                                play = False
                        y += 1
                        x -= 1

            if self.x != 7:
                x, y = self.x, self.y
                play = True
                while play:
                    for i in board_units_f:
                        if (x + 1, y + 1) in i:
                            play = False
                    if play:
                        if x != 7 and y != 7:
                            moves.append([(x + 1, y + 1), 3])
                        else:
                            break
                        for i in board_units_e:
                            if (x + 1, y + 1) in i:
                                play = False
                        y += 1
                        x += 1

        if self.x != 0:
            x = self.x
            play = True
            while play:
                for i in board_units_f:
                    if (x - 1, self.y) in i:
                        play = False
                if play:
                    if x != 0:
                        moves.append([(x - 1, self.y), 3])
                    else:
                        break
                    for i in board_units_e:
                        if (x - 1, self.y) == i[1]:
                            play = False
                    x -= 1

        if self.x != 7:
            x = self.x
            play = True
            while play:
                for i in board_units_f:
                    if (x + 1, self.y) in i:
                        play = False
                if play:
                    if x != 7:
                        moves.append([(x + 1, self.y), 3])
                    else:
                        break
                    for i in board_units_e:
                        if (x + 1, self.y) == i[1]:
                            play = False
                    x += 1

    def moving(self, coords):
        del moves[:]
        for i in board_units_f:
            if coords_unit in i:
                m = board_units_f.index(i)
                a = board_units_f.pop(m)
                a.pop(1)
                a.insert(1, coords)
                board_units_f.insert(m, a)
                break
        for i in board_units_e:
            if coords in i:
                board_units_e.pop(board_units_e.index(i))
                break


class Square:
    def __init__(self, coords):
        print('Square')


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
                            board.check_piece(i[1])(i[0]).moving(check[1])




    screen.fill((163, 110, 255))
    board.render()
    board.update()
    if pygame.mouse.get_focused():
        x, y = pygame.mouse.get_pos()
        screen.blit(arrow, (x, y))
    pygame.display.update()

pygame.quit()
