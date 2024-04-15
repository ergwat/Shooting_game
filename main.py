import pygame
import random

pygame.init()

# задаём константы и параметры рабочего окна
# =====================================================
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Игра "Тир"')
icon = pygame.image.load("img/tir.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0,SCREEN_WIDTH-target_width)
target_y = random.randint(0, SCREEN_HEIGHT-target_height)
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# =====================================================


running=True
while running:
    # заливаем экран случайным цветом из рандомной константы
    screen.fill(color)
    # размещаем мишень в случайные координаты
    screen.blit(target_image, (target_x, target_y))

    # основной цикл, отслеживающий любые события
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT: running = False
            case pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if target_x < mouse_x < target_x + target_width and target_y <mouse_y < target_y + target_height:
                    target_x = random.randint(0, SCREEN_WIDTH - target_width)
                    target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # смена кадра
    pygame.display.update()


pygame.quit()