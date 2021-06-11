def tri_personnalisé (e):
    return len (e)


def afficher ( collection,n_premiers_elements=-1):
    # "--- LISTE des PIZZAS (4)---"
    # afficher les pizzas 1 pizza par ligne 
    # "AUCUNE PIZZA" 
    #collection.sort(reverse=True,key=tri_personnalisé)
    c= collection[0:n_premiers_elements]
    if not n_premiers_elements == -1:
        c = collection [:n_premiers_elements]

    nb_pizzas = len (c)
    if nb_pizzas == 0:
        print("AUCUNE PIZZA")
    else :
        print(f"--- LISTE DES PIZZAS({(nb_pizzas)})---")
        for i in collection:
            print(i)
        print()
        print("Première pizza :"+ c [0] )
        print("Dernière pizza :" + c [-1])
        # première pizza
        # la dernière pizza 
def ajouter_pizza_utilisateur (c):
    p = input("Pizza à ajouter : ")
    #if pizza_existe(p,collection):
    if p in c:
        print("ERREUR: Cette pizza existe déjà")
    else:
        c.append(p)
# def pizza_existe(e,collection):
#      for i in collection:
#       if i == e:
#           return True
#    return False


pizzas =["4 fromages","végétarienne","hawai","calzone"]

# pizza_existe ->bool
# True : la pizza existe -> print ("ERREUR :la pizza existe déjà ")
# False : elle n'existe pas -> append 

vide =()
afficher (vide,2)


