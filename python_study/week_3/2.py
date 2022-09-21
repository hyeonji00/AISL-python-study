def solve_boat_num(people):
	boat = 0
	sorted_people = sorted(people)

	i = 0
	j = len(sorted_people) - 1

	while i <= j:
		if sorted_people[i] + sorted_people[j] <= limit:
			i += 1
		j -= 1
		boat += 1
	
	return boat

N = int(input("인원을 입력하세요.\n>> "))
limit = int(input("구명보트의 무게 제한을 입력하세요.(40 ~ 240)\n>> "))
print("{}명의 몸무게를 입력하세요.\n>>".format(N))
people = []

for i in range(N):
	weight = int(input())
	people.append(weight)

print(solve_boat_num(people))