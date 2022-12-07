#importation des bibliothèques
import networkx as nx
import random

def creer_labyrinthe(nombre_colonnes, nombre_lignes, degradation):
    """ Produit un labyrinthe au format d’un Graphe NetworkX
    """
    G = nx.Graph()
    nb_sommet = nombre_colonnes*nombre_lignes
    
    for index in range(nb_sommet):
        G.add_node(index)
        nb_ligne = index//nombre_colonnes
        index_min = nb_ligne*nombre_colonnes
        index_max = index_min + nombre_colonnes - 1
        voisins = []
        conected = False
        while conected == False:
            print("yes")
            if index - 1 >= index_min:
                voisins.append(index - 1)
            if index + 1 <= index_max: 
                voisins.append(index+1)
            if index - nombre_colonnes > 0: 
                voisins.append(index - nombre_colonnes)
            if index + nombre_colonnes < nb_sommet:
                voisins.append(index + nombre_colonnes)
            for voisin in voisins:
               if random.randint(0,1) == 0:
                   G.add_edge(index, voisin)
        conected = nx.is_connected(G)           
    return G
