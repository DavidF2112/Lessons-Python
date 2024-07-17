def generate():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

gen = generate()
for _ in range(10):
    print(next(gen))