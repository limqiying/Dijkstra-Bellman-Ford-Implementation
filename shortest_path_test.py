"""
This is a test class that allows us to randomly create graph objects to test the correctness of our implementation
"""
from graph import *
from random import randrange, sample, gauss


class NonNegativeTest:
    def __init__(self, number_of_tests=100):
        self._test_num = number_of_tests
        self._random_graphs = self._generate_random()

    def _generate_random(self):
        """
        returns a list of randomly-generated graphs. The length of this list is specified at
        initialization. We set the maximum number of nodes in a graph to be 100, and the max cost for an edge to be 30.
        """
        graph_list = []

        for i in range(self._test_num):
            g = ShortestPathGraph(0)
            num_nodes = randrange(5, 15)
            node_list = range(num_nodes)
            g.set_nodes(node_list)

            for node in node_list:
                num_neighbours = randrange(num_nodes)
                neighbours = sample(node_list, num_neighbours)  # the neighbours of node
                costs = [randrange(1, 30) for _ in range(num_neighbours)]
                n = [node] * num_neighbours
                edge_list = zip(n, neighbours, costs)
                g.set_edges(edge_list)

            graph_list.append(g)

        return graph_list

    def get_graph(self, index):
        """
        returns the graph from the list of random graphs, specified by the index
        """
        if index > len(self._random_graphs):
            return "Index out of range"
        return self._random_graphs[index]

    @staticmethod
    def brute_force_test(g, node):
        """
        computes the shortest distance from graph at index to the specified node using brute force
        """
        if node not in g.get_nodes():
            return "node " + str(node) + " does not exist."
        else:
            paths = NonNegativeTest.find_paths(g, g.get_root(), node)
            if len(paths) == 0:
                return "There is no path from root to this node"
            costs = []
            for path in paths:
                cost = sum([g.get_edge_cost(path[i], path[i + 1]) for i in range(len(path)-1)])
                costs.append(cost)
            z = list(zip(paths, costs))
            shortest = min(z, key=lambda x: x[1])
            return shortest



    @staticmethod
    def find_paths(g, start_node, end_node, path=None):
        """
        Code algorithm taken from https://stackoverflow.com/questions/2606018/path-between-two-nodes
        """
        if path is None:
            path = []
        path = path + [start_node]

        if start_node == end_node:
            return [path]

        paths = []
        for node in g.get_out_neighbours(start_node):
            if node not in path:
                new_paths = NonNegativeTest.find_paths(g, node, end_node, path)
                paths.extend(new_paths)
        return paths


test = NonNegativeTest(1)
graph = test.get_graph(0)
root = graph.get_root()
print(graph)
print(graph.dijkstra_get_dist(3))
print(NonNegativeTest.brute_force_test(graph, 3))
