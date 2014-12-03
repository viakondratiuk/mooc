# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, name):
        self.name = str(name)
        
    def getName(self):
        return self.name
        
    def __str__(self):
        return self.name
        
class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        
    def getSource(self):
        return self.src
        
    def getDestination(self):
        return self.dest
        
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)
        
class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        Edge.__init__(src, dest)
        self.weight = weight
        
    def getWeight(self):
        return self.weight
        
    def __str__(self):
        return str(self.src) + '->(' + str(self.weight) + ')' + str(self.dest)
        
class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
        
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        self.nodes.add(node)
        self.edges[node] = []
        
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
        
    def childrenOf(self, node):
        return self.edges[node]
        
    def hasNode(self, node):
        return node in self.nodes
        
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1] 
    
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
        
def testSP():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    
    return (g, nodes)
    
def printPath(path):
    res = ''
    for node in path:
        res += node.getName() + '->'
    return res[:-2]
    
def DFS(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            newPath = DFS(graph, node, end, path)
            if newPath != None:
                return newPath
    return None

g, nodes = testSP()
sp = DFS(g, nodes[0], nodes[5])
print 'Shortest path found by DFS:', printPath(sp)