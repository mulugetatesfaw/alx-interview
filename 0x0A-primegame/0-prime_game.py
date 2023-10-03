def isWinner(x, nums):
    if not nums or x < 1:
        return None

    def generate_primes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(pow(n, 0.5)) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        return primes

    prime_numbers = generate_primes(max(nums))
    winner = None

    for n in nums:
        prime_count = sum(prime_numbers[:n + 1])
        if prime_count % 2 == 0:
            winner = 'Ben' if winner == 'Maria' else 'Maria'
        else:
            winner = 'Maria' if winner == 'Ben' else 'Ben'

    return winner
