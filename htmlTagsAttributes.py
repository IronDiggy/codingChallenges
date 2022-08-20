import re

n = input()

htmlTags = []
for i in range(int(n)):
    line = input()
    htmlTags.append(line)

#print(htmlTags)

for item in htmlTags:
    