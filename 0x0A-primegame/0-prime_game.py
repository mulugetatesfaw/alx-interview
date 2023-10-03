#!/usr/bin/python3
def generate_primes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return primes

def isWinner(x, nums):
    winner = None
    prime_numbers = generate_primes(max(nums))

    for n in nums:
        prime_count = sum(prime_numbers[:n + 1])
        if prime_count % 2 == 0:
            # If the total count of prime numbers is even, Ben wins
            winner = 'Ben' if winner == 'Maria' else 'Maria'
        else:
            # If the total count of prime numbers is odd, Maria wins
            winner = 'Maria' if winner == 'Ben' else 'Ben'

    return winner
