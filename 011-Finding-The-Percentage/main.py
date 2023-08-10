if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_marks = student_marks[query_name]
    

    
    sum_marks = 0
    for marks in query_marks:
        sum_marks += marks
    
    print("{:.2f}".format(sum_marks/len(query_marks)))       