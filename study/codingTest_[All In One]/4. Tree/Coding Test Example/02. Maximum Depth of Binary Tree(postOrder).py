from collections import deque
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        max_depth = 0
        leftDepth = 0 
        rightDepth = 0
        # Base case
        if root is None:
            return max_depth

        # 둘 다 없으면
        if root.left is None and root.right is None:
            return 1
        # 1. left
        if root.left:
            leftDepth = self.maxDepth(root.left)
        # 2. right
        if root.right:
            rightDepth = self.maxDepth(root.right)
        # max_depth 구하기
        max_depth = max(leftDepth, rightDepth) + 1
        return max_depth
        
bt = TreeNode(3)
bt.left = TreeNode(5)
bt.right = TreeNode(1)
bt.left.left = TreeNode(6)
bt.left.right = TreeNode(2)
bt.left.right.left = TreeNode(0)
bt.left.right.right = TreeNode(8)
bt.left.right.left = TreeNode(7)
bt.left.right.right = TreeNode(4)

sol = Solution()
answer = sol.maxDepth(bt) # 4
print(answer)