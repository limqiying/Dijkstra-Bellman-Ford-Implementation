"""
Script used to get and plot performance data for both algorithms
requires matplotlib as dependency
"""
from non_neg_test import *
from math import log
import matplotlib.pyplot as plt


class PerformanceTest:

    def __init__(self, num_data=1000):
        self._test = NonNegativeTest(num_data)
        self._brute_data, self._d_data = self._test.get_performance_data()

    def get_dij_data(self):
        return self._d_data

    def plot_dijk_log(self):
        nodes, edges, y = zip(*self._d_data)
        x = [(n*log(n, 2)+m) for n, m in zip(nodes,edges)]

        plt.plot(x, y, 'ro')


test = PerformanceTest(10)
test.plot_dijk_log()
plt.show()