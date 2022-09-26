import random

list = ["python", "programing", "line", "hangman"]
random_str = list[random.randrange(0, 4)]
length = len(random_str)
wrong_cnt = 6

answer = ["_" for i in range(length)]

while wrong_cnt > 0:
	print(*answer)
	letter = input("Input letter > ")
	change_flag = 0

	for i in range(length):
		if random_str[i] == letter:
			if change_flag == 0:
				print("Correct")
			answer[i] = letter
			change_flag = 1

	if change_flag == 0:
		wrong_cnt -= 1
		print("Wrong 남은 시도 횟수 : {}".format(wrong_cnt))

	if wrong_cnt:
		print()

	if "_" not in answer:
		print(*answer)
		print("SUCESS")
		break

print("word = {}".format(random_str))