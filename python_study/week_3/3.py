from collections import deque

def dfs(graph, node, visited):
	visited[node] = True
	print(node, end = " ")

	for i in graph[node]:
		if visited[i] == False:
			dfs(graph, i, visited)


def bfs(graph, node, visited):
	queue = deque([node])
	visited[node] = True

	while queue:
		v = queue.popleft()
		print(v, end = " ")

		for i in graph[v]:
			if visited[i] == False:
				queue.append(i)
				visited[i] = True


graph = [
	[],
	[2, 3, 8], # 1번 노드와 인접한 노드
	[1, 7], # 2번 노드와 인접한 노드
	[1, 4, 5], # 3번 노드와 인접한 노드
	[3, 5], # 4번 노드와 인접한 노드
	[3, 4], # 5번 노드와 인접한 노드
	[7], # 6번 노드와 인접한 노드
	[2, 6, 8], # 7번 노드와 인접한 노드
	[1, 7] # 8번 노드와 인접한 노드
]

visited = [False] * 9

dfs(graph, 1, visited)
bfs(graph, 1, visited)
