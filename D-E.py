import pygame

pygame.init()
size = 700, 700
indent = 70
part = 20
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 50)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.board = []
        n = 0
        for y in range(self.height):
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

        self.cell_size = 70

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

        pygame.draw.rect(screen, pygame.Color('black'), (indent - 4, indent - 4,
                                                         self.cell_size * 8 + 8,
                                                         self.cell_size * 8 + 8), 4)
        pygame.draw.rect(screen, pygame.Color("gold"), (indent - part - 4, indent - part - 4,
                                                        self.cell_size * 8 + part * 2 + 8,
                                                        self.cell_size * 8 + part * 2 + 8), part)


class Turtle:
    def __init__(self):
        pass


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

    screen.fill((163, 110, 255))
    meny.draw(screen, 100, 100, 75)
    # board.render()
    # screen.blit(pygame.transform.scale(
    #    pygame.image.load('cyber_Turtle_enemy.png').convert_alpha(), (60, 60)), (215, 215))
    # screen.blit(pygame.transform.scale(
    #    pygame.image.load('cyber_Turtle_frendly.png').convert_alpha(), (60, 60)), (215, 285))
    pygame.display.flip()

pygame.quit()
