x = int(1)
y = int(1)
z = int(2)
n = int(3)

xList = [i for i in range(x + 1)]
yList = [i for i in range(y + 1)]
zList = [i for i in range(z + 1)]

list = [[x, y, z] for x in xList for y in yList for z in zList if x + y + z != n]

print(xList)
print(yList)
print(zList)

print(list)
