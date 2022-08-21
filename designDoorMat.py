values = list(map(int, input().split()))
height = values[0]
width = values[1]

# upper half
pattern = ".|."

for i in range(1, height, 2):

    print(
        ("-" * int((width - (len(pattern * i))) // 2))
        + pattern * i
        + ("-" * int((width - (len(pattern * i))) // 2))
    )

# middle line
text = "WELCOME"
print(
    ("-" * int((width - (len(text))) // 2))
    + text
    + ("-" * int((width - (len(text))) // 2))
)


# lower half
for i in range(height-2,0,-2):
    
    print(
        ("-" * int((width - (len(pattern * i))) // 2))
        + pattern * i
        + ("-" * int((width - (len(pattern * i))) // 2))
    )