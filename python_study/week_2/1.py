N, K = map(int, input().split())

pixel = []

for i in range(N):
	pixel.append([])
	pixel[i] = input().split()

for i in range(N * K):
	x = i // K
	for j in range(N * K):
		y = j // K
		print(pixel[x][y], end = " ")
	print()
