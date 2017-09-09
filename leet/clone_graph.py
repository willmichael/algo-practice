# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
sys.setrecursionlimit(2000)

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None
        elif not node.neighbors:
            return UndirectedGraphNode(node.label)
        else:
            new_node = UndirectedGraphNode(node.label)
            for nb in node.neighbors:
                new_node.neighbors.append(self.cloneGraph(nb))
            return new_node

        
