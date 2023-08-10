if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        
Scorelist = [x[1] for x in records]

unique_score = set(Scorelist)
unique_score = list(unique_score)

unique_score.sort()
unique_score.remove(min(unique_score))

second_lowest_score = min(unique_score)


min_students = [x[0] for x in records if x[1] == second_lowest_score ]

min_students.sort()

for min_student in min_students:
    print(min_student)