import arithmetiquesUtils

class ZNZPlus:

    def __init__(self, n):
        self.n = n
        self.card = None
        self.domain = None
        self.subGroups = {} # dict of each element of (Z/nZ, +)
        self.generatorAmount = None
        self.generators = None

    def getN(self):
        return self.n

    def getCard(self):
        """
        Le cardinal/l'ordre de (Z/nZ, +) vaut n
        """
        if self.card == None:
            self.card = self.getN()

        return self.card

    def getDomain(self):
        """
        Renvoie le domaine de définition du groupe
        """
        if self.domain != None:
            return self.domain

        self.domain = [x for x in range(self.getN())]
        return self.getDomain()

    def getSubGroup(self, a):

        if a in self.subGroups:
            return self.subGroups[a]

        if not a in self.getDomain():
            # L'élément a doit être dans le groupe
            return None

        subGroup = [a]
        composedA = a

        while composedA != 0:
            composedA = (composedA + a) % self.getN()
            subGroup.append(composedA)

        self.subGroups[a] = subGroup
        return self.getSubGroup(a)

    def getGeneratorAmount(self):
        if self.generatorAmount != None:
            return self.generatorAmount

        generators = []
        generatorAmount = 0

        for e in self.getDomain():
            if arithmetiquesUtils.pgcd(e, self.getN()) == 1:
                generatorAmount += 1
                if self.generators == None:
                    generators.append(e)

        if self.generators == None:
            self.generators = generators

        self.generatorAmount = generatorAmount
        return self.getGeneratorAmount()


    def getGenerators(self):

        if self.generators != None:
            return self.generators

        generators = []

        for e in self.getDomain():
            if arithmetiquesUtils.pgcd(e, self.getN()) == 1:
                generators.append(e)

        self.generators = generators
        return self.getGenerators()
