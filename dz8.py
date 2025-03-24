import math
from math import pi
print("Выберете фигуру, площадь которой хотите вычислить: \n1 - треугольник \n2 - прямоугольник \n3 - круг")
question = int(input("выбираю: "))
if question == 1:
    a = int(input("Введите сторону a = "))
    b = int(input("Введите сторону b = "))
    c = int(input("Введите сторону c = "))
    p = (a + b + c)/2
    square1 = round(math.sqrt(p * (p-a) * (p - b) * (p - c)), 2)
    print("Площадь треугольника равна: ", square1)
elif question == 2:
    a = int(input("Введите сторону a = "))
    b = int(input("Введите сторону b = "))
    print("Площадь прямоугольника равна: ", (a * b))
elif question == 3:
    r = int(input("Введите радиус r = "))
    print("Площадь круга равна: ", round((r * r * pi), 2))
else:
    print("Вы ввели неверное число")