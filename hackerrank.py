def palindromIndex(s):
    found = False
    print(s)
    print(len(s))
    # if its a palindrom return -1
    if s == s[::-1]: 
        return -1

    i = 0
    j = len(s)-1
    while(i < j):
        if s[i] != s[j]:
            # save the last i and j that were equal for the other side
            a = max(i-1,0)
            # check if the right side (j) can be an option
            if s[i] == s[j-1] and found is False:
                found = True
                idx = j
                i += 1
                j -= 2
            else:
                # try the left side
                break
        else:
            # keep going
            i += 1
            j -= 1
    
    if (found is True and i >= j):
        print(f'right: {i}')
        return idx
    # Else, try the other side
    found = False

    b = len(s)-a-1
    # print(a, b, s[a],s[b] )
    while(a < b):
        if s[a] == s[b]:
            a += 1
            b -= 1
            # if idx already found its more than one character
        elif s[a+1] == s[b] and found is False:
            found = True
            idx = a
            a += 2
            b -= 1
        else:
            return -1

    return idx

# print(palindromIndex('baa'))

def getTotalX(A, B):
     # numbers must be between the max of array A and the min of array B (inclusive)
    a = max(A)
    b = min(B)+1
    if b<a:
        return 0
    counter = 0
    # numbers must be multiples of a
    for n in range(a, b, a):
        if all(n%x == 0 for x in A) and all(x%n == 0 for x in B):
            counter += 1

    return counter

# getTotalX([2,4],[16,32,96])

# find minimum number of string to change to make to halfs of string anagram (contain the same letters)
def anagram(s):
    # Write your code here
    if len(s)%2 == 1: 
        return -1
    
    left = s[:int(len(s)/2)]
    right = s[int(len(s)/2):]
    print(left, right)

print(anagram('xaxbbbxx'))