book_info = {
	"HarryPotter1" : [[1997], [6], [26]],
	"TheLordOfTheRings" : [[1954], [7], [29]],
	"engineering_mathematics1" : [[2018], [2], [28]]
}

while (1):

	book = input("원하시는 책을 입력하세요.\n>")

	if book in book_info:
		print("------------------------------------\n원하시는 정보를 선택해주세요.\n"
		"1. 년\n2. 월\n3. 일\n4. 종료\n------------------------------------")

		num = int(input())

		if num == 1:
			print("{}년 입니다.".format(book_info[book][0][0]))

		elif num == 2:
			print("{}월 입니다.".format(book_info[book][1][0]))

		elif num == 3:
			print("{}일 입니다.".format(book_info[book][2][0]))

		elif num == 4:
			print("프로그램이 종료되었습니다.")
			break


	else:
		print("제목을 다시 입력해주세요.")