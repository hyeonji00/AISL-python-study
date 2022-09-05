while (1) :

	print("---------------------------------------------------------------\n")
	print("“구구단을 외자, 구구단을 외자” 프로그램을 실행합니다.\n")
	print("1. 홀수 구구단\n2. 짝수 구구단\n3. 종료\n")
	print("---------------------------------------------------------------\n")

	num = int(input("숫자를 입력하세요: "))

	if num == 1 :
		for i in range(3, 10, 2):
			print("{}단".format(i))
			for j in range(1, 10):
				print(i, "*", j, "=", i * j)

	elif num == 2 :
		for i in range(2, 10, 2):
			print("{}단".format(i))
			for j in range(1, 10):
				print(i, "*", j, "=", i * j)

	elif num == 3 :
		print("프로그램을 종료합니다.")
		break

	else :
		print("잘못 입력하셨습니다. 1~3 번 숫자를 입력하세요.")