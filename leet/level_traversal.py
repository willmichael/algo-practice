# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        level = [root]

        while root and level:
            res.append([r.val for r in level])
            leftright = [(r.left, r.right) for r in level]
            level = [leaf for lr in leftright for leaf in lr if leaf]
        return res
        
