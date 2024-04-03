import pygame, draw, random, math, sound, os

import main


def init_2DArray(width, height):
    return [[random.randrange(1, 6) for x in range(width)] for y in range(height)]

# проверка на бабах
def match_exists(board):
    # Проверяет строки
    for y in range(len(board)):
        streak = 1
        for x in range(1, len(board[y])):
            if board[y][x] == board[y][x - 1] and board[y][x] != 0:
                streak += 1
            else:
                streak = 1
            if streak >= 3:  # Полоса из 3 одинаковых сердечек
                return True
    # Проверяет столбцы
    for x in range(len(board[0])):
        streak = 1
        for y in range(1, len(board)):
            if board[y][x] == board[y - 1][x] and board[y][x] != 0:
                streak += 1
            else:
                streak = 1
            if streak >= 3:
                return True
    return False


# Настраивает поле так, чтобы на ней не было совпадений
def format_board(board):
    while match_exists(board):
        for y in range(len(board)):
            for x in range(len(board[y])):
                board[y][x] = random.randrange(1, 7)
    return board


# Displays the text-based array representation of the board
def show_board(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end=" ")
        print()


# Обновляет и приостанавливает работу экрана
def display_pause(clock, x):
    pygame.display.flip()  # экран обновлений
    clock.tick(x)  # останавливает выполнение на 1/x секунд с момента последнего тика


# Проверяет, находится ли второе выбранное сердечко рядом с первом сердечком
def isAdjacent(selected_x, selected_y, x, y):
    if selected_x + 1 == x and selected_y == y:
        return True
    elif selected_x - 1 == x and selected_y == y:
        return True
    elif selected_y + 1 == y and selected_x == x:
        return True
    elif selected_y - 1 == y and selected_x == x:
        return True
    return False

# меняет местами
def swap(array, x1, y1, x2, y2):
    temp = array[y1][x1]
    array[y1][x1] = array[y2][x2]
    array[y2][x2] = temp


def elim_matches(board):
    elim_list = []
    # Проверяет строки на наличие совпадений
    for y in range(len(board)):
        streak = 1
        for x in range(1, len(board[y])):
            if board[y][x] == board[y][x - 1] and board[y][x] != 0:
                streak += 1
            else:
                streak = 1
            if streak == 3:
                elim_list += [[y, x - 2]]
                elim_list += [[y, x - 1]]
                elim_list += [[y, x]]
            elif streak > 3:
                elim_list += [[y, x]]
    # Проверяет столбики на наличие совпадений
    for x in range(len(board[0])):
        streak = 1
        for y in range(1, len(board)):
            if board[y][x] == board[y - 1][x] and board[y][x] != 0:
                streak += 1
            else:
                streak = 1
            if streak == 3:
                elim_list += [[y - 2, x]]
                elim_list += [[y - 1, x]]
                elim_list += [[y, x]]
            elif streak > 3:
                elim_list += [[y, x]]

    # Превращает все найденные совпадения в пустоты
    for i in range(len(elim_list)):
        y = elim_list[i][0]
        x = elim_list[i][1]
        board[y][x] = 0

    return len(elim_list)


# Возвращает, если на доске есть какие-либо пустые плитки
def board_filled(board):
    for y in range(len(board)):
        if 0 in board[y]:  # 0 is an empty tile
            return False
    return True


# Отбрасывает все плитки с пустым пространством под ними на одну
# Обходит массив от нижнего левого угла вверх по каждому столбцу
def drop_tiles(board):
    for x in range(len(board[0])):
        for y in range(len(board) - 2, -1, -1):  # проходит снизу вверх по каждому столбцу
            if board[y + 1][x] == 0 and board[y][x] != 0:
                swap(board, x, y + 1, x, y) #cдвиг


# Заполняет все пустые плитки в верхней части доски
def fill_top(board):
    for x in range(len(board[0])):
        if board[0][x] == 0:
            board[0][x] = random.randrange(1, 7)


def gameMain(turns_left, GOAL_SCORE):
    # Начальные игровые переменные
    WIDTH = 7
    HEIGHT = 9
    BOX_LENGTH = 70
    selected = False
    selected_x = None
    selected_y = None
    score = 0
    exit_game = False
    gameover_displayed = False
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # Центрирует окно, которое будет сгенерировано

    board = init_2DArray(WIDTH, HEIGHT)
    format_board(board)

    pygame.init()  # загружает все модули pygame
    sound.load()
    screen = draw.create_screen(WIDTH, HEIGHT, BOX_LENGTH)
    clock = pygame.time.Clock()
    draw.window(board, turns_left, score, GOAL_SCORE)
    pygame.display.flip()  # обновление экрана

    # Цикл игры
    while not exit_game:
        while turns_left > 0 and not exit_game and score < GOAL_SCORE:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # кнопка выхода из окна
                    exit_game = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        main.main()
                        gameover_displayed = True
                        exit_game = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    coord_pair = pygame.mouse.get_pos()  # выделение щелчком левой кнопки мыши
                    x = math.floor(coord_pair[0] / BOX_LENGTH)
                    y = math.floor(coord_pair[1] / BOX_LENGTH)



                    if x < WIDTH and y < HEIGHT:
                        if selected == False:  # Ранее ни одно сердечко не было выбрано
                            selected = True
                            selected_x = x
                            selected_y = y
                            draw.selected(x, y)
                        elif selected == True:
                            if isAdjacent(selected_x, selected_y, x, y): #если выбранные сердечки рядом
                                swap(board, selected_x, selected_y, x, y) # меняет местами
                                draw.window(board, turns_left, score, GOAL_SCORE)
                                display_pause(clock, 2.5)

                                if match_exists(board):
                                    turns_left -= 1
                                    turn_score = 0
                                    combo_count = 1

                                    # Повторяет до тех пор, пока совпадений больше не останется
                                    while match_exists(board):
                                        turn_score += elim_matches(board)
                                        draw.window(board, turns_left, score,
                                                    GOAL_SCORE)
                                        sound.play_effect("pop")
                                        display_pause(clock, 2.5)

                                        while not board_filled(board): # проверка на пустоты
                                            # Отбрасывает плитки и заполняет доску до отказа
                                            drop_tiles(board)
                                            fill_top(board)
                                            draw.window(board, turns_left, score,
                                                        GOAL_SCORE)
                                            display_pause(clock, 2.5)

                                        combo_count += 1

                                    combo_count -= 1
                                    score += turn_score * combo_count
                                    draw.window(board, turns_left, score,
                                                GOAL_SCORE)
                                    pygame.display.flip() #обновление

                                    if combo_count > 1: #добавление звука и вставок при в зрывах больше 1
                                        sound.play_combo(combo_count)
                                        draw.combo_msg(combo_count)
                                        pygame.display.flip()
                                        pygame.time.delay(2000)
                                        draw.window(board, turns_left, score,
                                                    GOAL_SCORE)
                                        pygame.display.flip()


                                elif not match_exists(board):
                                    # откидывает сердечко назад
                                    swap(board, selected_x, selected_y, x, y)
                                    draw.window(board, turns_left, score,
                                                GOAL_SCORE)
                                    pygame.display.flip()

                            elif not isAdjacent(selected_x, selected_y, x, y):
                                # если сердечки не рядом
                                draw.window(board, turns_left, score, GOAL_SCORE)
                                pygame.display.flip()

                            selected = False
                            selected_x = None
                            selected_y = None

            display_pause(clock, 60)




        if not gameover_displayed:
            if score >= GOAL_SCORE:
                draw.win()
                sound.play_effect("win")

            else:
                draw.lose()
                sound.play_effect("lose")
            gameover_displayed = True
            pygame.display.flip()


        # выход из игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # кнопка выхода
                exit_game = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main.main()
                    gameover_displayed = True
                    exit_game = True



