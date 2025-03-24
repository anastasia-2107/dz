# import random
#
# mas = [random.randint(0, 100) for i in range(10)]
# print("Основной рандомный список:", mas)
# a = mas.copy()
# # print(a)
#
# # print(mas, id(mas))
# # print(a, id(a))
#
# a.sort(reverse=False)
# # print(a)
# min_ = a[0]
# print("Min: ", min_)
#
# if min_ in mas:
#     ind = mas.index(min_, 0)
#     print("Index min: ", ind)
#
# mas[0:ind] = []
# print(mas)



# РАЗБОР НА УРОКЕ
# import random
# mas1 = [random.randint(0, 100) for i in range(10)]
# print("Основной рандомный список:", mas1)
# mas = mas1.copy()
# mas.sort()
# print(mas)
# min_ = mas[0] # нельзя называть переменную min - зарезервированное слово
# print("Min: ", min_)
# ind = mas1.index(min_)
# print("Index min: ", ind)
# del mas1[:ind]
# print(mas1)


# ВТОРОЙ ВАРИАНТ
# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print("Основной рандомный список:", mas)
# print(len(mas))
# print(min(mas))
# print(max(mas))
