import math

class calculator:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def add(self):
		return self.num1 + self.num2

	def sub(self):
		return self.num1 - self.num2

	def mul(self):
		return self.num1 * self.num2

	def div(self):
		if self.num2 == 0:
				print("0으로 나눌 수 없습니다.")
		else:
			return self.num1 / self.num2

class improved_calculator(calculator):	
	def power(self):
		return math.pow(self, self.num1, self.num2)

	def gcd(self):
		return math.gcd(self, self.num1, self.num2)

def main():
	while 1:
		print("아래에 사용을 원하는 사칙연산을 선택해주세요!\n"
		"1. 더하기\n2. 빼기\n3. 곱하기\n4. 나누기\n5. 제곱\n6. 최대 공약수\n7. 종료")

		N = int(input(">> "))
		if N == 7:
			print("계산기 프로그램을 종료합니다.")
			break

		num1, num2 = map(int, input("두 숫자를 입력해주세요: ").split())

		calc = improved_calculator(num1, num2)

		if N == 1:
			print(calc.add())
		
		elif N == 2:
			print(calc.sub())

		elif N == 3:
			print(calc.mul())

		elif N == 4:
			print(calc.div())

		elif N == 5:
			print(calc.power())

		elif N == 6:
			print(calc.gcd())

		print()

main()
