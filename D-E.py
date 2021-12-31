from typing import Any

import pygame

pygame.init()
size = 900, 700
indent = 70
part = 20
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 50)
Units = ['turtle']
turtle_active = False


class Board:
    def __init__(self, width, height):
        self.turtle_move = (700, 70, 120, 120)
        self.width = width
        self.height = height
        self.slovar_with_coords = {}
        self.board = []
        self.units_peek = (700, 0, 900, 700)
        self.cell_size = 70
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
                                     (indent + x * self.cell_size, indent + y * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                else:
                    pygame.draw.rect(screen, pygame.Color("gold"),
                                     (indent + x * self.cell_size, indent + y * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                self.slovar_with_coords[x, y] = (
                    x * self.cell_size + indent, y * self.cell_size + indent, self.cell_size,
                    self.cell_size)

        pygame.draw.rect(screen, pygame.Color('black'), (indent - 4, indent - 4,
                                                         self.cell_size * 8 + 8,
                                                         self.cell_size * 8 + 8), 4)
        pygame.draw.rect(screen, pygame.Color("gold"), (indent - part - 4, indent - part - 4,
                                                        self.cell_size * 8 + part * 2 + 8,
                                                        self.cell_size * 8 + part * 2 + 8), part)
        pygame.draw.rect(screen, pygame.Color('darkslategray4'),
                         self.units_peek)  # отсюда будем перетаскивать фигуры

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
        if self.units_peek[0] <= x <= self.units_peek[0] + self.units_peek[2] and self.units_peek[
            1] <= y <= self.units_peek[1] + self.units_peek[3]:
            if self.turtle_move[0] <= x <= self.turtle_move[0] + self.turtle_move[2] and \
                    self.turtle_move[1] <= y <= self.turtle_move[1] + self.turtle_move[3]:
                return 'turtle'
        return None


# def Turtle(self, cell_num):
#    screen.blit(pygame.transform.scale(
#        pygame.image.load('cyber_Turtle_frendly.png').convert_alpha(), (60, 60)),
#       (self.slovar_with_coords[cell_num[0], cell_num[1]]))


# class Turtle:
# def __init__(self):
#  super(Turtle, self).__init__(Board)
#  self.hp = 10
#   self.damage = 2

# def enemy(self, cell_num):
#    pass

#  def friend(self, cell_num):
#     pass


class Meny:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        self._option_surfaces.append(font.render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)

    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction,
                                                len(self._option_surfaces) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                pygame.draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)


meny = Meny()
board = Board(8, 8)
meny.append_option('aleksey_', lambda: print(1))
meny.append_option('_fursenko', quit)

running = True
arrow = pygame.image.load("arrow.png")
pygame.mouse.set_visible(False)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                meny.switch(-1)
            elif event.key == pygame.K_s:
                meny.switch(1)
            elif event.key == pygame.K_SPACE:
                meny.select()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(board.check(x, y))
            if board.check(x, y) is not None:
                if board.check(x, y)[0] and turtle_active:
                    arrow = pygame.image.load("arrow.png")
                    #board.Turtle(board.check(x, y)[1])
                if board.check(x, y) == 'turtle':
                    arrow = pygame.image.load('cyber_Turtle_frendly.png')
                    turtle_active = True

    screen.fill((163, 110, 255))
    meny.draw(screen, 100, 100, 75)
    board.render()  # показываем дисплей
    if pygame.mouse.get_focused():
        x, y = pygame.mouse.get_pos()
        screen.blit(arrow, (x, y))
    pygame.display.update()

pygame.quit()
