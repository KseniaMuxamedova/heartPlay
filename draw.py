import random

import pygame, os

image_dict = {}


def load_images():
    image_names = ["love (1)", "love (2)", "love (3)", "love (4)", "love (5)", "love (6)", "love (7)"]
    for i in range(len(image_names)):
        file_path = "images/" + image_names[i] + ".png"
        image_dict[image_names[i]] = pygame.image.load(file_path)


# Возвращает объект экрана pygame
def create_screen(grid_width, grid_height, box_length):
    global BOX_LENGTH, screen
    BOX_LENGTH = box_length

    load_images()
    window_icon = image_dict["love (4)"]
    pygame.display.set_icon(window_icon)
    pygame.display.set_caption("Поменяй сердечки")

    screen = pygame.display.set_mode((BOX_LENGTH * (grid_width + 2),
                                      BOX_LENGTH * grid_height))
    return screen


# Масштабирует значения меньшей длины массива до пикселей
def to_pixels(x):
    return x * BOX_LENGTH

# рисовка окна
def window(board, turns_left, score, goal_score):
    bg = pygame.image.load("images/bg.jpg")
    screen.blit(bg, (0, 0))  # Фон
    draw_sidebar(turns_left, score, goal_score)
    draw_board(board)


def startwindow():
    bg = pygame.image.load("images/startBG.jpg")
    title = pygame.image.load("images/title.png")
    screen.blit(bg, (0, 0))  # Фон
    screen.blit(title, (10, 10))
    b1 = pygame.image.load("images/play.png")
    screen.blit(b1, (20, 250))
    b1 = pygame.image.load("images/about.png")
    screen.blit(b1, (20, 370))

def aboutwindow():
    bg = pygame.image.load("images/startBG.jpg")
    title = pygame.image.load("images/title.png")
    screen.blit(bg, (0, 0))  # Фон
    screen.blit(title, (10, 10))
    font = pygame.font.SysFont("comic sans ms", 30)
    text = font.render("Цель: очистить поле от сердец,", True, (233, 159, 188))
    screen.blit(text, (to_pixels(0.3), to_pixels(2)))
    text = font.render("соединяя по 3 или больше одинаковых;", True, (233, 159, 188))
    screen.blit(text, (to_pixels(0.3), to_pixels(2.5)))
    text = font.render("Как играть в Поменяй сердечки: мышью;", True, (233, 159, 188))
    screen.blit(text, (to_pixels(0.3), to_pixels(3)))
    text = font.render("Об авторе: Дунаева Ксения", True, (233, 159, 188))
    screen.blit(text, (to_pixels(0.3), to_pixels(4)))
    text = font.render("Студент Факультета Компьютерных наук", True, (233, 159, 188))
    screen.blit(text, (to_pixels(0.3), to_pixels(4.5)))
    text = font.render("Контакты: https://vk.com/best_fizmat11", True, (233, 159, 188))
    screen.blit(text, (to_pixels(0.3), to_pixels(5)))
    text = font.render("Игра посвящена любимой пиавке!", True, (233, 159, 188))
    screen.blit(text, (to_pixels(0.3), to_pixels(6)))
    b1 = pygame.image.load("images/back.png")
    screen.blit(b1, (0, 540))

def levelwindow():
    bg = pygame.image.load("images/startBG.jpg")
    title = pygame.image.load("images/title.png")
    screen.blit(bg, (0, 0))  # Фон
    screen.blit(title, (10, 10))
    b1 = pygame.image.load("images/1.png")
    screen.blit(b1, (20, 200))
    b1 = pygame.image.load("images/2.png")
    screen.blit(b1, (20, 320))
    b1 = pygame.image.load("images/3.png")
    screen.blit(b1, (20, 440))
    b1 = pygame.image.load("images/back.png")
    screen.blit(b1, (0, 540))


# подписи сбоку
def draw_sidebar(turns_left, score, goal_score):
    font = pygame.font.SysFont("comic sans ms", 30) #шрифт текста сбоку

    text = font.render("Цель:", True, (245, 203, 77))
    screen.blit(text, (to_pixels(7.2), to_pixels(0)))
    #pygame.draw.line(screen, (245, 203, 77), (to_pixels(7), to_pixels(0.6)),  # начальная точка
                     #(to_pixels(8.75), to_pixels(0.6)), 1)  # конечная точка, ширина
    text = font.render(str(goal_score), True, (245, 159, 106))
    screen.blit(text, (to_pixels(7.4), to_pixels(0.6)))

    text = font.render("Осталось", True, (125, 221, 198))
    screen.blit(text, (to_pixels(7.1), to_pixels(1.8)))
    text = font.render("Ходов:", True, (125, 221, 198))
    screen.blit(text, (to_pixels(7.3), to_pixels(2.3)))
    #pygame.draw.line(screen, (0, 0, 0), (to_pixels(7), to_pixels(2.6)),
                     #(to_pixels(8.75), to_pixels(2.6)), 1)
    text = font.render(str(turns_left), True, (38, 172, 202))
    screen.blit(text, (to_pixels(7.5), to_pixels(2.8)))

    text = font.render("Счёт:", True, (233, 159, 188))
    screen.blit(text, (to_pixels(7.4), to_pixels(3.5)))
    offset = 0
    if score >= 100:
        offset = -0.3
    elif score >= 10:
        offset = -0.15
    text = font.render(str(score), True, (169, 140, 188))
    screen.blit(text, (to_pixels(7.75 + offset), to_pixels(4.1)))


def draw_board(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            draw_icon(board[y][x], x, y)


# для загрузки и рисования каждого сердечка
def draw_icon(num, x, y):
    icon = None
    x = to_pixels(x) + 3  # ячейка = 70x70,картика 64x64, смещение пикселя к центру
    y = to_pixels(y) + 3

    if num == 1:
        icon = image_dict["love (1)"]
    elif num == 2:
        icon = image_dict["love (2)"]
    elif num == 3:
        icon = image_dict["love (3)"]
    elif num == 4:
        icon = image_dict["love (4)"]
    elif num == 5:
        icon = image_dict["love (5)"]
    elif num == 6:
        icon = image_dict["love (6)"]
    if num != 0:
        screen.blit(icon, (x, y))

#выделение сердечка
def selected(x, y):
    x = to_pixels(x)
    y = to_pixels(y)
    rect = pygame.Rect(x, y, BOX_LENGTH, BOX_LENGTH)
    r = random.randrange(1, 255)
    g = random.randrange(1, 255)
    b = random.randrange(1, 255)
    pygame.draw.rect(screen, (r, g, b), rect, 3)


def win():
    center_msg("WIN!")


def lose():
    center_msg("LOSE")


# появление надписи победа/поражение
def center_msg(msg):
    color = (0, 0, 0)
    if msg == "WIN!":
        color = (38, 172, 202)
    elif msg == "LOSE":
        color = (245, 159, 106)

    rect = pygame.Rect(to_pixels(2), to_pixels(3),
                       to_pixels(3), to_pixels(2))
    pygame.draw.rect(screen, (255, 255, 255), rect, 0)
    pygame.draw.rect(screen, color, rect, 4)
    font = pygame.font.SysFont("Times New Roman", 70)
    text = font.render("YOU", True, color)
    screen.blit(text, (to_pixels(2.4), to_pixels(3)))
    text = font.render(msg, True, color)
    screen.blit(text, (to_pixels(2.4), to_pixels(4)))

# надписи при нескоьких бахах
def combo_msg(combo_count):
    msg = ""
    color = (0, 0, 0)
    x = 0.1

    if combo_count >= 5:
        color = (245, 203, 77)
        msg = "LEGENDARY"
    elif combo_count == 4:
        color = (233, 159, 188)
        msg = "EPIC"
        x = 2.25
    elif combo_count == 3:
        color = (125, 221, 198)
        msg = "TRIPLE"
        x = 1.65
    elif combo_count == 2:
        color = (169, 140, 188)
        msg = "DOUBLE"
        x = 1.2

    rect = pygame.Rect(0, to_pixels(4), to_pixels(7), to_pixels(1))
    pygame.draw.rect(screen, (255, 255, 255), rect, 0)
    pygame.draw.rect(screen, color, rect, 4)

    font = pygame.font.SysFont("Times New Roman", 79)
    text = font.render(msg, True, color)
    screen.blit(text, (to_pixels(x), to_pixels(3.9)))
