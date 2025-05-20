#!/usr/bin/python3
#-*-coding : utf-8-*-

from random import shuffle

def generate_taquin(taille):
    L = list(range(1,taille*taille+1,1))
    shuffle(L)
    return L 

def affiche_taquin(taquin,taille):
    for j in range(taille):
        for i in range(taille):
            val = taquin[i + 4 * j]
            if val == taille*taille:
                print("| {:^4} ".format(" "), end="")  # blank centered in 4 spaces
            else:
                print("| {:^4} ".format(val), end="")  # number centered in 4 spaces
        print("|")
        print("")   

affiche_taquin(generate_taquin(4), 4)
affiche_taquin(list(range(1,17,1)),4)

def resoudre_taquin(taquin):
    #on veut résoudre le taquin. Pour ça, on veut déterminer les permutations nécessaires. 
    #Ça revient à inverser une matrice ? le taquin dans l'ordre fait 
    
    pass