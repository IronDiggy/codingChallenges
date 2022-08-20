n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
totalMark = 0
marks = student_marks[query_name]
for mark in marks:
    totalMark += mark

totalMark = totalMark / len(marks)
print("{0:.2f}".format(totalMark))
