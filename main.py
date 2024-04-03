import pygame,game, draw, random, math, sound, os

def level(exit_game):
    draw.levelwindow()
    pygame.display.flip()
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # кнопка выхода из окна
                exit_game = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                coord_pair = pygame.mouse.get_pos()
                x = coord_pair[0]
                y = coord_pair[1]

                if x >= 195 and x <= 445:
                    if y >= 260 and y <= 330:
                        game.gameMain(50, 100)
                    elif y >= 380 and y <= 430:
                        game.gameMain(40, 200)
                    elif y >= 489 and y <= 555:
                        game.gameMain(30, 300)
                if (x >= 0 and x <= 470) and (y >= 520 and y <= 590):
                    main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # кнопка выхода
                exit_game = True

def about(exit_game):
    draw.aboutwindow()
    pygame.display.flip()
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # кнопка выхода из окна
                exit_game = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                coord_pair = pygame.mouse.get_pos()
                x = coord_pair[0]
                y = coord_pair[1]
                print(x, y)
                if (x >= 0 and x <= 470) and (y >= 520 and y <= 590):
                    main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # кнопка выхода
                exit_game = True

def main():
    WIDTH = 7
    HEIGHT = 9
    BOX_LENGTH = 70
    exit_game = False
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # Центрирует окно, которое будет сгенерировано

    pygame.init()  # загружает все модули pygame
    screen = draw.create_screen(WIDTH, HEIGHT, BOX_LENGTH)
    draw.startwindow()
    pygame.display.flip()

    while not exit_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # кнопка выхода из окна
                    exit_game = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    coord_pair = pygame.mouse.get_pos()
                    x = coord_pair[0]
                    y = coord_pair[1]
                    print(x, y)
                    if x >=215 and x <=430:
                        if y >=295 and y <=365:
                            level(exit_game)
                        elif y >=428 and y <=490:
                            about(exit_game)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # кнопка выхода
                    exit_game = True


if __name__ == "__main__": main()