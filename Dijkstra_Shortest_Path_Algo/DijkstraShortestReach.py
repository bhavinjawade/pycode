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
    if(self.graph[a-1][b-1] != 0):
        temp = self.graph[a-1][b-1]
        if(temp > dist):
            self.graph[a-1][b-1] = dist
    else:
        self.graph[a-1][b-1] = dist
    if(self.graph[b-1][a-1] != 0):
        temp = self.graph[b-1][a-1]
        if(temp > dist):
            self.graph[b-1][a-1] = dist
    else:
        self.graph[b-1][a-1] = dist
    #self.printgraph()
  
  def printgraph(self):
    print(self.graph)
  
  def printshortestgraph(self, dist,src):
        f = open('somefile.txt', 'a')
        #print("Vertex tDistance from Source")
        for node in range(self.vert):
          if(node == src):
            continue
          if(node == self.vert - 1):
            if(dist[node] != sys.maxsize):
                print(dist[node],file = f)
            else:
                print(-1,file = f)
          elif(dist[node] != sys.maxsize):
            #print("From 0 to ", node ," - >",dist[node],end = " ")
            #print(self.pathlist[node])
            print(dist[node],end = ' ',file = f)
            #f.write(dist[node] + " ")
          elif(dist[node] == sys.maxsize):
            #print("From 0 to ", node ," - >",-1,end = " ")
            print(-1,end = ' ',file = f)
            #f.write(-1 + " ")
        #print('\n')
        #f.write("\n")
  
  def findmindist(self,dist,sptSet):
        #print(dist)
        minval = sys.maxsize
        #print(minval)
        #min_index = 225
        for v in range(self.vert):
            if dist[v] <= minval and sptSet[v] == False:
                minval = dist[v]
                min_index = v
                #print("assign",v)
        return min_index
  
  def dijkstra(self, src):
        dist = [sys.maxsize] * self.vert
        src = src - 1
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
        self.printshortestgraph(dist,src)

t = int(input().strip())
for a0 in range(t):
    n,m = input().strip().split(' ')
    n,m = [int(n),int(m)]
    gr = Graph(n)
    for a1 in range(m):
        x,y,r = input().strip().split(' ')
        x,y,r = [int(x),int(y),int(r)]
        gr.insertedge(x,y,r)
    s = int(input().strip())
    gr.dijkstra(s)
