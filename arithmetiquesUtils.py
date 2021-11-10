def pgcd(a, b):
    while b:
        cached = a
        a = b
        b = cached % b
    return a

def euler_phi(n):
    """
    La fonction φ d'Euler est définie pour tout entier n par :
    φ(n) = card({i∈N t.q. i⩽n et pgcd(i,n)=1})

    NB: J'ai utilisé la décomposition en produit de facteurs
    premiers
    """
    primeTest = 2
    res = 1
    while n != 1:
        count = 0
        while n % primeTest == 0:
            count += 1
            n //= primeTest
        if count != 0:
            res *= (primeTest**(count - 1)) * (primeTest - 1)
        primeTest += 1

    return res

def getDivisors(n):
    divisorsStart = []
    divisorsEnd = []
    i = 1
    while i < n**0.5:
        if n % i == 0:
            divisorsStart.append(i)
            divisorsEnd.append(n // i)
        i += 1

    divisorsEnd.reverse()

    if i == n**0.5:
        divisorsStart.append(i)

    return divisorsStart + divisorsEnd

def decompose(n):
    """
    Tout entier n se décompose de façon unique sous la forme
    n = ∏ (p_i ** e_i) où les p_i sont des nombres premiers.
    L'objectif de cet exercice est de programmer la fonction decompose(n) qui renvoie la liste des p_i
    Exemple : decompose(99999876400)
    renvoie la liste [2,5,29,1483,5813] car 99999876400=24×52×29×1483×5813

    Pour obtenir la décomposition de l'entier n en facteurs premiers, on peut procéder de la façon suivante:

    on commence par regarder si n est pair et si c'est le cas on divise n
    par 2 tant que cela est possible et 2 est ajouté à la liste des facteurs premiers.
    en parcourant les entiers i par pas de 2 à partir de i=3,
    si i divise n on le rajoute dans la liste et on divise n par i tant que cela est possible.
    On arrête ce parcours lorsque n = 1.
    """
    factors = []
    primeTest = 2
    last = -1
    while n % primeTest == 0:
        n >>= 1
        if last != primeTest:
            last = primeTest
            factors.append(primeTest)
    primeTest += 1

    while n != 1:
        while n % primeTest == 0:
            n //= primeTest
            if last != primeTest:
                factors.append(primeTest)
                last = primeTest
        primeTest += 2
    return factors

def euclide_e(a, n):
    """
    Soient a et n deux entiers, l'algorithme d'Euclide étendu permet de calculer u et v dans Z tels que au+vn=pgcd(a,n).
    Ecrire la fonction euclide_e(a,n) qui renvoie la liste [u,v,pgcd(a,n)].
    """
    u_1 = n
    v_1 = 1
    w_1 = 0
    u_2 = a
    v_2 = 0
    w_2 = 1

    while u_1 % u_2 != 0:
        u_3 = u_1 % u_2
        v_3 = v_1 - (u_1 // u_2) * v_2
        w_3 = w_1 - (u_1 // u_2) * w_2

        u_1 = u_2
        v_1 = v_2
        w_1 = w_2

        u_2 = u_3
        v_2 = v_3
        w_2 = w_3

    return [v_2, w_2, u_2]

if __name__ == "__main__":
    print(getDivisors(50))
