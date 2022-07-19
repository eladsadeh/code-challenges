def findPrimes(n):
    if n == 1:
        return 'Bob'

    # def isPrime(m): 
    #     for num in primes:
    #         if m%num == 0:
    #             return False
    #     return True
    
    is_prime = [1] * (n+1)
    num =2
    count = 0
    while num <= n:
    # for num in range(2,n//2+1):
        if is_prime[num]:
            count += 1
            for i in range(num*num,n+1,num):
                is_prime[i] = 0
        num += 1

    print(is_prime)
    print(is_prime[2:].count(1))
    print(count)

    # primes = [2]
    # for i in range (2,n+1):
    #     if isPrime(i):
    #         primes.append(i)
    # print(primes)
    # return len(primes)

print(findPrimes(11))