

class Quiz:
    def __init__(self, name='User', vopr=[], otv=[], var=[]):
        self.name = name
        self.vopr = vopr
        self.otv = otv
        self.var = var
        print(f'Привет, {name}\n')
        self.vopros()
        self.otvet()

    def vopros(self):
        print(f'Твой вопрос звучит так: {self.vopr}\n')
        print(f'Варианты ответов: \n {self.var}\n')

    def otvet(self):
        ch = input('-->')
        if ch in self.otv:
            print('Ты лучший!')
        else:
            print('Попробуй еще раз')
            return self.otvet()



a1 = Quiz(vopr="Откуда на Беларусь готовилось нападение?",
otv="там 4 позиции, я карту принёс, сейчас покажу",
var=[
"Откуда мне знать?",
"Со склада грязи.",
"С планеты Нибиру.",
"С загнивающег запада.",
"Там 4 позиции, я карту принёс, сейчас покажу"
])