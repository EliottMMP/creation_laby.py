#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#importation des bibliothèques
import networkx as nx

def creer_labyrinthe(nombre_colonnes, nombre_lignes, degradation):
    """ Produit un labyrinthe au format d’un Graphe NetworkX
    """
    G = nx.Graph()
    nb_sommet = nombre_colonnes*nombre_lignes
    
    
    for index in range(nb_sommet):
        G.add_node(index)
        
    return G
    
    
if __name__ == "__main__":
    # Lance le test de la fonction creer_labyrinthe()
    Labyrinthe = creer_labyrinthe(4, 3, 30)
    m = nx.adjacency_matrix(Labyrinthe)
    print(m)
    
