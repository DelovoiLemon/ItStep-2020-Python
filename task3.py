# С помощью модуля turtle реализуйте программу,
# которая передвигая по холсту перо,
# закрашивает прямоугольную область указанным
# с клавиатуры цветом. Использовать функции
# begin_fill() и end_fill() запрещено!
# В качестве ответа приложите ссылку на файл программы.
# Обратите внимание на критерии оценки, описанные в начале опроса **

from turtle import*

def fill(width, height):
    for i in range(height):
        forward(width)
        if (i%2 == 0):
            right(90)
        else:
            left(90)
        forward(1)
        if (i%2 == 0):
            right(90)
        else:
            left(90)

def fill2(width, height):
    for i in range(height):
        forward(width)
        right(90)
        forward(height - i - 1)
        right(90)

width  = 100
height = 20
speed(10)

while True:
    try:
        color = textinput("Color", "Введите цвет: ")
        pencolor(color)
        break
    except:
        pass


fill(width, height)
up()
goto(0, height + 10)
down()
fill2(width, height)

up()
home()
