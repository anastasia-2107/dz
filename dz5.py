
# a = [input("-> ") for i in range(int(input("n = ")))]

a = [0] * int(input("Введите количество элементов списка: "))
for i in range(len(a)):
    a[i] = int(input("-> "))
    sum = 0
    for num in a:
        if num < 0:
            sum += num
    # while a[i] < len(a):
    #     sum += a[i]
print("Сумма отрицательных элементов:", sum)






