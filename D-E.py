from typing import Any

import pygame

pygame.init()
size = 900, 700
screen = pygame.display.set_mode(size)

indent = 70
part = 20
Units = ['turtle']
turtle_move = (700, 70, 120, 120)
units_peek = (700, 0, 900, 700)
turtle_active = False
cell_size = 70

board_units_f = [['cyber_Turtle_frendly.png', (0, 6)], ['cyber_Turtle_frendly.png', (1, 6)],
                 ['cyber_Turtle_frendly.png', (2, 6)], ['cyber_Turtle_frendly.png', (3, 6)],
                 ['cyber_Turtle_frendly.png', (4, 6)], ['cyber_Turtle_frendly.png', (5, 6)],
                 ['cyber_Turtle_frendly.png', (6, 6)], ['cyber_Turtle_frendly.png', (7, 6)],
                 ['cyber_Turtle_frendly.png', (3, 7)], ['cyber_Turtle_frendly.png', (4, 7)]]
board_units_e = [['cyber_Turtle_enemy.png', (1, 1)], ['cyber_Turtle_enemy.png', (2, 1)],
                 ['cyber_Turtle_enemy.png', (3, 1)], ['cyber_Turtle_enemy.png', (4, 1)],
                 ['cyber_Turtle_enemy.png', (5, 1)], ['cyber_Turtle_enemy.png', (6, 1)],
                 ['cyber_Turtle_enemy.png', (2, 0)], ['cyber_Turtle_enemy.png', (3, 0)],
                 ['cyber_Turtle_enemy.png', (4, 0)], ['cyber_Turtle_enemy.png', (5, 0)]]



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

    def update(self):
        for i in board_units_f:
            screen.blit(pygame.transform.scale(
                pygame.image.load(i[0]).convert_alpha(), (60, 60)), (5 + indent + i[1][0] * cell_size,
                                                                     5 + indent + i[1][1] * cell_size))

        for i in board_units_e:
            screen.blit(pygame.transform.scale(
                pygame.image.load(i[0]).convert_alpha(), (60, 60)), (5 + indent + i[1][0] * cell_size,
                                                                     5 + indent + i[1][1] * cell_size))

board = Board(8, 8)
running = True
arrow = pygame.image.load("arrow.png")
pygame.mouse.set_visible(False)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
            # x, y = event.pos
            # print(board.check(x, y))
            # if board.check(x, y) is not None:
                # if board.check(x, y)[0] and turtle_active:
                    # arrow = pygame.image.load("arrow.png")
                    # turtle_active = False
                    # check = board.check(x, y)
                    # if check[0] == True and check[1][1] > 3:
                        # board_units.append(['cyber_Turtle_frendly.png', check[1]])
                # if board.check(x, y) == 'turtle':
                    # arrow = pygame.image.load('cyber_Turtle_frendly.png')
                    # turtle_active = True

    screen.fill((163, 110, 255))
    board.render()
    board.update()
    if pygame.mouse.get_focused():
        x, y = pygame.mouse.get_pos()
        screen.blit(arrow, (x, y))
    pygame.display.update()

pygame.quit()
