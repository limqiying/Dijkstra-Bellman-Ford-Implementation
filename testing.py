"""
Script to run tests for correctess on shortest path implementation
"""
from non_neg_test import *
from neg_test import *
from test_util import *


def main():

    print("Generating 100 Graphs with non-negative edge weights. \n")
    non_neg = NonNegativeTest(100)
    non_neg.run_correctness()
    print("Non-Negative test complete. \n")
    print("***********************************\n")
    print("Generating 10 Graphs with negative edge weights. \n")
    non_neg = NegativeTest(10)
    non_neg.run_correctness_dij()
    print("Negative test complete.")

    print("Generating 100 Graphs with negative edge weights. \n")
    neg2 = NegativeTest(100)
    neg2.run_correctness_neg()
    print("Negative test complete. \n")

    # Compare bellmanford and Dikstra
    print("Generating 10 Graphs with negative edge weights to compare jikstra and bellmanford. \n")
    neg3 = NegativeTest(10)
    graph_list = neg3._random_neg_graphs
    for graph in graph_list:
        print(graph.dijkstra_get_dist(4,numerical = True))
        print(graph.bellmanford_get_dist(4))

    print("Comparison between djikstra and bellmanford complete. \n")


if __name__ == "__main__":
    main()
