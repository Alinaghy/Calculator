def calculate_floor(string):
    D = 0
    U = 0
    for i in string:
        if i == "U":
            U += 1
        if i == "D":
            D += 1
    return U-D

