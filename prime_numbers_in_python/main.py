# Get all prime numbers in a given range
from time import perf_counter
from math import sqrt


# Approach 1
def check_if_prime_app_1(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# Approach 2
def check_if_prime_app_2(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False

    return True


# Approach 3
def check_if_prime_app_3(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


# Approach 4
def check_if_prime_sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)

    # mark 1 and 0 as not prime
    prime[0] = prime[1] = False

    p = 2

    while p ** 2 <= n:
        if prime[p] == True:
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1

    res = [{'number': i, 'is_prime': prime[i]} for i in range(n + 1)]
    return res


if __name__ == '__main__':
    start_time = perf_counter()

    N = 10000

    # code for app 1-3
    for i in range(N + 1):
        print(
            {
                'number': i,
                # 'is_prime': check_if_prime_app_1(i)    # Time for N=10000 is 0.392423875 s
                # 'is_prime': check_if_prime_app_2(i)    # Time for N=10000 is 0.244428833 s
                'is_prime': check_if_prime_app_3(i)  # Time for N=10000 is 0.117226792 s
            }
        )

    # code for app 4
    print(*check_if_prime_sieve_of_eratosthenes(N), sep='\n')  # Time for N=10000 is 0.028863834 s

    print(f'Time taken for the program to run for N={N}:{perf_counter() - start_time}')
