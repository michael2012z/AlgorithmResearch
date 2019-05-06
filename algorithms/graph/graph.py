from algorithms.basic.queue import Queue

class Vertex:
    
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.distance = 0
        self.color = ''

    def addNeighbor(self, nbr, weight=1):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def setDistance(self, d):
        self.distance = d

    def getDistance(self):
        return self.distance

    def setColor(self, c):
        self.color = c

    def getColor(self):
        return self.color


class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0


    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, v):
        if v in self.vertList:
            return self.vertList[v]
        else:
            return None

    def __contains__(self, v):
        return v in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def bfs(self, start):
        start.setDistance(0)
        vertQueue = Queue()
        vertQueue.enqueue(start)
        while (vertQueue.size() > 0):
            currentVert = vertQueue.dequeue()
            for nbr in currentVert.getConnections():
                if (nbr.getColor() == 'white'):
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance() + currentVert.getWeight(nbr))
                    vertQueue.enqueue(nbr)
            currentVert.setColor('black')
            print(currentVert.getId())

def test1():
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    for v in g:
        for w in v.getConnections():
            print("( %s , %s , %d)" % (v.getId(), w.getId(), v.getWeight(w)))

def test2():
    g = Graph()
    g.addVertex("fool")
    g.addVertex("pool")
    g.addVertex("foil")
    g.addVertex("foul")
    g.addVertex("cool")
    g.addVertex("poll")
    g.addVertex("fail")
    g.addVertex("pole")
    g.addVertex("pall")
    g.addVertex("pope")
    g.addEdge("fool", "pool")
    g.addEdge("fool", "foil")
    g.addEdge("fool", "foul")
    g.addEdge("fool", "cool")
    g.addEdge("pool", "poll")
    g.addEdge("foil", "fail")
    g.addEdge("poll", "pole")
    g.addEdge("poll", "pall")
    g.addEdge("pole", "pope")
    g.bfs(g.getVertex("fool"))
    pass
    
if __name__ == '__main__':
    test2()
