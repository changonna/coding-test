def preorder(root):
	if root is None:
		return
	print(root) # 1
	preorder(root.left)
	preorder(root.right)