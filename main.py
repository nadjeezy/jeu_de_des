from partie import Partie


class Main:
    if __name__ == '__main__':
        partie = Partie(int(input("Veuillez entrer le nombre de tours : ")),int(input("Veuillez entrer le nombre de dés :")))
        partie.initialiser()
        partie.lancer()
        partie.afficher_gagnant()
        