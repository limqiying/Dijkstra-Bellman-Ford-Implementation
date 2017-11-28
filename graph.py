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

    def __init__(self):
        self._graph = defaultdict(set)
        self._cost = defaultdict()

    def get_nodes(self):
        return list(self._graph.keys())

    def set_nodes(self, nodes):
        """
        adds a list of Nodes specified by the input list nodes
        """
        for n in nodes:
            self._graph[n] = set()

    def set_edges(self, edge_list):
        """
        Edges are input as a list of tuples, (v,w,c) where v,w are Nodes and c is the cost of the edge
        """
        for (v, w, c) in edge_list:
            if v in self._graph.get_nodes() and w in self._graph.get_nodes():
                self._graph[v].add(w)
                # uses the edge with the smaller weight, if there are parallel edges
                self._cost[(v, w)] = min(c, self._cost[(v, w)])
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


class ShortestPathGraph(Graph):
    def __init__(self, root):
        super(Graph, self).__init__()
        self._root = root
        self.set_nodes([root])
        # stores distances from root as returned by the dijkstra algorithm
        self._d_dist = [INF] * len(self.get_nodes())
        # stores distances from root as returned by the bellman-ford algorithm
        self._bf_dist = [INF] * len(self.get_nodes())
        # stores the parent nodes of each node in the shortest path Dijkstra tree
        self._d_prev = [None] * len(self.get_nodes())
        # stores the parent nodes of each node in the shortest path BF tree
        self._bf_prev = [None] * len(self.get_nodes())

    def dijkstra(self):
        """
        An implementation of the Dijkstra's Algorithm, as taken from the pseudocode from class notes.
        Since python's heapq does not have an easily-accessible decreaseKey() function, we worked around this by
        maintaining the self._d_dist array to hold the 'correct', up-to-date distance. When we extract the minimum key
        from the heap, we first verify if this item represents the correct distance as in Line 93, before continuing as
        the pseudocode describes.
        """
        # making the priority queue
        d = [(INF, node) if node != self._root else (0, node) for node in self.get_nodes()]
        heapq.heapify(d)
        self._d_dist[self._root] = 0  # setting the distance of the root to self as 0
        # loop through all the vertices
        for i in range(len(self.get_nodes())):
            (d_v, v) = heapq.heappop(d)  # extract the vertex with the minimum distance to the root
            if d_v == self._d_dist[v]:  # verifies that the popped item correctly contains the minimum distance
                for neighbour in self.get_out_neighbours(v):
                    new_distance = d[v] + self._cost[(v, neighbour)]
                    if new_distance < d[neighbour]:
                        self._d_dist[neighbour] = new_distance
                        # this line "decreases key" of the neighbour by pushing in a tuple containing the neighbour and
                        # the shorter distance value
                        heapq.heappush(d, (new_distance, neighbour))
                        self._d_prev[neighbour] = v


graph = ShortestPathGraph()
graph.set_nodes(range(10))
graph.set_edges([(2, 4, 6), (3, 1, 7), (1, 5, 3), (1, 9, 5), (2, 5, 3), (2, 4, 1)])
