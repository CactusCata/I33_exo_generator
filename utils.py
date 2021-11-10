import random

def getRandomNumberIn(min, max):
    return (int(random.random() * (max + 1 - min))) + min

def getRandomOdd(min, max):
    """
    Return a random number between min and max
    who is odd (impair)
    """
    res = getRandomNumberIn(min, max)
    return res if res % 2 == 1 else getRandomOdd(min, max)

def getRandomPeer(min, max):
    """
    Return a random number between min and max
    who is peer (pair)
    """
    res = getRandomNumberIn(min, max)
    return res if res % 2 == 0 else getRandomPeer(min, max)

def getSophieGermainIn(max):
    eraPrimesNumbers = eratostene(max)

    sophieGermainNumbers = []
    for i in range(len(eraPrimesNumbers)):
        if eraPrimesNumbers[i] and (eraPrimesNumbers[(i - 1) // 2]):
            sophieGermainNumbers.append(i)

    return sophieGermainNumbers

def getNonPrimesNumbersIn(min, max):
    """
    Retourne un tableau contenant tous les nombres
    non premiers de min à max
    """
    eraPrimesNumbers = eratostene(max)
    nonprimeNumbers = []
    for i in range(min, len(eraPrimesNumbers)):
        if not eraPrimesNumbers[i]:
            nonprimeNumbers.append(i)
    return nonprimeNumbers

def getNonPrimeNumberIn(min, max):
    """
    Retourne un nombre non premier entre
    min et max
    """
    return random.choice(getNonPrimesNumbersIn(min, max))

def getPrimesNumbersIn(min, max):
    """
    Retourne un tableau contenant tous les nombres
    premiers de min à max
    """
    eraPrimesNumbers = eratostene(max)
    primeNumbers = []
    for i in range(min, len(eraPrimesNumbers)):
        if eraPrimesNumbers[i]:
            primeNumbers.append(i)
    return primeNumbers

def getPrimeNumberIn(min, max):
    """
    Retourne un nombre premier entre min
    et max
    """
    return random.choice(getPrimesNumbersIn(min, max))

def eratostene(max):
    """
    Permet de récuperer sous le forme d'un tableau
    de boolean tous les entiers à leurs place avec
    une valeur vrai/faux correspondant à leur
    statut de nombre premier ou non
    """

    eraPrimesNumbers = [True] * (max + 1)
    eraPrimesNumbers[0] = eraPrimesNumbers[1] = False

    for i in range(2, max + 1):
        if eraPrimesNumbers[i]:
            for j in range(i + 1, max + 1):
                if eraPrimesNumbers[j] and j % i == 0:
                    eraPrimesNumbers[j] = False

    return eraPrimesNumbers

if __name__ == "__main__":
    for i in range(50):
        print(getRandomElementInArray([1, 2, 3]))
