import exerciceList

class Exam:

    def __init__(self, exoAmount):
        self.questionCount = 0
        self.exo = []

        #for i in range(exoAmount):
        #    self.exo.append(exerciceList.new())
        for i in range(30):
            self.exo.append(exerciceList.exercicesTypes[i]())

    def next(self):
        currentExercice = self.exo[self.questionCount]
        print("Question " + str(self.questionCount + 1) + ": " + currentExercice.getStatement())

        while not currentExercice.hasPutCorrectAnswer():
            triedAnswer = input("Reponse proposée: ")
            currentExercice.testAnswer(triedAnswer)

        self.questionCount += 1

    def isEnded(self):
        return self.questionCount == len(self.exo)
