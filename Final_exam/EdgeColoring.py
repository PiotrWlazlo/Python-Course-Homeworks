from Edge import *
from GraphFactory import *
from Graph import *
import math


class EdgeColor:

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict()
        self.m = 0  # graph.e() is slow
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
            else:
                self.color[(edge.source, edge.target)] = None  # edge.source < edge.target
                self.m += 1
        if len(self.color) < self.m:
            raise ValueError("edges are not unique")

    def run(self):
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
        print(peripheral_edges)
        for edge in peripheral_edges:
            node1 = edge[0]
            #print('Wierchołek startowy:',node1)
            node2 = edge[1]
            #print('Wierchołek koncowy:', node2)
            for i in range(math.floor(self.graph.v()/2)):
                #print('petla nr:',i)
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


if __name__ == '__main__':
    N = 15
    G = GraphFactory(Graph)
    g1 = G.make_complete(N, directed=False)
    g1.save("graf.txt")
    c1 = EdgeColor(g1)
    c1.run()
    print(c1.color)
