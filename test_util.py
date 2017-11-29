"""
Tools used to test our graphs in both negative and non-negative edge graphs.
Author: Qi Ying Lim
"""

from random import choice
from time import time

INF = 9999


class TestTools:
    @staticmethod
    def brute_force_result(g, node):
        """
        computes the shortest distance, and the shortest path from graph at index to specified node using brute force
        """
        if node not in g.get_nodes():
            return "node " + str(node) + " does not exist."
        else:
            paths = TestTools.find_paths(g, g.get_root(), node)
            if len(paths) == 0:
                return 0, INF
            costs = []
            for path in paths:
                cost = sum([g.get_edge_cost(path[i], path[i + 1]) for i in range(len(path) - 1)])
                costs.append(cost)
            z = list(zip(paths, costs))
            shortest = min(z, key=lambda x: x[1])
            return shortest

    @staticmethod
    def find_paths(g, start_node, end_node, path=None):
        """
        Code algorithm taken from https://stackoverflow.com/questions/2606018/path-between-two-nodes
        Recursive algorithm to find all the paths from the start and end nodes
        """
        if path is None:
            path = []
        path = path + [start_node]
        if start_node == end_node:
            return [path]

        paths = []
        for node in g.get_out_neighbours(start_node):
            if node not in path:
                new_paths = TestTools.find_paths(g, node, end_node, path)
                paths.extend(new_paths)
        return paths

    @staticmethod
    def correctness_test_2(graph_list):
        """
        Runs test on all the randomly generated graphs, with both and postive negative edges
        If there is an error, this will be raised by the assertion.
        Otherwise, a simple "test passed" will be created.
        This test only checks that the distance computed by the brute force method is equal to ths distance computed
        by bellman's algorithm.
        This avoids the problem where there might be two paths that have the same smallest distances.
        """
        test_num = 1  # counter for the number of tests
        for graph in graph_list:
            try:
                node = choice(list(graph.get_nodes()))  # randomly chooses some node in the node list
            except IndexError:
                print('graph has no nodes')
            else:
                (brute_path, brute_dist) = TestTools.brute_force_result(graph, node)
                d_dist = graph.bellmanford_get_dist(node)
                if d_dist[1] == -INF:
                    print("Negative cycle detected at node :" + str(d_dist[0]) + "Test"  + str(test_num) + " passed." )
                    # One can check by printing the graph. 
                else:
                    assert brute_dist == d_dist[0], "brute distance is " + str(brute_dist) + " while bf computed " + str(d_dist[0])
                    print("Test " + str(test_num) + " passed.")
                test_num += 1

    @staticmethod
    def get_performance(graph_list, algorithm):
        """
        param: algorithm if "D", runs Dijkstra
            if "B", runs, Bellman-Ford
        returns the two lists of tuples of (n, m, time), where n is the number of nodes, m the number of edges, and
        time is the time taken to find the shortest paths in the graph.
        First returned list is the time taken by Bellman-Ford
        Second returned list is the time taken by Dijkstra
        """
        brute_data = []
        alg_data = []
        for graph in graph_list:
            try:
                node = choice(list(graph.get_nodes()))  # randomly chooses some node in the node list
            except IndexError:
                print('graph has no nodes')
            else:
                n = graph.get_num_nodes()
                m = graph.get_num_edges()
                brute_start = time()
                TestTools.brute_force_result(graph, node)
                brute_end = time()

                if algorithm == "D":
                    alg_start = time()
                    graph.dijkstra_get_dist(node)
                    alg_end = time()
                else:
                    alg_start = time()
                    graph.bellmanford_get_dist_get_dist(node)
                    alg_end = time()

                brute_time = brute_end - brute_start
                d_time = alg_end - alg_start

                brute_data.append((n, m, brute_time))
                alg_data.append((n, m, d_time))

        return brute_data, alg_data


