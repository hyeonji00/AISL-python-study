N, K = map(int, input().split())

pixel = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
	pixel[i] = input().split()

for i in range(N * K):
	x = i // K
	for j in range(N * K):
		y = j // K
		print(pixel[x][y], end = " ")
	print()