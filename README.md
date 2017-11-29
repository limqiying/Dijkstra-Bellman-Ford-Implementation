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
