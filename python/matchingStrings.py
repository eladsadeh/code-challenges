def matchingStrings(strings, queries):
    res = []
    res2= []
    for q in queries:
        res.append(strings.count(q))

    for q in queries:
        s = filter(lambda x: x == q, strings)
        res2.append(len(list(s)))
    
    print(res, res2)

matchingStrings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab'])
