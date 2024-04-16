import pygame
import random

pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 36)


def acc (hits, total_clicks):
    accuracy = hits / total_clicks * 100  # Рассчитываем точность до 1 знака после запятой
    return accuracy


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

target_x = random.randint(0, SCREEN_WIDTH-target_width)
target_y = random.randint(0, SCREEN_HEIGHT-target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

total_clicks = 0  # Общее количество кликов
hits = 0  # Количество попаданий по мишени
accuracy=0
# =====================================================


# ... Предыдущая часть кода ...

TARGET_SPEED = 0.2  # Скорость, с которой мишень будет двигаться
x_direction = random.randint(-10, 10)  # Начальное направление движения мишени по оси X (1 для право, -1 для лево)
y_direction = random.randint(-10, 10)  # Начальное направление движения мишени по оси Y (1 для вниз, -1 для вверх)

# ... Предыдущая часть кода ...

running = True
while running:
    # заливаем экран случайным цветом из рандомной константы
    screen.fill(color)

    # Обновление позиции мишени
    target_x += TARGET_SPEED * x_direction/5
    target_y += TARGET_SPEED * y_direction/5

    # Проверка на выход мишени за пределы экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        x_direction *= -1  # Изменение направления движения по оси X
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        y_direction *= -1  # Изменение направления движения по оси Y

    # Отображение мишени
    screen.blit(target_image, (target_x, target_y))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Выход из игры
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Обработка нажатия кнопки мыши
            total_clicks += 1 # Плюс один выстрел
            accuracy=acc(hits, total_clicks)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверка, попала ли пуля в мишень
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1 # Плюс одно попадание
                accuracy=acc(hits, total_clicks)
                # Перемещение мишени в случайное место на экране после попадания
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                x_direction = random.randint(-10, 11)
                y_direction = random.randint(-10, 11)

    # Отображаем текст счета в верхней части экрана по центру
    score_text = f"Кликов: {total_clicks} Попаданий: {hits} Точность: {accuracy:.0f}%" # Округляем точность до 0 знаков после запятой
    score_surface = font.render(score_text, True, (255, 255, 255))  # Белый цвет текста
    # Вычисляем X позицию для центрирования текста
    score_x = (SCREEN_WIDTH - score_surface.get_width()) / 2
    screen.blit(score_surface, (score_x, 10))  # 10 пикселей от верхнего края экрана


    # Обновление экрана
    pygame.display.update()

# Завершение работы с Pygame
pygame.quit()
