def prime_generator(limit):

    if limit < 2:
        return
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False  
    
    for num in range(2, limit):
        if is_prime[num]:
            yield num
            for multiple in range(num * num, limit, num):
                is_prime[multiple] = False


for prime in prime_generator(50):
    print(prime)
