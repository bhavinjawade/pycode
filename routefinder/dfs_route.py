# Provide the graph in the form of list:
#    The cost of moving from i to j is cost[i][j]
#    Cost of moving from anoy row to the first row is 0
#    If there is not path between the 2 nodes the the cost of moving from one node to the other is -1

# There can be only one starting point
# You can provide with multiple ending points. The algorithm chooses the best destination and provides with the path.

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


def dfs(visited, graph, node, goals, list):
    if node not in visited:
        list.append(node)
        visited.add(node)
        if node in goals:
            exit
        else:
            for n in graph[node]:
                dfs(visited, graph, n, goals, list)


def DFS_Traversal(cost, start_point, goals):
    if start_point in goals:
        l = [start_point]
        return l
    l = []
    a = []
    dict1 = {}
    for i in range(0, len(cost)):
        dict1[i] = []
        for j in range(0, len(cost)):
            if (cost[i][j] > 0):
                dict1[i].append(j)
    visited = set()
    dfs(visited, dict1, start_point, goals, a)
    flag = 1
    l2 = []
    for var in a:
        if flag:
            l2.append(var)
            if var in goals:
                flag = 0
    h = len(l2)
    i = 0
    while i < h-1:
        if cost[l2[i]][l2[i+1]] > 0:
            l.append(l2[i])
        else:
            l.append(l2[i])
            while cost[l[-1]][l2[i+1]] <= 0:
                l.pop()
        i += 1
    l.append(l2[h-1])
    return l


if __name__ == '__main__':
    # DFS_Traversal(cost, start_point, goals)
    route = DFS_Traversal(cost, 1, [6, 7, 10])
    print(route)
