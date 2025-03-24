def avg(fn):
    def wrap(*args):
        st = ""
        for i in args:
            st += str(i) + ", "
        print("Среднее арифметическое:", st[:-2], "=", fn(*args) / len(args))

    return wrap


@avg
def summa(*args):
    print("Сумма:", *args, "=", sum(args))
    return sum(args)


summa(2, 3, 3, 4)