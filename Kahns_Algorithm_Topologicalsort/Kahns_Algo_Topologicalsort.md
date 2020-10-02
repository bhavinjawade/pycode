# Kahn’s Topological Sort Algorithm

Topological Sorting is mainly used for scheduling jobs from the given dependencies among jobs. In computer science, applications of this type arise in instruction scheduling, ordering of formula cell evaluation when recomputing formula values in spreadsheets, logic synthesis, determining the order of compilation tasks to perform in makefiles, data serialization, and resolving symbol dependencies in linkers.

## Topological Sorting:

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for
every directed edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph
is not possible if the graph is not a DAG.
<br>
<br>

**For example**, a topological sorting of the following graph is ͞5 4 2 3 1 0͟. There can be more
than one topological sorting for a graph. For example, another topological sorting of the
following graph is ͞4 5 2 3 1 0͟. The first vertex in topological sorting is always a vertex with indegree
as 0 (a vertex with no incoming edges).
<br>
The canonical application of topological sorting is in scheduling a sequence of jobs or tasks
based on their dependencies. The jobs are represented by vertices, and there is an edge
from x to y if job x must be completed before job y can be started (for example, when washing
clothes, the washing machine must finish before we put the clothes in the dryer). Then, a
topological sort gives an order in which to perform the jobs.

<br>

![alt text](https://www.geeksforgeeks.org/wp-content/uploads/graph.png "Graph")

The usual algorithms for topological sorting have running time linear in the number of nodes
plus the number of edges, asymptotically O(|V|+|E|) 

### Kahn’s Algorithm:
One of these algorithms, first described by Kahn (1962), works by choosing vertices in the same
order as the eventual topological sort. First, find a list of "start nodes" which have no incoming
edges and insert them into a list Store; at least one such node must exist in a non-empty acyclic
graph. Then:
<br>

```python
Indegree <- list containing in-degree of each vertex
Store <- list containing vertices having 0 in-degree
Topsort <- empty list that will contain the sorted elements
while store is non empty do :
 remove a vertex from store
 add it to topsort
 for each vertex m with an edge from n to m do:
 remove edge e from the graph
 if indegree of m is 0:
 insert m into store
if graph has edges then
 return error (graph has atleast one cycle)
else
 return topsort
```

If the graph is a DAG, a solution will be contained in the list topsort (the solution is not
necessarily unique). Otherwise, the graph must have at least one cycle and therefore a
topological sorting is impossible.
<br>
For the above mentioned graph value of topsort, store and indegree for each iteration:
<br>

| Iteration | Topsort | Store | In-degree |
| --- | --- | --- | --- |
| 0 | -             | [4,5] | [2,2,1,1,0,0] |
| 1 | [4]           | [5]   | [1,1,1,1,0,0] |
| 2 | [4,5]         | [2,0] | [0,1,0,1,0,0] |
| 3 | [4,5,2]       | [0,3] | [0,1,0,0,0,0] |
| 4 | [4,5,2,0]     | [3]   | [0,1,0,0,0,0] |
| 5 | [4,5,2,0,3]   | [1]   | [0,0,0,0,0,0] |
| 6 | [4,5,2,0,3,1] | []    | [0,0,0,0,0,0] |

<br>

**Markdown by: [Sakina Freegnajwala](https://www.linkedin.com/in/sakina-freeganjwala-033498152/)**