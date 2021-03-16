# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        self.res = 0
        def dfs(root,res):
            res += str(root.val)
            
            if (not root.left) and (not root.right):
                self.res += int(res,2)
            
            if root.left:
                dfs(root.left,res)
            if root.right:
                dfs(root.right,res)
        dfs(root,'')
        return self.res