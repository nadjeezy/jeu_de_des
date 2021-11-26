from de import De


class Gobelet:
    
    def __init__(self,nbde):
        self.valeur=0
        self.nbde = nbde
        self.remplir_tab(nbde)
        
    @property
    def valeur(self):
        return self._valeur
    
    @valeur.setter
    def valeur(self,valeur):
        self._valeur = valeur
    
    @property
    def nbde(self):
        return self._nbde
    
    @nbde.setter
    def nbde(self,nbde):
        self._nbde = nbde
        
    def remplir_tab(self,n):
        self.tabDes = [De()]
        for i in range (1,n):
            self.tabDes.append(De())        
        
    def getValeur(self):
        return self.valeur
    
    def lancer(self):
        for i in self.tabDes:
            i.lancer()
            self.valeur = self.valeur + i.getValeur()
        return self.valeur
        
    def afficher_score(self):
        print(f"La valeur du gobelet est {self.valeur}")
    
# gobelet = Gobelet(4)
# print(gobelet.lancer())
# gobelet.afficher_score()

