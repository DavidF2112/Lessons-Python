def geometric_progression(a,r):
    while True:
        yield a
        a *= r


gp = geometric_progression(2,3)
for _ in range(10):
    print(next(gp))