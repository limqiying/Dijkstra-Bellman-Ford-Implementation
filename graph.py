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
                self._cost[(v, w)] = c
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
        self._d_dist = [INF]*len(self.get_nodes())    # stores distances from root as returned by the dijkstra algorithm
        self._bf_dist = [INF]*len(self.get_nodes())   # stores distances from root as returned by the bellman-ford algorithm

    @staticmethod
    def decrease_key(heap, item):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (dist, node) in enumerate(heap):
            if node is item:
                del heap[index]
                heap.append(item)
                heapq.heapify(heap)

    def dijkstra(self, root):
        d = [(INF, node) if node != root else (0, node) for node in self.get_nodes()]
        heapq.heapify(d)
        self._d_dist[root] = 0

        set_x = set()
        for i in range(len(self.get_nodes())):
            (d_v, v) = heapq.heappop(d)
            set_x.add(v)
            for neighbour in self.get_out_neighbours(v):
                if (d[v] + v.get_weight(neighbour)) < d[neighbour]:
                    siftdown(d, d[0],)

