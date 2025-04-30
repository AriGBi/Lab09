from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.lista_aereoporti=DAO.getAllAeroporti()
        self._idMapAeroporto={}
        for i in self.lista_aereoporti:
            self._idMapAeroporto[i.ID]=i


    def build_graph(self,x):
        grafo=nx.Graph()
        elenco_edges=DAO.getEdges(x)
        for edge in elenco_edges:
            aereoportoP= self._idMapAeroporto[edge[0]]
            aeroportoA=self._idMapAeroporto[edge[1]]
            distanza_media=edge[2]
            grafo.add_edge(aereoportoP,aeroportoA, weight=distanza_media)

        return grafo.number_of_nodes(), grafo.number_of_edges(), grafo



