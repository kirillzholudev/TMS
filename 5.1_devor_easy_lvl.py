# easy lvl: декоратор разворачивающий аргументы Пример:a(1,2,3) # > a(3,2,1)
def f(arg):
    def wrapper(*b):
        print(b[::-1])

    return wrapper


@f
def num(*a):
    print(a)


num(5, 5, 8, 9, 1, 0, 0)
