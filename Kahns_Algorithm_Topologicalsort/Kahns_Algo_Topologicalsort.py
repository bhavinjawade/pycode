from collections import defaultdict

class Graph: 
  def __init__(self,size):
        self.graph = defaultdict(list)
        self.vert = size
  def insertedge(self,a,b):
    #adjmatrix = [[None for i in range(0,n)] for i in range(0,n)]
    a = int(a)
    b = int(b)
    self.graph[b].append(a)
    #print(adjmatrix)
    #a,b = input().split()
    #print(a,b)
    #adjmatrix[a-1][b-1] = 1
  
  def printgraph(self):
    print(self.graph)

  def Toposort(self):
    indegree = [0]*self.vert
    for i in self.graph:
      for j in self.graph[i]:
        indegree[j] += 1
    store = []
    for i in range(self.vert):
      if indegree[i] == 0:
        store.append(i)
    visit = 0
    topsort = []
    while store:
      u = store.pop(0)
      topsort.append(u)
      for j in self.graph[u]:
        indegree[j] -= 1
        if(indegree[j] == 0):
          store.append(j)
      visit += 1
    if(visit != self.vert):
      print("Cycle Detected")
    else:
      print(topsort[::-1])
    
new = Graph(6)
new.insertedge(0,1)
new.insertedge(1,2)
new.insertedge(1,3)
new.insertedge(2,3)
new.insertedge(3,4)
new.insertedge(4,5)
new.printgraph()
new.Toposort()