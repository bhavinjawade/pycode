# Disjoint Sets
Disjoint Sets are those sets of elements where no value or element is present in more than one set i.e there are no common elements and no overlapping. This data structure supports three major operations :
1. Find ()
2. Union()
3. make_set()



## Explanation / Working
Union-Find works on sets via trees.Each tree represents a set and root is the representative of set.

-  Initially every element is a single set i.e a tree with only one vertex.
-  An array is created such that every index of the array represents a tree and the value at that index represents its ancestor/parent.
-  For this we use the make_set() function as follows :

```sh
def make_set(vertex):
    
    parent[vertex]=vertex
    
```

#### Find :
The find() function takes a vertext as input and returns the representative of the set that the input vertex belongs to. We simply traverse from the input vertext to its parent and repeat until we fin the representative.

```sh
def find_set(vertex):
    
    if(vertex==parent[vertex]):
        return v
     else
        return find_set(parent[vertex])  #Recursive function
    
```

#### Union Function : 
It takes 2 sets as input and then we find representative of both the inputs.
If they are same,then we do nothing as they are already in the same set.Otherwise,we make the representative of any one tree the parent of the combined set of both trees.

```sh
def union_set(a,b):
    a = find_set(a)
    b = find_set(b)
    if(a! = b):
        parent[b] = a; #COMBINING THE TREES
``` 

## Analysis

Since the union and make set function takes constant time and the find function takes linear time in traversing N elements , the overall complexity becomes O(1) + O(N) = O(N) as we only take the largest term and ignore other terms. However, this can be improved by introducting certain modifications explained below.

## Modifications

1. Path Compression :
        In this method, we simply set the parent of each visited vertex directly to its representative. Code :
  ```sh
def find_set(vertex):
    
    if(vertex==parent[vertex]):
        return v
     else
        return parent[vertex] = find_set(parent[vertex])  
```
2. Union by Rank/Weight:
        Another approach for reducing time complexity is that we sdefine how the combination will take place.We can merge the trees on the basis of greater rank or more weight. This means that the tree with less number of nodes will be merged into the bigger tree.

 ## Analysis after modifications :
 The time complexity after applying both of the modifications is O(Ackermann function(N)) which is approximately a constant. So we can say that complexity is O(1).
 

# Applications

- Kruskal's Algorithm. 
- Finding cycles in a graph.
- Maze Generation 
- Online maintenance of biconnected components
- Lowest Common Ancestor Problem
- Diving an image into sets of different color.
- Efficient Connected component labeling or CCL algorithms use the Union-Find data structure. In real life when photoshop allows you to "grab" different objects in an image and differentiate between an object and "background" in either an assisted or fully automated way they are probably using the connected components technique. CCL is extensively used in image analysis, from automated segmentation of cancer cells to segmentation of persons or objects of interest in surveillance.
