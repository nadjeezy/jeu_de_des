from partie import Partie


class Main:
    if __name__ == '__main__':
        partie = Partie(10,3)
        partie.initialiser()
        partie.lancer()
        partie.afficher_gagnant()
        