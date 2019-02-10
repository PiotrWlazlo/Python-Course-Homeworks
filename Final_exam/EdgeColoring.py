from Edges import *
from Factory import *
from Graphs import *

class EdgeColor:
    
    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict()
        self.m = 0   # graph.e() is slow
        for edge in self.graph.iteredges():
            if edge.source == edge.target: 
                raise ValueError("a loop detected")
            else:
                self.color[(edge.source, edge.target)] = None   # edge.source < edge.target
                self.m += 1
        if len(self.color) < self.m:
            raise ValueError("edges are not unique")

    def run_complete(self):
        if self.graph.v()%2 != 0:
            self.complete_odd()
        else:
            self.complete_even()

    def complete_odd(self):
        length = len(list(self.graph.iternodes()))
        peripheral_edges = []
        for i in range(length):  #
            edge = (i, (i + 1) % length)
            if edge in self.color.keys():
                self.color[edge] = i
                peripheral_edges.append(edge)
            else:
                self.color[(edge[1], edge[0])] = i
                peripheral_edges.append((edge[1], edge[0]))
        for edge in peripheral_edges:
            node1 = edge[0]
            node2 = edge[1]
            for i in range(math.floor(self.graph.v()/2)):
                if node1 == 0: node1 = self.graph.v()-1
                else: node1 -= 1
                if node2 == self.graph.v()-1: node2 = 0
                else: node2 += 1
                if node1<node2:
                    self.color[(node1, node2)] = self.color[edge]
                elif node1>node2:
                    self.color[(node2, node1)] = self.color[edge]
                else:
                    continue
    
    def complete_even(self):
        edges = self.graph.del_node(self.graph.v()-1)
        self.complete_odd()
        self.graph.add_node(self.graph.v())
        for e in edges:
            self.graph.add_edge(e)
        colors = set(self.color.values())
        colors.remove(None)
        for i in range(self.graph.v()-1):
            s = set()
            for j in range(self.graph.v()-1):
                if i==j:
                    continue
                elif i>j:
                    s.add(self.color[(j,i)])
                else:
                    s.add(self.color[(i,j)])
            self.color[(i,self.graph.v()-1)] = (colors-s).pop()
    
        

