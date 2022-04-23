from cgi import print_form


def highestValuePalindrome(s, n, k):
    r = [] # indexes where replacement needed
    for i in range(n//2):
        print(i, n-i-1)
        if s[i] != s[n-i-1]: r.append(i)
    print(r)

    # return -1 if there are more replacemnts than k
    if k < len(r): return -1

print(highestValuePalindrome('13945441', 8, 1))