s = input()
alphaNum = False
alpha = False
digit = False
lower = False
upper = False

for char in s:
    if char.isalnum():
        alphaNum = True
    if char.isalpha():
        alpha = True
    if char.isdigit():
        digit = True
    if char.islower():
        lower = True
    if char.isupper():
        upper = True

print(alphaNum)
print(alpha)
print(digit)
print(lower)
print(upper)
