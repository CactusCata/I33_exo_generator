from exercice import Exercice
from znz import ZNZ
from zpz import ZPZ
from znzplus import ZNZPlus
import utils
import arithmetiquesUtils
import random

exercicesTypes = []

def new():
    randomInt = utils.getRandomNumberIn(0, len(exercicesTypes) - 1)
    print(f"Exercice type numero {randomInt + 1}")
    return exercicesTypes[randomInt]()

def registerExo():
    global exercicesTypes
    exercicesTypes = [exoType1, exoType2, exoType3, exoType4, exoType5, exoType6, exoType7, exoType8, exoType9, exoType10,
        exoType11, exoType12, exoType13, exoType14, exoType15, exoType16, exoType17, exoType18, exoType19, exoType20,
        exoType21, exoType22, exoType23, exoType24, exoType25, exoType26, exoType27, exoType28, exoType29, exoType30]


def exoType1():
    """
    Calcul de phi(n) où n est un nombre non premier
    """
    n = utils.getNonPrimeNumberIn(30, 80)
    response = arithmetiquesUtils.euler_phi(n)
    statement = f"Que vaut phi({n}) ?"
    return Exercice(statement, response, [])

def exoType2():
    """
    Calcul de phi(p) où p est un nombre premier
    """
    p = utils.getPrimeNumberIn(30, 80)
    response = p - 1
    statement = f"Que vaut phi({p}) ?"
    return Exercice(statement, response, [])

def exoType3():
    """
    Calcul de phi(p * q) où p et q sont premiers entre eux
    """
    p = utils.getPrimeNumberIn(2, 5) * 2
    q = utils.getPrimeNumberIn(5, 11) * 3
    response = (p - 1) * (q - 1)
    statement = f"Que vaut phi({p * q}) ?"
    return Exercice(statement, response, [])

def exoType4():
    """
    Calcul de phi(p**k) où p est premier et k est très petit
    """
    p = utils.getPrimeNumberIn(2, 8)
    k = utils.getRandomNumberIn(2, 4)
    response = p**(k - 1) * (p - 1)
    statement = f"Que vaut phi({p**k}) ?"
    return Exercice(statement, response, [])

def exoType5():
    """
    Ordre du groupe (Z/nZ, +) où est un un grand nombre quelconque (= n)
    """
    n = utils.getRandomNumberIn(30, 500)
    response = n
    statement = f"Que vaut l'ordre du groupe (Z/{n}Z, +) ?"
    return Exercice(statement, response, [])

def exoType6():
    """
    Ordre du groupe (Z/nZ)* où n est un nombre non
    premier. (= phi(n))
    """
    n = utils.getNonPrimeNumberIn(30, 80)
    response = arithmetiquesUtils.euler_phi(n)
    statement = f"Que vaut l'ordre du groupe (Z/{n}Z)* ?"
    return Exercice(statement, response, [])

def exoType7():
    """
    Ordre du groupe (Z/pZ)* où p est un nombre premier
    (= phi(p) = p - 1)
    """
    p = utils.getPrimeNumberIn(15, 40)
    response = p - 1
    statement = f"Que vaut l'ordre du groupe (Z/{p}Z)* ?"
    return Exercice(statement, response, [])

def exoType8():
    """
    Donner le symétrique de a dans (Z/nZ, +) (= n - a)
    """
    n = utils.getRandomNumberIn(80, 700)
    a = utils.getRandomNumberIn(20, n - 1)
    response = n - a
    statement = f"Que vaut le symétrique de {a} dans (Z/{n}Z, +) ?"
    return Exercice(statement, response, [])

def exoType9():
    """
    Donner le symétrique de a dans (Z/nZ)* (avec la méthode
    d'Euclyde étendue
    """
    n = utils.getRandomNumberIn(50, 150)
    group = ZNZ(n)
    a = random.choice(group.getDomain())
    response = group.getSymetric(a)
    statement = f"Que vaut le symétrique de {a} dans (Z/{n}Z)* ?"
    return Exercice(statement, response, [])

def exoType10():
    """
    Donner le symetrique de p - 1 dans (Z/pZ)*
    (= p - 1)
    """
    p = utils.getPrimeNumberIn(10, 50)
    a = p - 1
    response = p - 1
    statement = f"Que vaut le symétrique de {a} dans (Z/{p}Z)* ?"
    return Exercice(statement, response, [])

def exoType11():
    """
    Calcul de a^(p - 1) dans (Z/pZ)* (= 1)
    """
    p = utils.getPrimeNumberIn(20, 60)
    group = ZPZ(p)
    a = random.choice(group.getDomain())
    response = 1
    statement = f"Que vaut {a}^{p - 1} dans (Z/{p}Z)* ?"
    return Exercice(statement, response, [])

def exoType12():
    """
    Calcul de a^p dans (Z/pZ)* (= a)
    """
    p = utils.getPrimeNumberIn(30, 60)
    group = ZPZ(p)
    a = random.choice(group.getDomain())
    response = a
    statement = f"Que vaut {a}^{p} dans (Z/{p}Z)* ?"
    return Exercice(statement, response, [])

def exoType13():
    """
    Calcul du sous-groupe généré par un élement a
    dans (Z/nZ, +)
    """
    n = utils.getRandomNumberIn(15, 40)
    group = ZNZPlus(n)
    a = random.choice(group.getDomain())
    response = group.getSubGroup(a)
    statement = f"Que vaut le sous-groupe engendré par {a} dans (Z/{n}Z, +) ?"
    return Exercice(statement, response, [])

def exoType14():
    """
    Calcul du sous-groupe généré par un élément a
    dans (Z/nZ)* avec n quelconque
    """
    n = utils.getRandomNumberIn(15, 30)
    group = ZNZ(n)
    a = random.choice(group.getDomain())
    response = group.getSubGroup(a)
    statement = f"Que vaut le sous-groupe généré par {a} dans (Z/{n}Z)* ?"
    return Exercice(statement, response, [])

def exoType15():
    """
    Donner l'ordre d'un élément a dans (Z/nZ, +)
    ord(a) = n / pgcd(a, n)
    """
    n = utils.getRandomNumberIn(70, 200)
    a = utils.getRandomNumberIn(20, 50)
    response = n // arithmetiquesUtils.pgcd(a, n)
    statement = f"Que vaut l'ordre de {a} dans le groupe (Z/{n}Z, +)"
    return Exercice(statement, response, [])

def exoType16():
    """
    TRES DIFFICILE
    Donner l'ordre d'un élément a dans (Z/pZ)*
    (grâce à l'isomorphisme)
    La personne doit d'abord trouver un générateur de (Z/pZ) =
    (L’element g est-il un générateur dans (Z/pZ)* ? Il suffit de vérifier si g^((p – 1)/k) != 1 [p], pour tout diviseur k de p – 1)
    pour ensuite appliquer l'isomorphisme de groupe.
    """
    p = utils.getPrimeNumberIn(15, 40)
    groupZPZ = ZPZ(p)
    a = random.choice(groupZPZ.getDomain())
    g = random.choice(groupZPZ.getGenerators())
    power = groupZPZ.getSubGroup(g).index(a)
    response = (p - 1) // arithmetiquesUtils.pgcd(power, p - 1)
    statement = f"Que vaut l'ordre de {a} dans le groupe (Z/{p}Z)* avec {p} premier ?"
    return Exercice(statement, response, [])

def exoType17():
    """
    Donner l'ordre de n - 1 dans (Z/nZ)* avec n quelconque
    = 2
    """
    n = utils.getRandomNumberIn(80, 800)
    a = n - 1
    response = 2
    statement = f"Que vaut l'ordre de {a} dans le groupe (Z/{n}Z)* ?"
    return Exercice(statement, response, [])

def exoType18():
    """
    Donner l'ordre de a dans (Z/nZ)* (bêtement)
    """
    n = utils.getRandomNumberIn(9, 20)
    group = ZNZ(n)
    a = random.choice(group.getDomain())
    response = len(group.getSubGroup(a))
    statement = f"Que vaut l'ordre de {a} dans le groupe (Z/{n}Z)* ?"
    return Exercice(statement, response, [])

def exoType19():
    """
    Donner l'ordre d'un générateur à la puissance x dans (Z/pZ)*
    grâce à l'isomorphisme
    """
    p = utils.getPrimeNumberIn(30, 60)
    groupZPZ = ZPZ(p)
    g = random.choice(groupZPZ.getGenerators())
    x = utils.getRandomNumberIn(5, 25)
    response = (p - 1) // arithmetiquesUtils.pgcd(x, p - 1)
    statement = f"Soit {g} un générateur de (Z/{p}Z)* où {p} est premier, donner l'ordre de {g}^{x} dans ce groupe."
    return Exercice(statement, response, [])

def exoType20():
    """
    Le groupe (Z/pZ)* est-il cyclique ? (oui toujours)
    """
    p = utils.getRandomNumberIn(20, 60)
    statement = f"Le groupe (Z/{p}Z) est-il cyclique ?"
    return Exercice(statement, "oui", [])

def exoType21():
    """
    Le groupe (Z/nZ)* est-il cyclique ? (oui ssi n est de la forme 2, 4, p^k, 2 * p^k)
    """
    n = -1
    response = None
    if random.random() > 0.5:
        p = utils.getPrimeNumberIn(2, 7)
        k = utils.getRandomNumberIn(1, 3)
        n = random.choice([2, 4, p**k, 2 * p**k])
        response = "oui"
    else:
        n = utils.getRandomNumberIn(5, 40)
        if ZNZ(n).getGeneratorAmount() != 0:
            return exoType21()
        response = "non"

    statement = f"Le groupe (Z/{n}Z)* est-il cyclique ?"
    return Exercice(statement, response, [])

def exoType22():
    """
    Donner le nombre de générateur de (Z/nZ, +)
    = phi(n)
    """
    n = utils.getRandomNumberIn(30, 100)
    response = arithmetiquesUtils.euler_phi(n)
    statement = f"Donner le nombre de générateur de (Z/{n}Z, +)"
    return Exercice(statement, response, [])

def exoType23():
    """
    Donner le nombre de générateur de (Z/pZ)*
    = phi(phi(p))
    """
    p = utils.getPrimeNumberIn(20, 80)
    response = arithmetiquesUtils.euler_phi(arithmetiquesUtils.euler_phi(p))
    statement = f"Combien y a t'il de générateur dans le groupe (Z/{p}Z)* ?"
    return Exercice(statement, response, [])

def exoType24():
    """
    Donner le nombre de générateur de (Z/nZ)* où n permet
    d'avoir un groupe cyclique
    """
    n = -1
    if random.random() > 0.5:
        p = utils.getPrimeNumberIn(2, 7)
        k = utils.getRandomNumberIn(1, 3)
        n = random.choice([2, 4, p**k, 2 * p**k])
    else:
        n = utils.getRandomNumberIn(5, 40)
        if ZNZ(n).getGeneratorAmount() != 0:
            return exoType24()

    group = ZNZ(n)
    response = group.getGeneratorAmount()
    statement = f"Combien y a t'il de générateur dans le groupe (Z/{n}Z)* ?"
    return Exercice(statement, response, [])

def exoType25():
    """
    Donner la liste des générateurs du groupe (Z/nZ, +)
    Ce sont les éléments premiers avec n
    """
    if random.random() > 0.5:
        # n non-premier
        n = utils.getPrimeNumberIn(20, 60)
    else:
        # n premier
        n = utils.getNonPrimeNumberIn(15, 40)
    group = ZNZPlus(n)
    response = group.getGenerators()
    statement = f"Quels sont les générateurs de (Z/{n}Z, +) ?"
    return Exercice(statement, response, [])

def exoType26():
    """
    Un élémént g est-il un générateur du groupe (Z/nZ)* ?
    """
    n = -1
    if random.random() > 0.5:
        p = utils.getPrimeNumberIn(2, 7)
        k = utils.getRandomNumberIn(1, 3)
        n = random.choice([2, 4, p**k, 2 * p**k, utils.getPrimeNumberIn(20, 50)])
    else:
        n = utils.getNonPrimeNumberIn(5, 40)
        if ZNZ(n).getGeneratorAmount() != 0:
            return exoType26()

    group = ZNZ(n)
    a = None
    response = None
    if random.random() > 0.5:
        a = random.choice(group.getGenerators())
        response = "oui"
    else:
        a = random.choice(group.getGenerators())
        if a in group.getGenerators():
            response = "oui"
        else:
            response = "non"

    statement = f"{a} est-il un générateur du groupe (Z/{n}Z)* ?"
    return Exercice(statement, response, [])

def exoType27():
    """
    L'élément g est-il un générateur dans (Z/pZ)* ?
    Il suffit de vérifier si g^((p - 1) / k) != 1 [p] pour tout diviseur k de p - 1
    """
    p = utils.getPrimeNumberIn(20, 60)
    group = ZPZ(p)

    a = None
    response = None
    if random.random() > 0.5:
        a = random.choice(group.getGenerators())
        response = "oui"
    else:
        a = random.choice(group.getDomain())
        if a in group.getGenerators():
            response = "oui"
        else:
            response = "non"

    statement = f"{a} est-il un générateur du groupe (Z/{p}Z)* ?"
    return Exercice(statement, response, [])

def exoType28():
    """
    Donner combien d'elements d'un groupe (Z/pZ)* sont de tel ordre:
    Soit un groupe cyclique d'ordre t, pour tout diviseur d de t
    il existe phi(d) éléments d'ordres d.
    """
    p = utils.getPrimeNumberIn(20, 80)
    t = arithmetiquesUtils.euler_phi(p)
    divisors = arithmetiquesUtils.getDivisors(t)
    response = {}
    for e in divisors:
        response[e] = arithmetiquesUtils.euler_phi(e)

    statement = f"Donner combien d'éléments du groupe (Z/{p}Z)* sont de tel ordre:"
    return Exercice(statement, response, [])

def exoType29():
    """
    Calculer a * (q * n + b) (= a*b) avec a E [5: 30],
    q E [2; 10] et b E [-2; 5] dans (Z/nZ, +) avec n quelconque
    """
    n = utils.getRandomNumberIn(35, 80)
    q = utils.getRandomNumberIn(2, 10)
    b = utils.getRandomNumberIn(-2, 3)
    a = utils.getRandomNumberIn(1, 30)
    response = a * b % n
    statement = f"Calculer {a} * {n * q + b} dans (Z/{n}Z, +)"
    return Exercice(statement, response, [])

def exoType30():
    """
    Calculer a^(q * n + b) (= a^b) avec a quelconque,
    q E [2 ; 5] et b E [-2 ; 3] dans (Z/nZ)* avec n quelconque
    """
    n = utils.getRandomNumberIn(20, 40)
    q = utils.getRandomNumberIn(2, 5)
    b = utils.getRandomNumberIn(-1, 2)
    a = random.choice(ZNZ(n).getDomain())
    response = pow(a, b, n)
    statement = f"Calculer {a}^{arithmetiquesUtils.euler_phi(n) * b + b} dans (Z/{n}Z)*"
    return Exercice(statement, response, [])
