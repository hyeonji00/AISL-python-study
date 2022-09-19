import sys

class Stack():
	def __init__(self):
		self.stack = []
	
	def push(self, X):
		self.stack.append(X)
	
	def pop(self):
		if len(self.stack) == 0:
			print(-1)
		else:
			print(self.stack.pop())

	def size(self):
		print(len(self.stack))

	def empty(self):
		if len(self.stack) == 0:
			print(1)
		else:
			print(0)

	def top(self):
		if len(self.stack) == 0:
			print(-1)
		else:
			print(self.stack[-1])


N = int(input("명령의 수 : "))

stack = Stack()

for i in range(N):
	X = sys.stdin.readline().split()

	if X[0] == "push":
		stack.push(X[1])
	elif X[0] == "pop":
		stack.pop()
	elif X[0] == "size":
		stack.size()
	elif X[0] == "empty":
		stack.empty()
	elif X[0] == "top":
		stack.top()
