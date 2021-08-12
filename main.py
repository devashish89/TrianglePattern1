# 1
# 22
# 303
# 4004
# 5005

for r in range(1, 6):
    # row is same as start no and each row has row no. elements
    val = ""
    for c in range(1, r + 1):
        if c == 1 or c == r:
            val += str(r)
        else:
            val += str(0)
    print(val)
