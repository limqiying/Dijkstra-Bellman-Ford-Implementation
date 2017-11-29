"""
Script used to get and plot performance data for both algorithms
requires matplotlib as dependency
"""
from non_neg_test import *
from neg_test import *
from math import log
import matplotlib.pyplot as plt


class PerformanceTest:

    def __init__(self, num_data=1000):
        self._test = NonNegativeTest(num_data)
        self._test = NegativeTest(num_data)
        self._brute_data, self._d_data = self._test.get_performance_data()

    def get_dij_data(self):
        return self._d_data

    def plot_dijk_log(self, brute_force_show=False):
        """
        Plots the graph of time versus n*logn +m for Dijkstra
        :param brute_force_show: if True, then the time versus n*logn +m for brute force will be in the same plot
        :return:
        """
        nodes, edges, y = zip(*self._d_data)
        x = [(n * log(n, 2) + m) for n, m in zip(nodes, edges)]

        if brute_force_show:
            nodes, edges, y2 = zip(*self._d_data)
            x2 = [(n * log(n, 2) + m) for n, m in zip(nodes, edges)]
            plt.plot(x2, y2, 'bs', label='Brute Force')

        plt.plot(x, y, 'ro', label='Dijkstra')

        plt.xlabel("nlogn + m")
        plt.ylabel("time")
        plt.legend(loc='upper left')
        plt.show()


test = PerformanceTest(100)
test.plot_dijk_log(brute_force_show=True)