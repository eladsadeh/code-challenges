def highestValuePalindrome(s, n, k):
    ri = [] # indexes that needs replacement
    mid = n//2 # mid index of s
    arr = list(s) # convert to array for easy replacements
    for i in range(mid):
    # find the indexes that needs replecement
        if arr[i] != arr[n-i-1]:
            # if one is '9' and we have replecements left,
            # replace the other one to '9'
            if k > 0 and (arr[i] == '9' or arr[n-i-1] == '9'):
                arr[i] = arr[n-i-1] = '9'
                k -= 1
            else:
            # save the index
                ri.append(i)

    # return -1 if there are more replacemnts than k
    if k < len(ri): return '-1'
    
    # if we have less than 2 extra replacements start replacing 
    # from the first index that needs replacement (if there is one)
    # otherwise start from 0
    i = ri[0] if k-len(ri)<2 and len(ri)>0 else 0
    
    while i <= mid and (k > 0 or len(ri)):
        if i in ri:
            ri.pop(0) # take out i
            # if we have 2 or more extra replacements
            if k-len(ri)>1:
            # replace both with '9'
                arr[i] = arr[n-i-1] = '9'
                k -= 2
            else:
            # replace the smaller of i or (n-i-1) with the
            # bigger element
                mx = max(arr[i],arr[n-i-1])
                arr[i] = arr[n-i-1] = mx
                k -= 1

        # else if we have 2 or more extra replacements
        # and its not already '9'
        elif k-len(ri)>1 and arr[i] != '9':
        # replace both sides with '9'
            arr[i] = arr[n-i-1] = '9'
        # reduce k by 2
            k -= 2
        # next index that needs replacement is ri[0].
        # if there is none, jump to the end
        nexti = ri[0] if len(ri)>0 else mid + 1
        # if we have less than 2 extra replacement
        # go next index that needs replacement
        # otherwise, go to the next index
        i = nexti if k-len(ri) < 2 else i + 1        
    # if there are any replacement left, and the string length
    # is odd, replace the middle to '9'
    if k > 0 and n%2:
        arr[mid] = '9'

    return ''.join(arr)