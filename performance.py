"""
Script used to get and plot performance data for both algorithms
requires matplotlib as dependency
"""
from non_neg_test import *
from neg_test import *
from math import log
import matplotlib.pyplot as plt
import numpy as np


class PerformanceTest:

    def __init__(self, num_data=1000):
        self._test = NonNegativeTest(num_data)
        self._data = self._test.get_performance_data()
        self._nm_dict = dict()  # key = (n, m), value is a list of randomly generated graphs with n nodes and m edges
        self._brute_data, self._d_data, self._bf_data = self._data

    def get_dij_data(self):
        return self._d_data

    def generate_random(self, n, m, neg_cost=False):
        """
        generates a list of k randomly-generated graphs, with n nodes and m edges.
        edge costs are randomly generated
        stores this list in the test dictionary
        """
        graph_list = []
        for i in range(100):
            g = ShortestPathGraph(0)
            node_list = range(n)
            g.set_nodes(node_list)

            edges = set()
            costs = [randrange(1,30) if not neg_cost else randrange(-5, 30) for _ in range(m)]
            while len(edges) != m:
                edge = sample(node_list, 2)  # the neighbours of node
                edges.add((edge[0], edge[1]))
            edges = list(edges)
            edge_list = [(edges[i][0], edges[i][1], costs[i]) for i in range(m)]
            g.set_edges(list(edge_list))
            graph_list.append(g)
        self._nm_dict[(n, m)] = graph_list

    def plot_compare_pos(self, n, m):
        """
        generates a plot that shows the times for brute force, dijkstra, and bellman ford
        """
        if (n, m) not in self._nm_dict.keys():
            self.generate_random(n, m)
        nm_graphs = self._nm_dict[(n, m)]
        performance = TestTools.get_performance(nm_graphs)
        times = [list(list(zip(*s))[2]) for s in performance]

        labels = ["Brute Force", "Dijkstra", "Bellman-Ford"]
        colors = ["blue", "red", "green"]

        fig, ax = plt.subplots()
        width = 0.4
        for i, l in enumerate(labels):
            x = np.ones(100) + i -1
            y = np.array(times[i])
            ax.scatter(x, y, color=colors[i])
            mean = sum(times[i]) / 100
            ax.plot([i - width / 2., i + width / 2.], [mean, mean], color="k")
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels)
        flat_list = [item for sublist in times for item in sublist]
        plt.ylim((min(flat_list) - 0.00001, max(flat_list) + 0.00001))
        plt.title("Running times for n = " + str(n) + " and m = " + str(m))
        plt.show()

    def plot_dijk_log(self, brute_force_show=False):
        """
        Plots the graph of time versus n*logn +m for Dijkstra
        :param brute_force_show: if True, then the time versus n*logn +m for brute force will be in the same plot
        :return:
        """
        nodes, edges, y = zip(*self._d_data)
        x = [(n * log(n, 2) + m) for n, m in zip(nodes, edges)]

        if brute_force_show:
            nodes, edges, y2 = zip(*self._brute_data)
            x2 = [(n * log(n, 2) + m) for n, m in zip(nodes, edges)]
            plt.plot(x2, y2, 'bs', label='Brute Force')
        plt.plot(x, y, 'ro', label='Dijkstra')

        plt.title('Dijkstra Performance')
        plt.xlabel("nlogn + m")
        plt.ylabel("time")
        plt.legend(loc='upper left')
        plt.show()

    def plot_bf_poly(self, brute_force_show=False):
        """
        Plots the graph of time versus n*logn +m for Dijkstra
        :param brute_force_show: if True, then the time versus n*logn +m for brute force will be in the same plot
        :return:
        """
        nodes, edges, y = zip(*self._bf_data)
        x = [n*m for n, m in zip(nodes, edges)]

        if brute_force_show:
            nodes, edges, y2 = zip(*self._brute_data)
            x2 = [n*m for n, m in zip(nodes, edges)]
            plt.plot(x2, y2, 'bs', label='Brute Force')
        plt.plot(x, y, 'go', label='Bellman-Ford')
        plt.title('Bellman-Ford Performance')
        plt.xlabel("nm")
        plt.ylabel("time")
        plt.legend(loc='upper left')
        plt.show()


test = PerformanceTest(100)
test.plot_bf_poly(brute_force_show=True)
