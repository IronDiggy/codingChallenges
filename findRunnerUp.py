n = int(3)
arr = map(int, "-10 0 10".split())

originalList = list(arr)
newList = []
j = -1000

for i in originalList:
    if i > j:
        j = i
        newList.append(i)
    elif i < j:
        newList.append(i)


newList.sort(reverse=True)


print(newList[1])
