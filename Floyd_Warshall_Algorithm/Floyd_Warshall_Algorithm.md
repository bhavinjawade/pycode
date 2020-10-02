# Floyd Warshall Algorithm

The Floyd-Warshall algorithm is a shortest path algorithm for graphs. Like the Bellman-Ford algorithm or the Dijkstra's algorithm, it computes the shortest path in a graph. However, Bellman-Ford and Dijkstra are both single-source, shortest-path algorithms. This means they only compute the shortest path from a single source. Floyd-Warshall, on the other hand, computes the shortest distances between every pair of vertices in the input graph.

<br>

### Algorithm -

<br>

```Python
Floyd_Warshall(int n, int W[1..n, 1..n]) {
array d[1..n, 1..n]
for i = 1 to n do { // initialize
for j = 1 to n do {
d[i,j] = W[i,j]
pred[i,j] = null
}
}
for k = 1 to n do // use intermediates {1..k}
for i = 1 to n do // ...from i
for j = 1 to n do // ...to j
if (d[i,k] + d[k,j]) < d[i,j]) {
d[i,j] = d[i,k] + d[k,j] // new shorter path length
pred[i,j] = k // new path is through k
			
```
<br>
Clearly the algorithm’s running time is Θ(n3). The space used by the algorithm is Θ(n2). Observe
that we deleted all references to the superscript (k) in the code. It is left as an exercise that this does
not affect the correctness of the algorithm. 

<br>

## Applications of Floyd Warshall Algorithm

The Floyd–Warshall algorithm can be used to solve the following problems, among others:
<br>
* Shortest paths in directed graphs (Floyd’s algorithm).
* Transitive closure of directed graphs (Warshall’s algorithm). In Warshall’s original formulation of the algorithm, the graph is unweighted and represented by a Boolean adjacency matrix. Then the addition operation is replaced by logical conjunction (AND) and the minimum operation by logical disjunction (OR).
* Finding a regular expression denoting the regular language accepted by a finite automaton (Kleene’s algorithm)
* Inversion of real matrices (Gauss–Jordan algorithm).
* Optimal routing. In this application one is interested in finding the path with the maximum flow between two vertices. This means that, rather than taking minima as in the pseudocode above, one instead takes maxima. The edge weights represent fixed constraints on flow. Path weights represent bottlenecks; so the addition operation above is replaced by the minimum operation.
* Testing whether an undirected graph is bipartite.
* Fast computation of Pathfinder networks.
* Maximum Bandwidth Paths in Flow Networks