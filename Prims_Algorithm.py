from dataclasses import dataclass, field
@dataclass(eq=False)
class Node :
    idnum : int
@dataclass
class Graph :
    source  : int
    adjlist : dict
    def PrimsMST(self):
        priority_queue = { Node(self.source) : 0 }
        added = [False] * len(self.adjlist)
        min_span_tree_cost = 0
        while priority_queue :
            node = min(priority_queue, key=priority_queue.get)
            cost = priority_queue[node]
            del priority_queue[node]
            if added[node.idnum] == False :
                min_span_tree_cost += cost
                added[node.idnum] = True
                print("Node added: " + str(node.idnum) + ",cost: "+str(min_span_tree_cost))
                for item in self.adjlist[node.idnum] :
                    adjnode = item[0]
                    adjcost = item[1]
                    if added[adjnode] == False :
                        priority_queue[Node(adjnode)] = adjcost
        return min_span_tree_cost
def main() :
    g1_edges_from_node = {}
    g1_edges_from_node[0] = [ (1,1), (2,2), (3,1), (4,1), (5,2), (6,1) ]
    g1_edges_from_node[1] = [ (0,1), (2,2), (6,2) ]
    g1_edges_from_node[2] = [ (0,2), (1,2), (3,1) ]
    g1_edges_from_node[3] = [ (0,1), (2,1), (4,2) ]
    g1_edges_from_node[4] = [ (0,1), (3,2), (5,2) ]
    g1_edges_from_node[5] = [ (0,2), (4,2), (6,1) ]
    g1_edges_from_node[6] = [ (0,1), (2,2), (5,1) ]

    g1 = Graph(0, g1_edges_from_node)
    cost = g1.PrimsMST()
    print("Cost of the minimum spanning tree in graph 1 : " + str(cost) +"\n")
    g2_edges_from_node = {}
    g2_edges_from_node[0] = [ (1,4), (2,1), (3,5) ];
    g2_edges_from_node[1] = [ (0,4), (3,2), (4,3), (5,3) ];
    g2_edges_from_node[2] = [ (0,1), (3,2), (4,8) ];
    g2_edges_from_node[3] = [ (0,5), (1,2), (2,2), (4,1) ];
    g2_edges_from_node[4] = [ (1,3), (2,8), (3,1), (5,3) ];
    g2_edges_from_node[5] = [ (1,3), (4,3) ];
    g2 = Graph(0, g2_edges_from_node)
    cost = g2.PrimsMST()
    print("Cost of the minimum spanning tree in graph 1 : " + str(cost))
if __name__ == "__main__" :
    main()