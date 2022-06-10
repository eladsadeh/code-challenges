def happyLadybugs(b):
    if b.count('_') == len(b):
        print('YES')
    # print([b.count(c) for c in set(b) if c != '_'])
    elif min([b.count(c) for c in set(b) if c != '_'])==1:
        print('NO')
    elif (b.count('_') == 0):
        b = '#' + b + '#'
        for i in range(1,len(b)-1):
            if b[i-1] != b[i] and b[i] != b[i+1]:
                print('NO')

    print('YES')


happyLadybugs('RRRR')