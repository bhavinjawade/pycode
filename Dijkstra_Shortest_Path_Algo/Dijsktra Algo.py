import sys
from collections import defaultdict

class Graph: 
  def __init__(self,n):
        self.vert = n
        #self.graph = defaultdict(list)
        self.graph = [[0 for column in range(n)] 
                      for row in range(n)]
        self.pathlist = defaultdict(list)
  def insertedge(self,a,b,dist):
    a = int(a)
    b = int(b)
    #print("bhavin")
    #self.graph[a].append(b)
    #print(adjmatrix)
    #a,b = input().split()
    #print(a,b)
    self.graph[a][b] = dist
    #self.printgraph()
  
  def printgraph(self):
    print(self.graph)
  
  def printshortestgraph(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.vert):
            print("From 0 to ", node ," - >",dist[node],end = " ")
            print(self.pathlist[node])
  
  def findmindist(self,dist,sptSet):
        #print(dist)
        minval = sys.maxsize
        #print(minval)
        #min_index = 225
        for v in range(self.vert):
            if dist[v] < minval and sptSet[v] == False:
                minval = dist[v]
                min_index = v
                #print("assign",v)
        return min_index
  
  def dijkstra(self, src):
        dist = [sys.maxsize] * self.vert
        dist[src] = 0
        self.pathlist[0].append(src)
        sptSet = [False] * self.vert
        for cout in range(self.vert):
            u = self.findmindist(dist, sptSet)
            #if u == 225 :
            #  break
            sptSet[u] = True
            for v in range(self.vert):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
                        self.pathlist[v] = self.pathlist[u] + [v]
                        #print(dist,"Changing")
        #print("bhavin")
        self.printshortestgraph(dist)
  
new = Graph(6)
new.insertedge(0,1,8)
new.insertedge(0,2,1)
new.insertedge(1,2,2)
new.insertedge(1,3,2)
new.insertedge(2,4,4)
new.insertedge(2,3,3)
new.insertedge(3,4,1)
new.insertedge(3,5,12)
new.insertedge(4,5,7)
new.dijkstra(0)