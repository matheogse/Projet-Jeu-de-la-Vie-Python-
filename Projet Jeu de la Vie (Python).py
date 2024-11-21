###########################################################
#----------------------------------------------------------
#PROJET DU JEU DE LA VIE
#----------------------------------------------------------
###########################################################

###########################################################
#Import des différents  modules
###########################################################
import time
import copy
import random

###########################################################
#Class Jeux de la Vie
###########################################################
class JeuDeLaVie:
    def __init__(self, nbr_de_lignes, nbr_de_colonnes):
        """
        Affecte un tableau à deux dimensions à l’attribut tableau

        :param tableau: tableau à deux dimensions
        """
        self.nbr_de_lignes = nbr_de_lignes                                              #On initialise le nombre de lignes de la grille/du tableau
        self.nbr_de_colonnes = nbr_de_colonnes                                          #On initialise le nombre de colonnes de la grille/du tableau
        self.tableau = self.initialiser_grille(nbr_de_lignes, nbr_de_colonnes)          #On initialise le tableau/la grille en lui/elle même
        self.numero_tour = 1                                                            #On initialise le nombre de tour à 1

    def run(self, nombre_tours, delai_entre_chaque_action):                             #C'est la fonction principal qui appelle l'ensemble des autres fonctions de la class
        """
        Méthode principale du jeu.

        Fait tourner le jeu de la vie pendant nombre_tours.
        Elle rafraichit l’affichage à chaque tour
        et attend delai entre chaque tour.

        :param nombre_tours: nombre de tours à effectuer
        :param delai: temps d’attente en secondes entre chaque tour
        """
        for tour in range(nombre_tours):                                                #Les actions suivantes s'effectues à chaques tours enregistrer dans tour
                print("—————————————\nTour n°",self.numero_tour,"\n—————————————")      #On affiche en premier lieu le numéro du tour en cours
                self.afficher_grille()                                                  #On commence par afficher la grille avec les parametres mis en place dans la fonction tour
                self.tour()                                                             #Puis on met la grille à jour pour le tour suivant du jeu
                self.numero_tour+=1                                                     #On ajoute un au numéro du tour pour signaler au programme le passage au tour suivant
                time.sleep(delai_entre_chaque_action)                                   #Avant de passer au prochain tour on attend le temps entrée dans l'instance qui appelle la class

    def tour(self):
        """
        Met à jour toute les cellules du tableau en respectant les règles
        du jeu de la vie.
        """
        tableau_tour_suivant = copy.deepcopy(self.tableau)                              #On fait une copie de notre tableau dans l'objectif de passer au tableau du tour suivant et ainsi garder en mémoire le tableau initial
        for i in range(self.nbr_de_lignes):                                             #Cette boucle parcourt ici chaque lignes du tableau enregistrer dans i
            for j in range(self.nbr_de_colonnes):                                       #Cette boucle parcourt les colonnes de chaques lignes du tableau enregistrer dans j
                total_voisins = self.total_voisins(i, j)                                #A chaque passage total_voisins enregistre le nombre de voisins de la cellule de position (i,j)
                tableau_tour_suivant[i][j] = self.resultat(self.tableau[i][j], total_voisins) #Cette variable met à jour le statue des cases pour le prochain tour
        self.tableau = tableau_tour_suivant                                             #Officialisation du tableau pour le prochain et enregistrement pour resortir les bonnes données au prochain tour

    def initialiser_grille(self, nbr_de_lignes, nbr_de_colonnes):                       #Cette foncion initalise la grille de départ en la paramétrant correctement
        grille = []                                                                     #On initialise une grille vide pour la paramétrer par la suite 
        for taille_ligne in range(nbr_de_lignes):                                       #On parcours le nombre de ligne en l'enregistrant dans taille_ligne
            ligne = [random.randint(0, 1) for taille_ligne in range(nbr_de_colonnes)]   #On choisit aléatoirement ou on dispose les cases vivantes initiales
            grille.append(ligne)                                                        #On ajoute les cases vivantes à la grille
        return grille                                                                   #On retourne la grille finale du tour en action avec les bonnes cases vivantes

    def valeur_case(self, i, j):                                                        #On crer cette fonction pour obtenir la valeur de la case de coordonnes (i,j)
        """
            Renvoie la valeur de la case [i][j] ou 0 si la case n’existe pas.
        """
        if 0 <= i < self.nbr_de_lignes and 0 <= j < self.nbr_de_colonnes:               #On vérifie si les coordonnes sont conformes à celles du tableau et donc que la case existe dans le tableau
            return self.tableau[i][j]                                                   #Renvoie la valeur de la cellule à la position (i, j) dans le tableau.
        return 0                                                                        #Si les coordonnes ne sont pas valide on renvoie une cellules morte

    def total_voisins(self, i, j):
        """Renvoie la somme des valeurs des voisins de la case [i][j]."""
        voisins = [
            self.valeur_case(i - 1, j - 1),                                             #Voisin en haut à gauche
            self.valeur_case(i - 1, j),                                                 #Voisin en haut 
            self.valeur_case(i - 1, j + 1),                                             #Voisin en haut à droite
            self.valeur_case(i, j - 1),                                                 #Voisin de gauche
            self.valeur_case(i, j + 1),                                                 #Voisin de droite
            self.valeur_case(i + 1, j - 1),                                             #Voisin en bas à gauche
            self.valeur_case(i + 1, j),                                                 #Voisin en bas
            self.valeur_case(i + 1, j + 1)                                              #Voisin en bas à droite
        ]
        return sum(voisins)                                                             #On retourne la somme des voisins réutilisé dans la fonction tour pour ensuite faire fonctionner le jeu et garder/supprimer/ajouter les diverses cases

    def resultat(self, valeur_case, total_voisins):
        """
        Renvoie la valeur suivante d’une la cellule.

        :param valeur_case: la valeur de la cellule (0 ou 1)
        :param total_voisins: la somme des valeurs des voisins
        :return: la valeur de la cellule au tour suivant

        >>> a = JeuDeLaVie([])
        >>> a.resultat(0, 3)
        1
        >>> a = JeuDeLaVie([])
        >>> a.resultat(0, 1)
        0
        >>> a = JeuDeLaVie([])
        >>> a.resultat(0, 4)
        0
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 2)
        1
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 3)
        1
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 1)
        0
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 4)
        0
        """
        if valeur_case == 1:                                                            #Si la valeur de la case est egal a 1 soit qu'elle est vivante
            if total_voisins < 2 or total_voisins > 3:                                  #Et que si le nombre total de voisin est <2 ou >3
                return 0                                                                #Alors on retourne 0 (case morte)
            else:                                                                       #Sinon
                return 1                                                                #Alors on retourne 1 (case vivante)
        else:                                                                           #Si la valeur de la case est differente de 1 soit qu'elle est morte
            if total_voisins == 3:                                                      #Et que si le nombre total de voisin est égal à 3
                return 1                                                                #Alors on retourne 1 (case vivante)
            else:                                                                       #Sinon
                return 0                                                                #Alors on retourne 0 (case morte)

    def afficher_grille(self):                                                          #Fonction crer pour afficher correctement la grille
        for nombre_de_lignes in range(self.nbr_de_lignes):                              #On parcours chaques lignes que l'on enregistre dans nombre_de_lignes
            for nombre_de_colonnes in range(self.nbr_de_colonnes):                      #On parcours chaques colonnes que l'on enregistre dans nombre_de_colonnes
                if self.tableau[nombre_de_lignes][nombre_de_colonnes] == 1:             #Si case vivante
                    print("🀫", end=" ")                                                 #Alors afficher
                else:                                                                   #Sinon
                    print(" ", end=" ")                                                 #Afficher un vide
                if nombre_de_colonnes < self.nbr_de_colonnes - 1:
                    print("|", end=" ")                                                 #Entre chaques case séparer avec une barre verticale
            print()                                                                     #Sauter une ligne à chaque tour pour bien visualiser le tableau
            if nombre_de_lignes < self.nbr_de_lignes - 1:
                print("——" * (self.nbr_de_colonnes * 2 - 1))
        print("\n" * 2)                                                                 #Affiche la ligne délimitant chaque ligne de la grille
        
print("————————————————————————————————————————————————————————————————————\nATTENTION : Le programme choisi une configuration de depart aléatoire pour le JEU DE LA VIE \n————————————————————————————————————————————————————————————————————")

###########################################################
# Dimensions grille
###########################################################
nbr_de_lignes = int(input("Donnez le nombre de ligne que votre grille va comporter : "))
nbr_de_colonnes = int(input("Donnez le nombre de colonnes que votre grille va comporter : "))

###########################################################
# On crer une instance du jeu avec une grille aléatoire
###########################################################
mon_jeu = JeuDeLaVie(nbr_de_lignes, nbr_de_colonnes)

###########################################################
# On éxécute le jeu 
###########################################################
mon_jeu.run(100, 0.1)
