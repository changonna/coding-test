'''
[ Lowest Common Ancestor of a Binary Tree ]
Binary 트리 하나와 해당 트리에 속한 두 개의 노드가 주어질 때,
두 노드의 공통 조상중 가장 낮은 TreeNode 즉, the lowest common ancestor(LCA)를 찾아라
'''


# Definition for a binary tree TreeNode.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if (root.val == p or root.val == q) or (left and right):
            return root.val
        else:
            return left or right

        

bt = TreeNode(3)
bt.left = TreeNode(5)
bt.right = TreeNode(1)
bt.left.left = TreeNode(6)
bt.left.right = TreeNode(2)
bt.left.right.left = TreeNode(7)
bt.left.right.right = TreeNode(4)
bt.right.left = TreeNode(0)
bt.right.right = TreeNode(8)

sol = Solution()
answer = sol.lowestCommonAncestor(bt, 6, 4) # 5
print(answer)
answer = sol.lowestCommonAncestor(bt, 5, 1) # 3
print(answer)




