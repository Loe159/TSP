class Graphe:
    """graph = { "a" : {"b":2,"c":1},
       ...
    }"""
    def __init__(self,graphe={},oriente = False):
        self.graphe = graphe
        self.oriente = oriente

    def ajouter_sommet(self,s):
        assert s not in self.graphe , "le sommet existe déjà"
        self.graphe[s] = {}

    def ajouter_arete(self,s1,s2,poids=1):
        if s1 not in self.graphe:
            self.graphe[s1]={}
        if s2 not in self.graphe:
            self.graphe[s2] = {}

        self.graphe[s1][s2]=poids
        if not self.oriente:
            self.graphe[s2][s1]=poids

    def liste(self):
        for s1 in self.graphe:
            print(s1, ' -> ', self.graphe[s1])

    def ordre(self):
        return len(self.graphe)

    def degre(self,s):
        return len(self.graphe[s])

    def get_matrice(self):
        rang = {}
        i = 0
        #affecte un rang à chaque sommet pour cosntruire la matrice
        for sommet in self.graphe:
            rang[sommet]=i
            i+=1
        #init la matrice avec des 0
        matrice = [[0]*len(self.graphe) for i in range(len(self.graphe))]

        for sommet1 in self.graphe:
            for sommet2 in self.graphe[sommet1]:
                matrice[rang[sommet1]][rang[sommet2]]=self.graphe[sommet1][sommet2]
        return matrice

    def matrice(self):
        matrice = self.get_matrice()
        for ligne in matrice:
            print(ligne)