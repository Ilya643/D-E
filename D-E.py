import pygame

pygame.init()
size = 560, 560
screen = pygame.display.set_mode(size)

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
                    print(1)
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
                    pygame.draw.rect(screen, pygame.Color(0, 0, 0),
                                     (x * self.cell_size, y * self.cell_size,
                                      self.cell_size, self.cell_size), 0)
                else:
                    pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                     (x * self.cell_size, y * self.cell_size,
                                      self.cell_size, self.cell_size), 0)


board = Board(8, 8)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    board.render()
    pygame.display.flip()

pygame.quit()
