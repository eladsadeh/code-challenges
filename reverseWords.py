def reverseSentence(s):
    res = ' '.join([w for w in s.split(' ')[::-1] if w != ''])
    print(res)


print(reverseSentence(' the  sky is blue'))

def reverseWords(s):
    res = ' '.join([w[::-1] for w in s.split(' ')])
    print(res)


print(reverseWords('the sky is blue'))