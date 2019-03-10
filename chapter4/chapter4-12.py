# ループの中断
a = 0
b = 5

while a < 5:
    if (b - a) <= 0:
        break
    print(b - a)
    a += 1
