"""
The ShortestPathGraph object allows us to easily create graphs, and run the Dijkstra and Bellman-Ford Algorithm,
and access the shortest distance as well as shortest distance trees.

Authors: Qi Ying Lim, Jiacheng Xu
"""

from collections import defaultdict
import heapq

INF = 9999  # infinity


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
        self._cost = defaultdict(lambda: INF)
        self._inEdges = defaultdict(set)

    def get_nodes(self):
        return set(self._graph.keys())

    def set_nodes(self, nodes):
        """
        adds a list of Nodes specified by the input list nodes
        """
        for n in nodes:
            if not self.in_graph(n):
                self._graph[n] = set()

    def set_edges(self, edge_list):
        """
        Edges are input as a list of tuples, (v,w,c) where v,w are Nodes and c is the cost of the edge
        """
        for (v, w, c) in edge_list:
            if v in self.get_nodes() and w in self.get_nodes():
                self._graph[v].add(w)

                if w in set(self._graph.keys()):
                    self._inEdges[w].add(v)
                else:
                    self._inEdges[w] = set()
                    self._inEdges[w].add(v)

                # uses the edge with the smaller weight, if there are parallel edges
                self._cost[(v, w)] = min(c, self._cost[(v, w)])
            else:
                raise KeyError('No such node ' + str(v) + " or " + str(w) + " in graph")

    def get_edge_cost(self, u, v):
        return self._cost[(u, v)]

    def get_out_neighbours(self, node, k=0):
        """
        :param node: the Node in the graph
        :return: a list of the outgoing neighbours from the node
        """
        if k == 0:
            if node in self.get_nodes():
                return self._graph[node]
            else:
                raise KeyError("No such node (" + str(node) + ") in graph")
        else:
            return

    def get_in_neighbours(self, node):
        if node in self.get_nodes():
            return self._inEdges[node]
        else:
            raise KeyError("No such node (" + str(node) + ") in graph")

    def in_graph(self, node):
        return node in self.get_nodes()

    def get_num_nodes(self):
        return len(self.get_nodes())

    def get_num_edges(self):
        return len(self._cost)

    def __repr__(self):
        return str(dict(self._graph))


class ShortestPathGraph(Graph):
    def __init__(self, root):
        Graph.__init__(self)
        self._root = root
        self.set_nodes([root])
        self._dijkstra_computed = False  # prevents unnecessary re-computation of distances
        self._bellman_ford_computed = False
        # stores distances from root as returned by the dijkstra algorithm
        self._d_dist = defaultdict(lambda: INF)
        # stores distances from root as returned by the bellman-ford algorithm
        self._bf_dist = defaultdict(lambda: INF)
        # stores the parent nodes of each node in the shortest path Dijkstra tree
        self._d_prev = defaultdict()
        self._d_prev[root] = None
        # stores the parent nodes of each node in the shortest path BF tree
        self._bf_prev = defaultdict()
        self._bf_prev[root] = None
        # time it took to run Dijkstra algorithm on this graph
        self._d_time = 0

    def get_root(self):
        return self._root

    def _dijkstra(self):
        """
        An implementation of the Dijkstra's Algorithm, as taken from the pseudocode from class notes.
        Since python's heapq does not have an easily-accessible decreaseKey() function, we worked around this by
        maintaining the self._d_dist array to hold the 'correct', up-to-date distance. When we extract the minimum key
        from the heap, we first verify if this item represents the correct distance as in Line 93, before continuing as
        the pseudo-code describes.
        """
        self._dijkstra_computed = True
        # making the priority queue
        d = [(INF, node) if node != self._root else (0, node) for node in self.get_nodes()]
        self._d_dist[self._root] = 0  # setting the distance of the root to self as 0
        # loop through all the vertices
        for i in range(len(self.get_nodes())):
            (d_v, v) = heapq.heappop(d)  # extract the vertex with the minimum distance to the root
            if d_v == self._d_dist[v]:  # verifies that the popped item correctly contains the minimum distance
                for neighbour in self.get_out_neighbours(v):
                    new_distance = self._d_dist[v] + self._cost[(v, neighbour)]
                    if new_distance < self._d_dist[neighbour]:
                        self._d_dist[neighbour] = new_distance
                        # this line "decreases key" of the neighbour by pushing in a tuple containing the neighbour and
                        # the shorter distance value
                        heapq.heappush(d, (new_distance, neighbour))
                        self._d_prev[neighbour] = v

    def dijkstra_get_dist(self, node, numerical=False):
        """
        returns the value dist(root, node)
        """
        if not self._dijkstra_computed:
            self._dijkstra()
        if self._d_dist[node] == INF and not numerical:
            return "There is no path from " + str(self._root) + " to " + str(node) + "."
        elif numerical:
            return self._d_dist[node]
        else:
            return "Distance from " + str(self._root) + " to " + str(node) + " is " + str(self._d_dist[node])

    def dijkstra_get_path(self, node):
        """
        returns the shortest path from node to root
        """
        if not self._dijkstra_computed:
            self._dijkstra()
        if self._d_dist[node] == INF:
            return "There is no path from " + str(self._root) + " to " + str(node) + "."
        else:
            v = node
            path = [node]
            while self._d_prev[v] is not None:
                path.append(self._d_prev[v])
                v = self._d_prev[v]
            path.reverse()
            return path

    def dijkstra_get_tree(self):
        """
        returns the edge set representing the shortest path tree obtained by running Dijkstra
        """
        if not self._dijkstra_computed:
            self._dijkstra()
        return list(map(lambda x: (x[1], x[0]), self._d_prev.items()))

    def _bellmanford(self):
        """
        This is the implementation of bellman_ford algorithm we learned during the class. 
        I used 2d array of the pseudo-code. 
        """
        n = len(self.get_nodes())
        self._bellman_ford_computed = True
        d = [[INF] * n for _ in range(n)]
        d[self._root][0] = 0

        for k in range(1, n):
            for i in range(n):  # go through all nodes
                d[i][k] = d[i][k - 1]
                for u in self.get_in_neighbours(i):
                    if d[i][k] > d[u][k - 1] + self._cost[(u, i)]:  
                        d[i][k] = d[u][k - 1] + self._cost[(u, i)]  # modify the current distance
                        self._bf_prev[i] = u  # switch the parent node

        # (One more iteration to check the negative cycle)
        for i in range(n):
            for u in self.get_in_neighbours(i):
                if d[i][n - 1] > d[u][n - 1] + self._cost[(u, i)]:
                    # print("Negative Cycle")
                    return i

        # Assign final distance to each node
        for node in self.get_nodes():
            self._bf_dist[node] = d[node][n - 1]
        return n + 1

    def bellmanford_get_dist(self, node):
        result = 0
        if not self._bellman_ford_computed:
            result = self._bellmanford()

        # if negative cycle detcted
        if result != len(self.get_nodes()) + 1:
            #print('neg cycle detected')
            return (result,-INF)

        # if there is no path from root to node
        if self._bf_dist[node] > (INF-10):
            #print('there is no path ')
            return (INF,INF)
        else:
            #print('there is a path of length ' + str(self._bf_dist[node]))
            # return "Distance from " + str(self._root) + " to " + str(node) + " is " + str(self._bf_dist[node])
            return  (self._bf_dist[node],self._bf_dist[node])

    def bellmanford_get_path(self, node):
        """
        returns the shortest path from node to root
        """
        result = 0
        if not self._bellman_ford_computed:
            #print("Running Bellman-Ford Algorithm")
            result = self._bellmanford()
        if self._bellmanford() != len(self.get_nodes()) + 1:
            return "Negative cycle"

        if self._bf_dist[node] > (INF - 10):
            return "There is no path from " + str(self._root) + " to " + str(node) + "."
        else:
            v = node
            path = [node]
            while self._bf_prev[v] is not None:
                path.append(self._bf_prev[v])
                v = self._bf_prev[v]
            path.reverse()
            return path

    def bellmanford_get_tree(self):
        """
        returns the edge set representing the shortest path tree obtained by running Dijkstra
        """
        if not self._bellman_ford_computed:
            print("Running Bellman-Ford Algorithm")
            self._bellmanford()
        return list(map(lambda x: (x[1], x[0]), self._bf_prev.items()))
