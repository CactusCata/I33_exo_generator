import arithmetiquesUtils

class ZNZ:

    def __init__(self, n):
        self.n = n
        self.card = None
        self.domain = None
        self.subGroups = {}
        self.generatorAmount = None
        self.generators = None

    def getN(self):
        return self.n

    def getCard(self):
        """
        On calcul le cardinal d'un tel groupe avec
        la fonction phi(n)
        """
        if self.card != None:
            return self.card

        if self.domain != None:
            self.card = len(self.domain)
            return self.getCard()

        self.card = arithmetiquesUtils.euler_phi(self.n)

        return self.card

    def getDomain(self):
        """
        On inscrit tous les elements de ce
        groupe
        """
        if self.domain != None:
            return self.domain

        self.domain = []
        for i in range(1, self.getN()):
            if hasSymetric(i, self.getN()):
                self.domain.append(i)

        return self.getDomain()

    def getSymetric(self, a):
        domain = self.getDomain()
        if a in domain:
            return (arithmetiquesUtils.euclide_e(a, self.getN())[1] + self.getN()) % self.getN()

    def getSubGroup(self, a):

        if self.subGroups != None and a in self.subGroups:
            return self.subGroups[a]

        if a not in self.getDomain():
            # L'élément a n'est pas dans le groupe
            return None

        composedA = a
        subGroup = [a]
        while composedA != 1:
            composedA = (composedA * a) % self.getN()
            subGroup.append(composedA)

        self.subGroups[a] = subGroup
        return self.getSubGroup(a)

    def isCyclicGroup(self):
        if self.getN() == 2 or self.getN() == 4:
            return True

        decompositionOfN = arithmetiquesUtils.decompose(self.getN())

        if len(decompositionOfN) == 1:
            return True

        if 2 in decompositionOfN and len(decompositionOfN) == 2:
            return True

        return False

    def getGeneratorAmount(self):
        if self.generatorAmount != None:
            return self.generatorAmount

        if self.isCyclicGroup():
            self.generatorAmount = arithmetiquesUtils.euler_phi(self.getN())
        else:
            self.generatorAmount = 0

        return self.getGeneratorAmount

    def getGenerators(self):
        if self.generators != None:
            return self.generators

        if not self.isCyclicGroup():
            return []

        generators = []
        for a in self.getDomain():
            if len(self.getSubGroup(a)) == self.getCard():
                generators.append(a)

        self.generators = generators
        return self.getGenerators()

def hasSymetric(a, n):
    return arithmetiquesUtils.pgcd(a, n) == 1

if __name__ == "__main__":
    group = ZNZ(39)
    print(group.getCard())
    print(group.getDomain())
