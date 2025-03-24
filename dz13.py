student = {}

n = int(input("Количество студентов: "))
sum = 0
# for i in range(1, n + 1):
#     name = input(str(i) + "-й студент: ")
#     mark = int(input("Балл: "))
#     student[name] = mark
#     sum += mark


for i, j in enumerate(range(n), 1):
    name = input(str(i) + "-й студент: ")
    mark = int(input("Балл: "))
    student[name] = mark
    sum += mark


average = sum / n
# print(student)
print("Средний балл:", round(average))
print("Студенты с баллом выше среднего:")

# for i in student:
#     if student[i] > average:
#         print(i)


for i, j in student.items():
    if j > average:
        print(i)