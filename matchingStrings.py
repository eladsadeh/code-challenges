def matchingStrings(strings, queries):
    res = []
    for q in queries:
        res.append(strings.count(q))
    
    print(res)

matchingStrings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab'])
