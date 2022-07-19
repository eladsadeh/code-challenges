def countPrimes(n):
    if n == 1:
        return 'Bob'

    def isPrime(m):
    
        for num in primes:
            if m%num == 0:
                return False
        return True
    
    primes = [2]

    for i in range (2,n+1):
        if isPrime(i):
            primes.append(i)
    print(primes)
    return len(primes)

print(countPrimes(1))