# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.result = None
        self.result_p = None
        def inorder(root):
            if root:
                inorder(root.left)
                if self.result_p != None:
                    self.result_p.right = TreeNode(root.val)
                    self.result_p = self.result_p.right
                else:
                    self.result = TreeNode(root.val)
                    self.result_p = self.result
                inorder(root.right)
                
        inorder(root)
        return self.result
    
        
        