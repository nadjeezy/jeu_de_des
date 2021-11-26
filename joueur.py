from gobelet import Gobelet


class Joueur:
    def __init__(self,nom):
        self.nom=nom
        self.score=0
        
    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self,nom):
        self._nom = nom
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,score):
        self._score = score
        
    def getNom(self):
        return self.nom
    
    def getScore(self):
        return self.score
    
    def jouer(self,gobelet:Gobelet):
        somme = gobelet.lancer()
        self.score += somme
        return self.score
    
    def afficher_score(self):
        return f"Le score est {self.score}"
    
# j = Joueur("benoit")
# gob = Gobelet(4)

# print(j.jouer(gob))
# j.afficher_score()