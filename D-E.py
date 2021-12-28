import pygame

pygame.init()
size = 700, 700
indent = 70
part = 15
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 20)



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

        pygame.draw.rect(screen, pygame.Color("saddlebrown"), (indent - 4, indent - 4,
                                                        self.cell_size * 8 + 8,
                                                        self.cell_size * 8 + 8), 4)
        pygame.draw.rect(screen, pygame.Color("gold"), (indent - part - 4, indent - part - 4,
                                                        self.cell_size * 8 + part * 2 + 8,
                                                        self.cell_size * 8 + part * 2 + 8), part)



board = Board(8, 8)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((163, 110, 255))
    board.render()
    pygame.display.flip()

pygame.quit()
