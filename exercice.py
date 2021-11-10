class Exercice:

    def __init__(self, statement, answer, ints):
        self.statement = statement
        self.answer = str(answer)
        self.ints = ints
        self.point = 1
        self.correctAnswer = False

    def getStatement(self):
        return self.statement

    def hasPutCorrectAnswer(self):
        return self.correctAnswer

    def testAnswer(self, triedAnswer):
        if triedAnswer == "skip":
            self.point = 0
            self.correctAnswer = True
            print("Question passée")
        elif self.answer == triedAnswer:
            self.correctAnswer = True
            print("Félicitation, la réponse est correcte !")
        else:
            self.point /= 2
            print("Mauvaise réponse...")
            if self.point < 0.1:
                print(f"Trop d'erreurs, la réponse était: {self.answer}")
                self.testAnswer("skip")
