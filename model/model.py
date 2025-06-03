import copy

import networkx as nx
from database.DAO import DAO
from model.store import Store

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}
        self._stores = DAO.getAllStores()

    def buildGraph(self, store, n):
        ID = self._ottieniID(store)
        self._nodes = DAO.getAllNodes(ID.store_id)
        self._graph.add_nodes_from(self._nodes)
        for v in self._graph.nodes:
            self._idMap[v.order_id] = v
        self.addPeso(ID.store_id)
        self.addEdges(ID.store_id, n)

    def addEdges(self, store, n):
        for u in self._graph.nodes:
            lista = DAO.getAllEdges(store, u, n)
            if len(lista) > 0:
                for order in lista:
                    if (u.order_id != order):
                        order_obj = self._idMap[order]
                        if not (self._graph.has_edge(u, order_obj)):
                            self._graph.add_edge(u, order_obj, weigth = u.quantity + order_obj.quantity)

    def addPeso(self, ID):
        for n in self._graph.nodes:
            valore = DAO.getPeso(ID, n)
            n.quantity = valore

    def getPath(self, n):
        path = nx.dag_longest_path(self._graph, self._graph.nodes[n])
        return path


    def getNumNodes(self):
        return len(self._graph.nodes())

    def getNumEdges(self):
        return len(self._graph.edges())

    def _ottieniID(self, store):
        for v in self._stores:
            self._idMap[v.store_name] = v
        return self._idMap[store]
