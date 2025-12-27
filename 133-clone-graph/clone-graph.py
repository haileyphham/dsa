"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #so basically we want to traverse the graph and create a clone of the graph
        if not node:
            return None 

        old_to_new = {} #creating a dictionary to store the copies
        
        def dfs(curr): #here, we input our current node, output its copy.
            if curr in old_to_new: # if we saw this node already,
                return old_to_new[curr] #we 
            copy = Node(curr.val) #copying the node if we havent seen it alr
            old_to_new[curr] = copy #map the cloned value in the dictionary

            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)



        


        