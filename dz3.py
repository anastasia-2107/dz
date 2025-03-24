# n = int(input("Введите число от 1 до 99: "))
# if 1 <= n <= 99:
#     print("Результат: ", end="")
#     if n != 11 and n % 10 == 1:
#         print(n, " копейка")
#     elif 2 <= n % 10 <= 4 and n != 12 and n !=13 and n != 14:
#         print(n, " копейки")
#     else:
#         print(n, "копеек")
# else:
#     print("Не верное число")




# ВАРИАНТ НА УРОКЕ
a = int(input("Введите число от 1 до 99: "))
kop = a
if 11 <= kop <= 14:
    print(a, "копеек")
elif 1 <= a <= 99:
    kop = kop % 10
    if kop == 1:
        print(a, "копейка")
    elif 2 <= kop <= 4:
        print(a, "копейки")
    else:
        print(a, "копеек")
else: print("Значения должны быть от 1 до 99")