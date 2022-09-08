def solution(new_id):

	#1
	new_id = new_id.lower()

	#2
	for i in new_id:
		if i.isalnum():
			pass
		elif i in ['-', '_', '.']:
			pass
		else:
			new_id = new_id.replace(i, "")

	#3
	while (".." in new_id):
		new_id = new_id.replace("..", ".")

	#4
	if new_id.find(".") == 0:
		new_id = new_id[1:]

	end = len(new_id) - 1
	if new_id.rfind(".") == end:
		new_id = new_id[:end]

	#5
	if new_id == "":
		new_id = "a"

	#6
	if len(new_id) >= 16:
		new_id = new_id[:15]

	end = len(new_id) - 1
	if new_id.rfind(".") == end:
		new_id = new_id[:end]

	#7
	if len(new_id) <= 2:
		end = len(new_id) - 1
		while len(new_id) < 3:
			new_id = new_id + new_id[end]

	return new_id


new_id = input("ID 입력 : ")
answer = ' '

answer = solution(new_id)
print("추천 ID :", answer)