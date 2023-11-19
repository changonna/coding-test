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
        if root is None:
            return max_depth
        q = deque()
        q.appendleft((root, 1))

        while q:
            cur_node, cur_depth = q.popleft()
            max_depth = max(cur_depth, max_depth)
            # visited.append(cur_node)
            if cur_node.left:
                q.appendleft((cur_node.left, cur_depth+1))
            if cur_node.right:
                q.appendleft((cur_node.right, cur_depth+1))
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