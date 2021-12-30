import pygame


pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("menu")
menuAtivo = True

font = pygame.font.SysFont('Arial', 35)
# создание кнопок меню
start_button = pygame.draw.rect(screen, (57, 255, 20), (20, 40, 150, 50))
screen.blit(font.render('START', True, (0, 0, 0)), (50, 50))

continue_button = pygame.draw.rect(screen, (57, 255, 20), (20, 130, 150, 50))
screen.blit(font.render('RULES', True, (0, 0, 0)), (50, 140))

quit_button = pygame.draw.rect(screen, (57, 255, 20), (20, 220, 150, 50))
screen.blit(font.render('EXIT', True, (0, 0, 0)), (50, 230))

pygame.display.update()
pygame.display.flip()


def startGame():
    screen.fill('white')
    pygame.display.flip()



def rules():
    screen = pygame.display.set_mode((500, 400))
    screen.fill('black')
    pygame.display.set_caption("Rules")
    pygame.display.update()
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.update()
    pygame.quit()



while menuAtivo:
    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if 170 >= pygame.mouse.get_pos()[0] >= 20 and 90 >= pygame.mouse.get_pos()[1] >= 40:
                pass
            if 170 >= pygame.mouse.get_pos()[0] >= 20 and 180 >= pygame.mouse.get_pos()[1] >= 130:
                rules()
            if 170 >= pygame.mouse.get_pos()[0] >= 20 and 270 >= pygame.mouse.get_pos()[1] >= 220:
                pygame.quit()
