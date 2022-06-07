def longestCommonPrefix(strs) -> str:
    # find the length of the shortest string   
    min_length = len(min(strs))
    if min_length == 0:
        return ''
    # choose reference string
    ref = strs.pop()
    # initialize answer and match boolean
    ans = ''
    match = True
    # iterate through the first "min_length" characters of the reference
    for i in range(min_length):
        j = 0 # index of the strings array
        c = ref[i] # reference character
        # iterate through strings until match is False
        while j<len(strs) and match:
        # if mismatch, stop iterating
            if c != strs[j][i]:
                match = False
            j += 1
        # if match all strings, add character to answer
        if match:
            ans += c
        # else return the answer
        else:
            return ans
            
    return ans