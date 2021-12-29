import pygame, sys


def Intersect(x1, x2, y1, y2, db1, db2):
    if (x1 > x2 - db1) and (x1 < x2 + db2) and (y1 > y2 - db1) and (y1 < y2 + db2):
        return 1
    else:
        return 0


window = pygame.display.set_mode((800, 670))
pygame.display.set_caption('Archer')
screen = pygame.Surface((800, 640))
info = pygame.Surface((800, 30))


class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0, 0, 0))

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))


class Menu:
    def __init__(self, punkts=[400, 350, u'Punkt', (250, 250, 30), (250, 30, 250)]):
        self.punkts = punkts

    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1] - 30))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1] - 30))

    def menu(self):
        done = True
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            info.fill((0, 100, 200))
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        exit()
            window.blit(info, (0, 0))
            window.blit(screen, (0, 30))
            pygame.display.flip()


hero = Sprite(400, 600, 'hero.png')
meta = Sprite(300, 0, 'object.png')
arrow = Sprite(-100, 600, 'arrow.png')

meta.move = True
hero.move_right = True
hero.move_down = True
arrow.push = False
meta.speed = 0
arrow.speed = 0.5
score = 0
lifes = 3

pygame.font.init()
score_f = pygame.font.SysFont('Arial', 32)
lifes_f = pygame.font.SysFont('Arial', 32)
end = pygame.font.SysFont('Times new roman', 80)
again = pygame.font.SysFont('Times new roman', 40)

punkts = [(350, 300, u'Play', (11, 0, 77), (250, 250, 30), 0),
          (350, 340, u'Exit', (11, 0, 77), (250, 250, 30), 1)]
game = Menu(punkts)
game.menu()

done = True
pygame.key.set_repeat(1, 1)
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                game.menu()

        if e.type == pygame.MOUSEMOTION:
            pygame.mouse.set_visible(False)
            p = pygame.mouse.get_pos()
            if p[0] > 0 and p[0] < 760:
                hero.x = p[0]
            if p[1] < 600 and p[1] > 200:
                hero.y = p[1]
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                if arrow.push == False:
                    arrow.x = hero.x + 4
                    arrow.y = hero.y
                    arrow.push = True

    y = -300
    x = -200

    if meta.move == True:
        meta.x += meta.speed
        if meta.x > 760:
            meta.move = False
    else:
        meta.x -= meta.speed
        if meta.x < -10:
            meta.move = True

    if arrow.y < 0:
        arrow.push = False
        lifes -= 1
    if arrow.push == False:
        arrow.x = -100
        arrow.y = 600
    else:
        arrow.y -= arrow.speed

    if Intersect(arrow.x, meta.x, arrow.y, meta.y, 5, 40) == True:
        arrow.push = False
        meta.speed += 0.2
        arrow.speed += 0.2
        score += 1
    if lifes <= 0:
        y = 300
        x = 450
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                lifes = 3
                score = 0
                meta.speed = 0
            else:
                exit()

    screen.fill((50, 50, 50))
    info.fill((45, 80, 45))

    arrow.render()
    meta.render()
    hero.render()

    screen.blit(end.render('Game Over', 1, (210, 120, 200)), (200, y))
    screen.blit(again.render('Try again?(press Space)', 1, (210, 120, 200)), (200, x))
    info.blit(lifes_f.render('Lifes: ' + str(lifes), 1, (210, 120, 200)), (600, 0))
    info.blit(score_f.render('Score: ' + str(score), 1, (210, 120, 200)), (5, 0))
    window.blit(info, (0, 0))
    window.blit(screen, (0, 30))
    pygame.display.flip()
    pygame.time.delay(5)