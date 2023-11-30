def inorder(root):
	if root is None:
		return
	inorder(root.left)
	print(root) # 2
	inorder(root.right)