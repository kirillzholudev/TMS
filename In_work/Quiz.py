

from random import shuffle


class Mystery:
    points = 0

    def __init__(self, question: str, answer: str, choices: list):
        self.question = question
        self.__answer = answer
        self.choices = choices
        shuffle(self.choices)

    def choices_set(self):
        for i in range(len(self.choices)):
            self.choices.insert(i, f"{i + 1}. {self.choices[i]}")
            self.choices.pop(i + 1)
        return self.choices

    def check(self):
        if self.choices[int(input("Enter the answer number - ")) - 1][3:] == self.__answer:
            Mystery.points += 1
            return True
        else:
            return False

    def __repr__(self):
        return "\n" + self.question + "\n" + "\n".join(self.choices_set()) + "\n" + f"Your points --> {Mystery.points}"


quiz_1 = Mystery(question="What animal can be seen on the Porsche logo?", answer="Horse",
              choices=["Pony", "Horse", "Monkey", "Rat", "Eagle"])

quiz_2 = Mystery("Which language has the most words?", "English",
              ["English", "Italian", "Spanish", "Russian", "Polish"])

quiz_3 = Mystery("When was Netflix founded?", "1997",
              ["1999", "2005", "2001", "2009", "1997"])

print(quiz_1)
print(quiz_1.check())
print(quiz_2)
print(quiz_2.check())
print(quiz_3)
print(quiz_3.check())
print(f"Youre score --> {Mystery.points} ")