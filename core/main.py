from data.config import *

from graphe import *
from distances import *
from prim import *

if __name__ == "__main__":
    distances = get_distances(C("cities"), C("distances_file"))
    g = Graphe({})
    distances = create_graph_from_distances(g, distances)
    matrice = g.get_matrice()

    p = Prim(matrice, C("cities"), C("start_city"), C("salesperson_number"))
    q = p.main(C("start_city"), C("salesperson_number"))[0]



