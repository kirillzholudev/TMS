#medium lvl: декоратор фильтрующий указаный элемент

# Нужно доделать
def my_filtr(filt):

    def name(*l):

        a = list(filter(lambda l: not filt, l))

        return a
    return name






@my_filtr(filt="Oleg")
def a(g,h,j):
    pass

a(1,2,"Oleg") # > Exception