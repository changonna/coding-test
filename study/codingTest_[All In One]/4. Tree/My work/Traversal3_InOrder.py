# bfs(Breadth-First Search) : 너비 우선 탐색

from collections import deque

def bfs(root):
  # 초기 설정
  visited = []
  if root is None:
    return []
  q = deque()
  q.append(root)

  while q:
    # q에 값 빼서  visited에 추가
    cur_node = q.popleft
    visited.append(cur_node)
    
    # 현재 노드에 left, right 값 q에 저장
    if cur_node.left:
      q.append(cur_node.left)
    if cur_node.right:
      q.append(cur_node.right)

  return visited

# bfs(root)