import pygame

pygame.init()
size = 560, 560
screen = pygame.display.set_mode(size)

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.board = []
        for y in range(self.height):
            stroka = []
            for x in range(self.width):
                stroka.append(0)
            self.board.append(stroka)

        self.cell_size = 70

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(0, 0, 0),
                                 (x * self.cell_size, y * self.cell_size,
                                  self.cell_size, self.cell_size), 5)


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
