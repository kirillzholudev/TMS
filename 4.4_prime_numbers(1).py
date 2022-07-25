simple_num = 0
list_ = []
for i in range(2, 100_000):
    for m in list_:
        if i % m == 0:
            break
    else:
        list_.append(i)
        simple_num += i
print(simple_num)