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
                # the right side can't be palindrom
                # try the left side
                break
        else:
            # keep going
            i += 1
            j -= 1
    
    if (found is True and i >= j):
        print(f'right: {i}')
        return idx
    # Try the other side
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

print(palindromIndex('baa'))
'''
found = False
    # if its a palindrom return -1
    if s == s[::-1]: 
        return -1
    # check the left side
    i = 0
    j = len(s)-1
    while(i < j):
        if s[i] == s[j]:
            i += 1
            j -= 1
        elif found is True:
            # if idx already found its more than one character
            break
        elif s[i] == s[j-1]:
            found = True
            idx = j
            i += 1
            j -= 2
        else:
            # more than one characters are not the same
            break
    # if the foreign character was found and the whole string was checked return the index
    if (found is True and i >= j): 
        return idx
        
    # Try the other side
    found = False
    i = 0
    j = len(s)-1
    while(i < j):
        if s[i] == s[j]:
            i += 1
            j -= 1
        elif found is True:
            # if idx already found its more than one character
            return -1
        elif s[i+1] == s[j]:
            idx = i
            i += 2
            j -= 1
        else:
            return -1
    return idx
'''

const numbers 