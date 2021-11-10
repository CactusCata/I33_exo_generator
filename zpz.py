import arithmetiquesUtils

class ZPZ:

    def __init__(self, p):
        self.p = p
        self.card = None
        self.domain = None
        self.subGroups = {}
        self.generatorAmount = None
        self.generators = None

    def getP(self):
        return self.p

    def getCard(self):
        return self.getP() - 1

    def getDomain(self):
        if self.domain != None:
            return self.domain

        self.domain = [i for i in range(1, self.getP())]
        return self.domain

    def getSymetric(self, a):
        if a in self.getDomain():
            return arithmetiquesUtils.euclide_e(a, self.getP())[1]

    def getSubGroup(self, a):

        if self.subGroups != None and a in self.subGroups:
            return self.subGroups[a]

        if a not in self.getDomain():
            # L'élément a n'est pas dans le groupe
            return None

        composedA = a
        subGroup = [a]
        while composedA != 1:
            composedA = (composedA * a) % self.getP()
            subGroup.append(composedA)

        self.subGroups[a] = subGroup
        return self.getSubGroup(a)

    def getGeneratorAmount(self):
        if self.generatorAmount != None:
            return self.generatorAmount

        self.generatorAmount = arithmetiquesUtils.euler_phi(arithmetiquesUtils.euler_phi(self.getP()))
        return self.getGeneratorAmount()

    def getGenerators(self):
        if self.generators != None:
            return self.generators

        generators = []
        divisors = arithmetiquesUtils.getDivisors(self.getP() - 1)[1:]

        for a in self.getDomain():
            maybeIsGenerator = True
            i = 0
            while maybeIsGenerator and i < len(divisors):
                if pow(a, (self.getP() - 1) // divisors[i], self.getP()) == 1:
                    maybeIsGenerator = False
                i += 1
            if maybeIsGenerator:
                generators.append(a)

        self.generators = generators
        return self.getGenerators()


if __name__ == "__main__":
    group1 = ZPZ(7)
    print(group1.getGenerators())
