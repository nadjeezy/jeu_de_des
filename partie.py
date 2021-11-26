from gobelet import Gobelet
from joueur import Joueur


class Partie:
    def __init__(self,tours,des):
        self.tours = tours
        self.des=des
        self.gobelet=Gobelet(des)
        self.remplir_tab_joueur()
    
    def remplir_tab_joueur(self):
        self.joueurs = [Joueur("")]
        for i in range (2):
            self.joueurs.append(Joueur(input("Nom du joueur "+str(i+1)+" : ")))
            
    @property
    def tours(self):
        return self._tours
    
    @tours.setter
    def tours(self,tours):
        self._tours = tours
        
    @property
    def des(self):
        return self._des
    
    @des.setter
    def des(self,des):
        self._des = des
        
    @property
    def gobelet(self):
        return self._gobelet
    
    @gobelet.setter
    def gobelet(self,gobelet):
        self._gobelet = gobelet
        
    def initialiser(self):
        self.joueurs[1].score=0
        self.joueurs[2].score=0
        
    def lancer(self):
        cpt_tour = 1
        print(self.joueurs[1].getNom() + " : " + self.joueurs[1].afficher_score())
        print(self.joueurs[2].getNom() + " : " + self.joueurs[2].afficher_score()+"\n")
        while(cpt_tour <= self.tours):
            self.joueurs[2].jouer(self.gobelet)
            self.gobelet.valeur=0
            self.joueurs[1].jouer(self.gobelet)
            self.gobelet.valeur=0
            print("Tour n°"+str(cpt_tour)+"\n----------\n")
            print(self.joueurs[1].getNom() + " : " + self.joueurs[1].afficher_score())
            print(self.joueurs[2].getNom() + " : " + self.joueurs[2].afficher_score()+"\n")
            cpt_tour +=1
    
    def afficher_gagnant(self):
        if self.joueurs[1].getScore() < self.joueurs[2].getScore():
            print("Le joueur "+self.joueurs[2].getNom()+" a gagné !!")
        elif self.joueurs[1].getScore() == self.joueurs[2].getScore():
            print("Les joueurs sont à égalité avec un score de "+self.joueurs[1].getScore()+" ! Il n'y a pas de vainqueur")
        else:
            print("Le joueur "+self.joueurs[1].getNom()+" a gagné !!")
        
# partie = Partie(10,3)
# partie.initialiser()
# partie.lancer()
# partie.afficher_gagnant()
        