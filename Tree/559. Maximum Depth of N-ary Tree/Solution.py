"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        self.dep = 0
        
        def dfs(root, dep):
            dep += 1
            if not root.children:
                self.dep = max(self.dep, dep)
            if root.children:
                for child in root.children:
                    dfs(child,dep)
        dfs(root,0)
        return self.dep