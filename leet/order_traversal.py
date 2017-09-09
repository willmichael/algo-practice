# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, heads = []
        while True:
            while root:
                heads.append(root)
                root = root.left
            if not heads:
                return res
            end = heads.pop()
            if end:
                res.append(heads.pop())
                root = root.right
                
                

            
