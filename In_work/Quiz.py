class Quiz:
    def __init__(self):
        self.quest = quest
        self.choices = choices
        self.question()
        self.choice()
        self.answer(self.ans)

    def question(self, que=1):
        self.que = que
        print(self.quest[self.que])

    def choice(self):
        for i in choices:
            print(i,':', choices[i])
        self.ans = input('Ваш ответ: ')

    def answer(self, ans):

        if ans == sel[1]:
            print("OK")
        else:
            print("NOK")




quest = {
    1: "Откуда на Беларусь готовилось нападение?"}

choices = {
    1: "Откуда мне знать?",
    2: "Со склада грязи.",
    3: "С планеты Нибиру.",
    4: "С загнивающег запада.",
    5: 'Там 4 позиции, я карту принёс, сейчас покажу.'}

sel = {
    1: '5'
}

q1 = Quiz()
