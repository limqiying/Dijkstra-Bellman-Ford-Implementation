from graph import *
from test_util import *
from random import randrange, sample, gauss


class NegativeTest:
    def __init__(self, number_of_tests=100):
        self._test_num = number_of_tests
        self._random_pos_graphs = self._generate_pos()
        self._random_neg_graphs = self._generate_neg()

    def _generate_pos(self):
        """
        returns a list of randomly-generated graphs. The length of this list is specified at
        initialization. We set the maximum number of nodes in a graph to be 100, and the max cost for an edge to be 30.
        """
        graph_list = []

        for i in range(self._test_num):
            g = ShortestPathGraph(0)
            num_nodes = randrange(5, 10)
            node_list = range(num_nodes)
            g.set_nodes(node_list)

            for node in node_list:
                num_neighbours = randrange(5)
                neighbours = sample(node_list, num_neighbours)  # the neighbours of node
                costs = [randrange(1, 30) for _ in range(num_neighbours)]
                n = [node] * num_neighbours
                edge_list = zip(n, neighbours, costs)
                g.set_edges(edge_list)

            graph_list.append(g)

        return graph_list

    def _generate_neg(self):
        """
        returns a list of randomly-generated graphs. The length of this list is specified at
        initialization. We set the maximum number of nodes in a graph to be 100, and the max cost for an edge to be 30.
        """
        graph_list = []

        for i in range(self._test_num):
            g = ShortestPathGraph(0)
            num_nodes = randrange(5, 10)
            node_list = range(num_nodes)
            g.set_nodes(node_list)

            for node in node_list:
                num_neighbours = randrange(5)
                neighbours = sample(node_list, num_neighbours)  # the neighbours of node
                costs = [randrange(-3, 10) for _ in range(num_neighbours)]
                n = [node] * num_neighbours
                edge_list = zip(n, neighbours, costs)
                g.set_edges(edge_list)

            graph_list.append(g)

        return graph_list

    def get_graph(self, index):
        """
        returns the graph from the list of random graphs, specified by the index
        """
        if index >= len(self._random_graphs):
            return "Index out of range"
        return self._random_graphs[index]

    def run_correctness_pos(self):
        TestTools.correctness_test_2(self._random_pos_graphs)

    def run_correctness_neg(self):
        TestTools.correctness_test_2(self._random_neg_graphs)
