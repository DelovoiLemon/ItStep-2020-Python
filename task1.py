# С помощью модуля turtle реализуйте функцию,
# которая в зависимости от переданного параметра N
# (принимает значения от 3 до 8) способна нарисовать
# 3-,4-, 5-,6-,7-,8-угольник. Контур фигур должен быть замкнут.
# В качестве ответа приложите ссылку на файл программы.
# Обратите внимание на критерии оценки, описанные в начале опроса.

from turtle import*;

l = 60      # Длина стороны
n = 0

while(n < 3 or n > 8):
    n = int(input("Введите кол-во углов от 3 до 8: "))

down()

for i in range(n):
    forward(l)
    right(360/n)


up()
home()
