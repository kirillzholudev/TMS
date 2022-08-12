# Занятие (проверка пароля в банк аккаунте)
class Bank_acc:

    def __init__(self, pin):
        self.__pin = pin
        self.__bank_acc = 0

    @property
    def acc(self):
        if self.__pin == int(input("Pin: ")):
            return self.__bank_acc

    @acc.setter
    def acc(self, val):
        self.__bank_acc = val

my_acc = Bank_acc(1234)
my_acc.acc += 100
print(my_acc.acc)2
