# Jeu de dés

Le but de l'exercice est de créer un jeu de dés classique dans lequel des joueurs joueront à tour de rôle en lançant un gobelet, qui contiendra des dés. Au bout d'un certain nombre de tour, On désigne le gagnant.
Le gagnant est le joueur qui a le score le plus élevé. Pour cela nous allons devoir définir plusieurs classes.

---

## Classe Dé
La classe Dé est celle qui représente un De du gobelet.
Celle-ci a :
  Un attribut :
  - Valeur : un nombre représentant la valeur d'un lancer de dé
  Un constructeur :
  - Sans arguments
  - Qui initialise la valeur du dé à 0
  Ainsi que 2 méthodes :
  - get_valeur() : renvoie la valeur du dé
  - lancer() : change la valeur du dé -> cette valeur doit être un nombre généré aléatoirement entre 1 et 6

## Classe Gobelet
La classe Gobelet représente le gobelet utilisé dans la partie.
Celui-ci a :
  Deux attributs :
  - Valeur : nombre représentant la valeur d'un lancer du gobelet
  - Des : tableau de dés qui contient un certain nombre de dés
  Un constructeur
  - Avec un argument
    o constructor(nb_des) : initialise la valeur du gobelet à 0, génère le nombre de dés nécessaires à la partie et les ajoute au tableau des
  Ainsi que 3 méthodes :
  - get_valeur() : renvoie la valeur du gobelet
  - lancer() : change la valeur des dés du gobelet ; met à jour la valeur du gobelet
  - afficher_score() : affiche en console le score du dernier lancé de gobelet

## Classe Joueur
La classe Joueur représente une personne participant à la partie :
Celui-ci à :
  Deux attributs :
  - Nom : chaîne de caractères représentant le nom du joueur
  - Score : nombre représentant le score du joueur (à un instant t)
  Un constructeur :
  - Avec un argument
    o constructor(nom) : initialise la valeur du nom du joueur à partir du paramètre nom, initialise le score du joueur à 0
  Ainsi que 4 méthodes :
  - get_nom() : renvoie le nom du joueur
  - get_score() : renvoie le score du joueur
  - jouer(gobelet) : prend en paramètre le gobelet de la partie, lance le gobelet, met à jour le score du joueur en fonction du résultat du lancé
  - afficher_score() : affiche en console le score du joueur

## Classe Partie
La classe Partie représente une partie de dés.
Celui-ci à :
  Trois attributs :
  - joueurs : tableau de joueurs
  - nb_tours : entier représentant le nombre de tours à jouer
  - gobelet : gobelet de dés
  Un constructeur :
  - Avec deux arguments
    o constructor(nb_tours, nb_des) : crée l'objet Partie en récupérant le nombre de tours et nombre de dés
  Ainsi que 3 méthodes :
  - initialiser() : permet d'inscrire des joueurs dans la partie
  - lancer() : lance la partie : chaque joueur joue à tour de rôle pendant les n tours. Une fois la partie terminée, affiche le gagnant.
  - afficher_gagnant() : compare les scores des joueurs et affiche le gagnant.

---
## Lancement du jeu
Executez la classe main.py
