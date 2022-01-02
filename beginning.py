import pygame
from typing import Any

pygame.init()


class Menu():
    def __init__(self):
        screen = pygame.display.set_mode((500, 400))
        self.screen = screen
        pygame.display.set_caption("menu")
        font = pygame.font.SysFont('Arial', 35)
        # создание кнопок меню
        start_button = pygame.draw.rect(self.screen, (57, 255, 20), (20, 40, 150, 50))
        self.start_button = start_button
        self.screen.blit(font.render('START', True, (0, 0, 0)), (50, 50))

        continue_button = pygame.draw.rect(self.screen, (57, 255, 20), (20, 130, 150, 50))
        self.continue_button = continue_button
        self.screen.blit(font.render('RULES', True, (0, 0, 0)), (50, 140))

        quit_button = pygame.draw.rect(self.screen, (57, 255, 20), (20, 220, 150, 50))
        self.quit_button = quit_button
        self.screen.blit(font.render('EXIT', True, (0, 0, 0)), (50, 230))

        pygame.display.update()
        pygame.display.flip()
        self.moving()

    def moving(self):
        menuativo = True
        while menuativo:
            for event in pygame.event.get():
                # nt(event)
                if event.type == pygame.MOUSEMOTION:
                    print(event)
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 90 >= pygame.mouse.get_pos()[1] >= 40:
                        pass


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 90 >= pygame.mouse.get_pos()[1] >= 40:
                        self.start()
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 180 >= pygame.mouse.get_pos()[1] >= 130:
                        self.rules()
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 270 >= pygame.mouse.get_pos()[1] >= 220:
                        pygame.quit()

    def rules(self):
        self.screen = pygame.display.set_mode((500, 400))
        self.screen.fill('black')
        pygame.display.set_caption("Rules")
        pygame.display.update()
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.update()
        pygame.quit()

    def start(self):
        pass

a = Menu()
