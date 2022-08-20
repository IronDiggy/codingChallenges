scoresList = list()


for line in range(int(input())):
    name = input()
    score = float(input())
    scoresList.append([name, score])

scoreStorage = list()

for score in scoresList:
    if score[1] in scoreStorage:
        continue
    else:
        scoreStorage.append(score[1])

scoreStorage.sort()


nameStorage = list()
for name in scoresList:
    if name[1] == scoreStorage[1]:
        nameStorage.append(name[0])


nameStorage.sort()
for name in nameStorage:
    print(name)
