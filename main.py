import pygame
import random

pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 36)


def acc (hits, total_clicks):
    accuracy = hits / total_clicks * 100  # Рассчитываем точность до 1 знака после запятой
    return accuracy


# Функция для проверки находится ли точка внутри круга
def is_point_in_circle(point_x, point_y, center_x, center_y, radius):
    # Расстояние от точки до центра круга
    distance = ((point_x - center_x) ** 2 + (point_y - center_y) ** 2) ** 0.5
    return distance <= radius



def points_calculation(mouse_x, mouse_y, circle_center_x, circle_center_y, points):
    distance = ((mouse_x - circle_center_x) ** 2 + (mouse_y - circle_center_y) ** 2) ** 0.5
    if distance <= radius / 7:
        points += 10
        message = random.choice(["В десяточку!!!", "Бинго!", "Есть пробитие!", "В яблочко!"])
    elif distance <= radius / 7 * 2:
        points += 9
        message = random.choice(["Девять! Отлично", "Почти в центр!"])
    elif distance <= radius / 7 * 3:
        points += 8
        message = random.choice(["Восьмёрка", "Восемь"])
    elif distance <= radius / 7 * 4:
        points += 7
        message = random.choice(["Семь!", "Семёрка"])
    elif distance <= radius / 7 * 5:
        points += 6
        message = random.choice(["Шесть баллов!", "Шесть тоже неплохо"])
    elif distance <= radius:
        points += 5
        message = random.choice(["Пятёрка!", "Попал!"])
    return points, message

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
radius = target_width / 2

target_x = random.randint(0, SCREEN_WIDTH-target_width)
target_y = random.randint(0, SCREEN_HEIGHT-target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# Координаты центра круга
target_center_x = target_x + radius
target_center_y = target_y + radius


total_clicks = 0  # Общее количество кликов
hits = 0  # Количество попаданий по мишени
accuracy = 0 # Точность в %
points = 0 # Очки за "качество" попадания: чем ближе к центру, тем лучше
message = ""
# =====================================================


TARGET_SPEED = 2  # Скорость, с которой мишень будет двигаться
x_direction = random.randint(-10, 10) / 5  # Начальное направление движения мишени по оси X (1 для право, -1 для лево)
y_direction = random.randint(-10, 10) / 5  # Начальное направление движения мишени по оси Y (1 для вниз, -1 для вверх)

# ... Предыдущая часть кода ...

running = True
while running:
    # заливаем экран случайным цветом из рандомной константы
    screen.fill(color)

    # Обновление позиции мишени
    target_x += TARGET_SPEED / 10 * x_direction
    target_y += TARGET_SPEED / 10 * y_direction

    # Проверка на выход мишени за пределы экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        x_direction *= -1  # Изменение направления движения по оси X
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        y_direction *= -1  # Изменение направления движения по оси Y

    # Отображение мишени
    screen.blit(target_image, (target_x, target_y))
    circle_center_x = target_x + radius
    circle_center_y = target_y + radius

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Выход из игры
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Обработка нажатия кнопки мыши
            total_clicks += 1 # Плюс один выстрел
            accuracy=acc(hits, total_clicks)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверка, попала ли пуля в мишень:
            if is_point_in_circle(mouse_x, mouse_y, circle_center_x, circle_center_y, radius):
                hits += 1 # Плюс одно попадание
                #points += 5 # Пока только 5, без яблочка =)
                accuracy = acc(hits, total_clicks)
                points, message = points_calculation(mouse_x, mouse_y, circle_center_x, circle_center_y, points)

                # Перемещение мишени в случайное место на экране после попадания
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                x_direction = random.randint(-2, 3)
                y_direction = random.randint(-2, 3)

    # Отображаем текст счета в верхней части экрана по центру
    score_text = f"Кликов: {total_clicks} Попаданий: {hits} Точность: {accuracy:.0f}%" # Округляем точность до 0 знаков после запятой
    score_surface = font.render(score_text, True, (255, 255, 255))  # Белый цвет текста
    message_surface = font.render(f'{message} + {points} очков', True, (255, 255, 255))  # Белый цвет текста
    # Вычисляем X позицию для центрирования текста
    score_x = (SCREEN_WIDTH - score_surface.get_width()) / 2
    screen.blit(score_surface, (score_x, 10))  # 10 пикселей от верхнего края экрана

    message_x = (SCREEN_WIDTH - message_surface.get_width()) / 2
    screen.blit(message_surface, (message_x, 50))  # 10 пикселей от верхнего края экрана


    # Обновление экрана
    pygame.display.update()

# Завершение работы с Pygame
pygame.quit()
