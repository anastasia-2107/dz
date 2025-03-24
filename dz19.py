def f_num(items):
    if not items: # if len(items) == 0
        return 0
    count = 0
    if items[0] < 0:
        count += 1
    return count + f_num(items[1:])


num = [-2, 3, 8, -11, -4, 6, -8]
print((f_num(num)))
