import pandas as pd

def find_bus(bus_stop):
	file_path = "/Users/hyeonji/Downloads/20220420기준_서울시_버스노선별정류소정보.xlsx"
	file = pd.read_excel(file_path)
	print(file)

def find_busstop(bus_num):
	pass


while 1:
	print("=" * 40 + "\n1. 정류장 정차 버스 찾기\n2. 버스노선의 정차 정류장 찾기\n3. 종료\n" + "=" * 40)
	N = int(input("정수값을 선택하시오 : "))

	if N == 1:
		bus_stop = input("정류장 이름을 입력하세요 (일부 명칭도 가능): ")
		find_bus(bus_stop)
	elif N == 2:
		bus_num = int(input("버스노선명을 입력하세요 : "))
		find_busstop(bus_num)
	elif N == 3:
		print("프로그램을 종료합니다.")
		break
