# С помощью модуля turtle реализуйте программу,
# которая рисует дом, состоящий из квадрата (основание дома),
# равностороннего треугольника (крыша), квадрата
# меньшего размера (окно в основании), 36-угольника (окно в крыше).
# В качестве ответа приложите ссылку на файл программы.
# Обратите внимание на критерии оценки, описанные в начале опроса.

from turtle import*

# Функция рисования многоугольника
# от текущей позиции пера
#
# @len - длина стороны
# @n - количество углов
def polygon (len, n):
    for i in range(n):
        down()
        forward(len)
        right(360/n)
        up()


k = 1                       # Коэффициент масштабирования

length_big   = 100 * k      # Длина стороны большого квадрата
length_small = 100 / 3 * k  # Длина стороны большого квадрата
length_circle = 3 * k       # Длина стороны 36-угольника


# Рисуем большой квадрат
polygon(length_big, 4)

# Рисуем маленький квадрат
forward(length_small)
right(90)
forward(length_small)
left(90)
polygon(length_small, 4)

# Рисуем треугольник
home()
forward(length_big)
right(180)
polygon(length_big, 3)

# Рисуем круг (36-угольник)
home()
left(90)
forward(length_big / 2 - k)
right(90)
forward(length_big / 2 - k)
polygon(length_circle, 36)

up()
home()
