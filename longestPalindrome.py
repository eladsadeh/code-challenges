def longestPalindrome(s):

    def maxPalindrome(s, left, right):
        l = left
        r = right
        while l >=0 and r < len(s) and s[l] == s[r]:
            # print("f:",l,r)
            l -= 1
            r += 1
            
        return r-l-1
    
    if len(s) < 2:
        return s
    
    p = 0
    mx_len = 1
    
    for i in range(0, len(s)-1):
        len1 = maxPalindrome(s, i, i)
        len2 = maxPalindrome(s,i,i+1)
        if max(len1, len2) > mx_len:
            mx_len = max(len1,len2)
            p = i - (mx_len-1)//2
            
    return s[p:p+mx_len]

print(longestPalindrome('bb'))
