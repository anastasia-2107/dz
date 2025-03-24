# ПЕРВЫЙ ВАРИАНТ - КАК РЕШИЛА Я, вывела уникальные элементы
a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
b = []

for element in a:
    if element in a and element not in b:
        b.append(element)
print(a)
print(b)



# ВАРИАНТЫ, КОТОРЫЕ БЫЛИ РАЗОБРАНЫ НА УРОКЕ

# lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# new_lst = []
# i = 0
# for element in lst:
#     k = element
#     for element in lst:
#         if k == element:
#             i += 1
#     if i == 1:
#         print(k, end=" ")
#         new_lst.append(k)
#     i = 0



# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []
#
# for i in range(len(a)):
#     if a.count(a[i]) == 1:
#         b.append(a[i])
# print(b)


# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
#
# for i in range(len(a)):
#     if a.count(a[i]) == 1:
#         print(a[i], end=" ")




# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(a)
# for i in a:
#     if a.count(i) == 1:
#         print(i, end=" ")

