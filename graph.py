"""
Creates graph object
"""

from collections import defaultdict
from sys import maxsize
import heapq

INF = maxsize  # infinity


class Graph:
    """
    creates a directed object, whose information is stored in the form of a dictionary, whose key is the vertex,
    and values are the list of neighbouring vertices. For example, if we have G where
        1 -> 2
        2 -> 3
        3 -> 1
        3 -> 2
    then our graph is stored in the dictionary:
        {1: [2], 2: [3], 3: [1,2]}
    """

    class Node:
        """
        a Node used in a Graph and Tree
        """

        def __init__(self, name):
            self._name = name  # identifier
            self._previous = None  # to be used in determining the parent in a tree
            self._distance = INF  # the shortest path from node to the particular start node
            self._weights = defaultdict()

        def name(self):
            return self._name

        def get_prev(self):
            return self._previous

        def set_prev(self, v):
            self._previous = v

        def get_dist(self):
            return self._distance

        def set_dist(self):
            return self._distance

        def get_weight(self, other):
            return self._weights[other]

        def set_weight(self, other, w):
            self._weights[other] = w

        def __repr__(self):
            return str(self._name)

    def __init__(self):
        self._graph = defaultdict(set)
        self._cost = defaultdict()

    def get_nodes(self):
        return list(self._graph.keys())

    def set_nodes(self, nodes):
        """
        adds a list of Nodes whose names are specified by the input list nodes
        """
        for n in nodes:
            self._graph[n] = set()

    def set_edges(self, edge_list):
        """
        Edges are input as a list of tuples, (v,w,c) where v,w are Nodes and c is the cost of the edge
        """
        for (v, w, c) in edge_list:
            if v in self.get_nodes() and w in self.get_nodes():
                v.set_weight(w, c)
            else:
                raise KeyError('No such node ' + str(v) + " or " + str(w) + " in graph")

    def get_out_neighbours(self, node):
        """
        :param node: the Node in the graph
        :return: a list of the outgoing neighbours from the node
        """
        if node in self.get_nodes():
            return self._graph[node]
        else:
            raise KeyError("No such node (" + str(node) + ") in graph")

    def __repr__(self):
        return str(dict(self._graph))

# class Dijkstra(Graph):
#
#     def populate_d(self, root):
#         d = [(node, INF) if node != root else (node, 0) for node in self.graph.get_nodes()]
#         heapq.heapify(d)
#         root.set_dist(0)
#
#         set_X = set()
#         for i in range(len(self.get_nodes())):
#             (v, d_v) = heapq.heappop(d)
#             set_X.add(v)
#             for neighbour in self.get_out_neighbours(v):
#                 if (v.get_dist() + v.get_weight(neighbour)) < neighbour.get_dist():

