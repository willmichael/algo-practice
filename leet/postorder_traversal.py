# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans, heads, visited = [], [], []
        while True:
            while root and root not in visited:
                heads.append(root)
                root = root.left
            if not heads:
                return ans
            end = heads[-1]
            if end.right and end not in visited:
                root = end.right
                visited.append(end)
            else:
                heads.pop()
                ans.append(end.val)
        return ans
            



x = TreeNode(1)
x.right = TreeNode(2)

s = Solution()
print s.postorderTraversal(x)
