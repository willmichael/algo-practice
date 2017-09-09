# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans, heads = [], []
        while True:
            while root:
                ans.append(root.val)
                heads.append(root)
                root = root.left
            if not heads:
                return ans
            end = heads.pop()
            root = end.right
        return ans

