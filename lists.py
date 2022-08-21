N = int(input())

arr = []

for line in range(N):
    operations = input()
    operationSplit = operations.split(" ")
    if operationSplit[0] == "append":
        arr.append(int(operationSplit[1]))
    if operationSplit[0] == "insert":
        arr.insert(int(operationSplit[1]), int(operationSplit[2]))
    if operationSplit[0] == "print":
        print(arr)
    if operationSplit[0] == "remove":
        arr.remove(int(operationSplit[1]))
    if operationSplit[0] == "sort":
        arr.sort()
    if operationSplit[0] == "pop":
        arr.pop()
    if operationSplit[0] == "reverse":
        arr.reverse()
