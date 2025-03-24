from random import randint


def func(a, b):
    return tuple(randint(a, b) for i in range(10))


tpl1 = func(0, 5)
# print(tpl1)
tpl2 = func(-5, 0)
# print(tpl2)
tpl3 = tpl1 + tpl2
print(tpl3)
# amount = 0
# for i in range(len(tpl3)):
#     if tpl3[i] == 0:
#         amount = tpl3.count(tpl3[i])
# print('Количество нулей =', amount)




# ВТОРАЯ ЧАСТЬ ЗАДАЧИ НА УРОКЕ

print('Количество нулей =', tpl3.count(0))




