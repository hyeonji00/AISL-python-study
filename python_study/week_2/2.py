def hanoi(N, start, by, dest):
	if N == 1:
		print(start, dest)
	else:
		hanoi(N - 1, start, dest, by)
		print(start, dest)
		hanoi(N - 1, by, start, dest)


N = int(input())

print(2 ** N - 1)
hanoi(N, 1, 2, 3)

