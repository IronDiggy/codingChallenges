def create_phone_number(n):
    string = "".join([str(item) for item in n])
    return "(" + string[0:3] + ") " + string[3:6] + "-" + string[6:]


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
