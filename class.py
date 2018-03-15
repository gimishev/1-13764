n = 100

for a in range(1, 100):
    for b in range(a, 100):
        c = a + b
        if 0.1 > (a / b) - (b / c) > 0:
            print(a, b)

