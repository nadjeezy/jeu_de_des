import random

class De:
    def __init__(self):
        self.valeur=0
        
    @property
    def valeur(self):
        return self._valeur
    
    @valeur.setter
    def valeur(self,valeur):
        self._valeur = valeur
        
    def getValeur(self):
        return self.valeur
        
    def lancer(self):
        self.valeur = random.randint(1,6)
        return self.valeur
