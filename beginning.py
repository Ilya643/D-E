import pygame

pygame.init()


class Menu:
    def __init__(self):
        screen = pygame.display.set_mode((500, 400))
        self.screen = screen
        pygame.display.set_caption("menu")
        self.font = pygame.font.SysFont('Arial', 35)
        # создание кнопок меню
        # кнопка старт
        start_button = pygame.draw.rect(self.screen, (57, 255, 20), (20, 40, 150, 50))
        self.start_button = start_button
        self.screen.blit(self.font.render('START', True, (0, 0, 0)), (50, 50))
        # кнопка правила
        continue_button = pygame.draw.rect(self.screen, (57, 255, 20), (20, 130, 150, 50))
        self.continue_button = continue_button
        self.screen.blit(self.font.render('RULES', True, (0, 0, 0)), (50, 140))
        # кнопка выход
        quit_button = pygame.draw.rect(self.screen, (57, 255, 20), (20, 220, 150, 50))
        self.quit_button = quit_button
        self.screen.blit(self.font.render('EXIT', True, (0, 0, 0)), (50, 230))
        pygame.display.update()
        pygame.display.flip()
        self.moving()

    # функция создания меню
    def moving(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 90 >= pygame.mouse.get_pos()[1] >= 40:
                        pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 90 >= pygame.mouse.get_pos()[1] >= 40:
                        # запускаем функцию старт
                        self.start()
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 180 >= pygame.mouse.get_pos()[1] >= 130:
                        # запускаем функцию правила
                        self.rules()
                    if 170 >= pygame.mouse.get_pos()[0] >= 20 and 270 >= pygame.mouse.get_pos()[1] >= 220:
                        # выход из игры
                        exit()

    def rules(self):
        # в это функии мы выводим правила по запросу из бд
        self.screen = pygame.display.set_mode((750, 550))
        self.screen.fill('black')
        pygame.display.set_caption("Rules")
        # создаем кнопку возвращения, чтобы после прочтения правил можно было вернуться в главное меню
        return_button = pygame.draw.rect(self.screen, (57, 255, 20), (580, 480, 150, 50))
        self.return_button = return_button
        self.screen.blit(self.font.render('RETURN', True, (0, 0, 0)), (600, 490))
        pygame.display.update()
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 730 >= pygame.mouse.get_pos()[0] >= 580 and 530 >= pygame.mouse.get_pos()[1] >= 480:
                        # запускаем функцию старт
                        self.moving()

    def start(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill('black')
        pygame.display.set_caption("menu_continue")
        pygame.display.update()
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.update()
        exit()


a = Menu()

