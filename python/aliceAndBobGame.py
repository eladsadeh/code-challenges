# https://www.hackerrank.com/challenges/alice-and-bobs-silly-game/problem
# find how many prime numbers there are between 2 and n
def sillyGame(n):
    if n == 1:
        return 'Bob'
    
    is_prime = [1] * (n+1)
    num =2
    # mark non prime numbers
    while num*num <= n:
        if is_prime[num]:
            for i in range(num*num,n+1,num):
                is_prime[i] = 0
        num += 1

    return 'Alice' if is_prime[2:].count(1)%2 else 'Bob'
   