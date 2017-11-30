# Analysis of Dijkstra & Bellman-Ford
Part 1 of Final Project for CSCI3383 (Algorithms) at Boston College:
* Instructor: Lewis Tseng
* Semester: Fall 
* Team Members: Tia Lim, Jiacheng Xu

## Introduction
Given any graph and some vertex, the Dijkstra's algorithm and the Bellman-Ford algorithm are used to determine, the shortest distances from s to all other nodes in G. While Dijkstra's algorithm has better time-complexity, it does not work when G contains negative edge-weights. Bellman-Ford has a higher time-complexity but is tolerant to negative edge-weights.

In this project, we implement and study the performance of both algorithms. Our code allows us to easily create graphs and run both shortest path algorithms on it, to obtain the shortest distances as well as the shortest paths from any given vertex to the start vertex.

## Usage
A guide on how to use our code
### Graph

Say we want to create a graph `g`, with starting node `0`, specified by the edges:

```python
0 -> 2 cost = 1
0 -> 3 cost = 3
3 -> 1 cost = 7
```
We first create an empty graph initialized with starting node `0`:
```python
g = ShortestPathGraph(0)
```
which will automatically add `0` to the node set of `g`. Next, we add our other nodes simply by passing them as a list:
```python
g.set_nodes([0,1,2,3])
```
Notice that we added the node `0` twice. This is fine, and repeat nodes will not be added to the graph.
Next, we added the edges by passing an edge list, containing `(vertex_1, vertex_2, cost)` tuples. 
```python
graph.set_edges([(0, 2, 1), (0, 3, 3), (3, 1, 7)])
```
This completes the whole specification of our graph. 

### Dijkstra's Algorithm
If we want to find the shortest from our starting node `0` to node `3`, for example, we call 
```python
graph.dijkstra_get_dist(3)
graph.dijkstra_get_dist(3, numerical=True)
```
The first call will output a sentence, stating the start node and our specifying node, as well as the computed shortest distance. This is used for easier visualization.
The second call will output only the integer representing the shortest distance. This is used for our testing later.

If we want to obtain the shortest path from `0` to `3`, we can call
```python
graph.dijkstra_get_path(3)
```
which will return a list representing the path from `0` to `3`. Finally, calling 
```python
graph.dijkstra_get_tree()
```
We will obtain the entire edge set as a list of tuples specifying the shortest path tree as computed by Dijkstra's Algorithm.

### BellmanFord's Algorithm
BellmanFord Algorithm is designed to solve the negative edges issue. In addition, when there are negative cycles in the graph, BellmanFord Algorithm going to detect one of them and output negative cycle. The actual implementation function of the pseudo-code we covered in class is in file graph.py and the function name is: 
```python
graph._bellmanford()
```
This is a private function which return n+1 (n is number of nodes in graph) when there is a path between source node and given node, and return the first node it detect that within one negative cycle when there is negative cycle. In order to use this function, you can use following funtions:
```python
graph.bellmanfor_get_dist(3)
```
For example, function above return shortest distance from node 3 to source node.
```python
graph.bellman_get_path(3)
```
Function above return the shortes path from source node to node 3

```python
graph.bellman_get_tree(3)
```
We will obtain the entire edge set as a list of tuples specifying the shortest path tree as computed by BellmanFord's Algorithm.

Caveats for BellmanFord's Algorithm: When there is a negative cycle in the graph, the brutal force will still output some distance while the BellmanFord output one node that contained in one negative cycle. So far the best way to check which one is correct is to print the graph and see the cycle around that node. 

# Testing

Since we have two types of graphs -- one with negative edges, and one without negative edges we needed to conduct two types of tests, `NonNegativeTest` and the `NegativeTest`.

To test the correctness, the test first computes the shortest path in each of these graphs with the brute force method.
It then checks that the result computed by our implementation of our shortest path algorithms is equal to the brute-force result for each graph generated.

For `NegativeTest`, we have to test additionally if our Bellman-Ford algorithm correctly detects a negative cycle. We do this by verifying that the path it outputs indeed contains a negative cycle.

# Performance

We also implemented a way to easily visualize the performance of the different algorithms bench-marked against the runtime of the brute-force method. We discuss our analysis of our findings in the written report.
`PerformanceTest` object contains 1000 randomly generated graphs, which we can implement 3 different types of tests with. Say that we initialized a `PerformanceTest` object

```python
pf = PerformanceTest()
```

To see the run-time of our Dijkstra's algorithm on the 1000 randomly generated graphs,
```python
pf.plot_dijk_log()
pf.plot_dijk_log(brute_force_show=True)
```
will create a plot of nlogn + m against t, where n is the number of nodes, m the number of edges, and t the run-time of Dijkstra. Setting `brute_force_show=True` will plot the Dijkstra times against the brute force times.
Since in theory, Dijkstra should be O(nlogn + m), we should expect a mainly linear plot. Here is an example of such a plot we obtained:
![Dij_perf](https://github.com/limqiying/Dijkstra-Bellman-Ford-Implementation/blob/master/plots/dijkstra_performance.png)

The implementation is similar for Bellman-Ford performance testing,
```python
pf.plot_bf_poly()
pf.plot_bf_poly(brute_force_show=True)
```
will plot n*m against t. Bellman-Ford's algorithm has the theoretical time complexity of O(nm), so we too expect a linear plot. This is a plot we obtained:
![BF_perf](https://github.com/limqiying/Dijkstra-Bellman-Ford-Implementation/blob/master/plots/bellman-ford%20performance.png)

`PerformanceTest` also allows us to see how brute-force, Dijkstra and Bellman-Ford performs on graphs with a fixed n and m. Calling

```python
pf.plot_compare_pos(n, m)
```
Will show the scatter plots of times for 100 randomly generated graphs with n nodes and m edges, for the 3 shortest-path algorithms. Here is an example of something we obtained:
![Compare](https://github.com/limqiying/Dijkstra-Bellman-Ford-Implementation/blob/master/plots/10_10.png)