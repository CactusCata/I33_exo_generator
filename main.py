from exam import Exam
import exerciceList

if __name__ == "__main__":

    exerciceList.registerExo()

    questionAmount = int(input("Veuillez saisir un nombre de question: "))
    exam = Exam(questionAmount)

    while not exam.isEnded():
        exam.next()
