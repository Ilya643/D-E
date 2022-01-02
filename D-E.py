from typing import Any

import pygame

pygame.init()
size = 900, 700
indent = 70
part = 20
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 50)
Units = ['turtle']
turtle_move = (700, 70, 120, 120)
units_peek = (700, 0, 900, 700)
turtle_active = False
cell_size = 70
picture = 'cyber_Turtle_frendly.png'
coords = ''


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
                         units_peek)  # отсюда будем перетаскивать фигуры

        """ Ф и г у р а 1 """
        pygame.draw.rect(screen, pygame.Color('deeppink2'), (700, 70, 900, 220))
        pygame.draw.rect(screen, pygame.Color('black'), (700, 70, 120, 120), 1)
        screen.blit(pygame.transform.scale(
            pygame.image.load('cyber_Turtle_frendly.png').convert_alpha(), (100, 100)), (710, 80))

    def check(self, x, y):
        for i in self.slovar_with_coords:
            coords = self.slovar_with_coords.get(i)
            if coords[0] <= x <= coords[0] + coords[2] and coords[1] <= y <= coords[1] + coords[3]:
                return [True, i]
        if units_peek[0] <= x <= units_peek[0] + units_peek[2] and units_peek[1]\
                <= y <= units_peek[1] + units_peek[3]:
            if turtle_move[0] <= x <= turtle_move[0] + turtle_move[2] and \
                    turtle_move[1] <= y <= turtle_move[1] + turtle_move[3]:
                return 'turtle'
        return None


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
            print(board.check(x, y))
            if board.check(x, y) is not None:
                if board.check(x, y)[0] and turtle_active:
                    arrow = pygame.image.load("arrow.png")
                    turtle_active = False
                    check = board.check(x, y)
                    if check[0] == True and check[1][1] > 3:
                        print('рисуем фигуру')
                if board.check(x, y) == 'turtle':
                    arrow = pygame.image.load('cyber_Turtle_frendly.png')
                    turtle_active = True





    screen.fill((163, 110, 255))
    board.render()  # показываем дисплей
    if pygame.mouse.get_focused():
        x, y = pygame.mouse.get_pos()
        screen.blit(arrow, (x, y))
    pygame.display.update()

pygame.quit()
