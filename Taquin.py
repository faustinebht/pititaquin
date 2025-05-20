#%%
import random
n=4
taille_taquin=n*n
taquin=list(range(1,taille_taquin))
taquin.append(0)
random.shuffle(taquin)
#print(taquin)

def affiche_taquin(taquin):
    for j in range(n):
        for i in range(n):
            val = taquin[i + 4 * j]
            if val == 0:
                print("| {:^4} ".format(" "), end="")  # blank centered in 4 spaces
            else:
                print("| {:^4} ".format(val), end="")  # number centered in 4 spaces
        print("")

affiche_taquin(taquin)
#%%
for i in range(10):
    taille_taquin=n*n
    taquin=list(range(1,taille_taquin))
    taquin.append(0)
    random.shuffle(taquin)
    affiche_taquin(taquin)
    print("-----------------")
#%%
