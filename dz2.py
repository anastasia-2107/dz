num = int(input("Введите пятизначное число: ")) # 12345
a = num % 10 # 5
# print(a)
num //= 10 # 1234
b = num % 10 # 4
# print(b)
num //= 10 # 123
c = num % 10 # 3
# print(c)
num //= 10 # 12
d = num % 10 # 2
# print(d)
num //= 10 # 1
e = num  # 1
# print(e)
num = str(e) + str(d) + str(c) + str(b) + str(a)
# print(num)
mult = a * b * c * d * e
print("Произведение цифр числа", num, ":", mult)
sred = (a + b + c + d + e) / 5
print("Среднее арифметическое: ", sred)
