# Provide the graph in the form of list:
#    The cost of moving from i to j is cost[i][j]
#    Cost of moving from anoy row to the first row is 0
#    If there is not path between the 2 nodes the the cost of moving from one node to the other is -1

#    Provide the heuristic value for each node i in heuristic[i]

# There can be only one starting point
# You can provide with multiple ending points. The algorithm chooses the best destination and provides with the path.

from copy import deepcopy
from queue import PriorityQueue

cost = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 9, -1, 6, -1, -1, -1, -1, -1],
        [0, -1, 0, 3, -1, -1, 9, -1, -1, -1, -1],
        [0, -1, 2, 0, 1, -1, -1, -1, -1, -1, -1],
        [0, 6, -1, -1, 0, -1, -1, 5, 7, -1, -1],
        [0, -1, -1, -1, 2, 0, -1, -1, -1, 2, -1],
        [0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1],
        [0, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1],
        [0, -1, -1, -1, -1, 2, -1, -1, 0, -1, 8],
        [0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 7],
        [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]]

heuristic = [0, 5, 7, 3, 4, 6, 0, 0, 6, 5, 0]


def A_star_util(s, visited, path, goals, value, heuristic, graph, path_dict, cost_dict):
    path.append(s)
    visited.add(s)
    if s in goals:
        path_dict.update({tuple(path): value})
        return
    for i in graph[s].queue:
        if i not in visited:
            vis_copy = visited.copy()
            A_star_util(i, vis_copy, deepcopy(path), goals, value +
                        cost_dict[s, i], heuristic, graph, path_dict, cost_dict)


def A_star_Traversal(cost, heuristic, start_point, goals):
    if start_point in goals:
        l = [start_point]
        return l
    l = []
    graph = dict()
    cost_dict = dict()
    path_dict = dict()
    visited = set()
    visited.add(start_point)
    path = [start_point]
    for i in range(len(cost)):
        q = PriorityQueue()
        graph[i] = q
        for j in range(len(cost[i])):
            if cost[i][j] > 0:
                graph[i].put(j)
                cost_dict.update(
                    {(i, j): cost[i][j] + heuristic[j] - heuristic[i]})
    for i in graph[start_point].queue:
        if i not in visited:
            value = cost_dict[start_point, i]
            vis_copy = visited.copy()
            A_star_util(i, vis_copy, deepcopy(path), goals, value,
                        heuristic, graph, path_dict, cost_dict)
    l = []
    if path_dict:
        l = min(path_dict, key=path_dict.get)
        l = [x for x in l]
    return l


if __name__ == '__main__':
    # A_star_Traversal(cost, heuristic, start_point, goals)
    route = A_star_Traversal(cost, heuristic, 1, [6, 7, 10])
    print(route)
