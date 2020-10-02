from collections import defaultdict

class Graph: 
  def __init__(self):
        self.graph = defaultdict(list)
  def insertedge(self,a,b):
    #adjmatrix = [[None for i in range(0,n)] for i in range(0,n)]
    a = int(a)
    b = int(b)
    self.graph[a].append(b)
    #print(adjmatrix)
    #a,b = input().split()
    #print(a,b)
    #adjmatrix[a-1][b-1] = 1
  
  def printgraph(self):
    print(self.graph)
  
  def dfsshow(self,v):
    visited = [False]*(max(self.graph.values())[0]+1)
    #print(len(self.graph),max(self.graph.values()))
    self.visit(v,visited)
    
  def visit(self,v,visited):
    visited[v] = True
    print(v,"->",end = " ")
    for i in self.graph[v]:
      if visited[i] == False:
        self.visit(i,visited)
        
  def fullsearch(self):
    startnode = min(self.graph)
    v = startnode
    visited = [False]*(max(self.graph.values())[0]+1)
    #print(len(self.graph),max(self.graph.values()))
    self.visit(v,visited)
    v = startnode + 1
    print("BREAK ->",end = " ")
    while(visited[v] == False):
      self.visit(v,visited)
    #print(visited)
  
        
new = Graph()
new.insertedge(0,1)
new.insertedge(0,2)
new.insertedge(1,2)
new.insertedge(3,3)
new.insertedge(2,0)
new.insertedge(2,3)
new.fullsearch()
new.dfsshow(2)