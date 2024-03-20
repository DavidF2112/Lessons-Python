import random
def generate():
    i = random.randbytes(10)
    i = i.split()
   
    ' '.join(map(str, i))
    for a in i:
        i.pop("/")
    return i 


print(generate())