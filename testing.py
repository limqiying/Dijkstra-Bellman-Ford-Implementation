"""
Script to run tests for correctess on shortest path implementation
"""
from non_neg_test import *
from neg_test import *


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


if __name__ == "__main__":
    main()
