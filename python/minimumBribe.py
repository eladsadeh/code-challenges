def minimumBribes(q):
    bribes = 0
    for i in range(len(q)):
        displacement = q[i] - i - 1
        if displacement > 2:
            print("Too chaotic")
            return
        else:
            bribes += displacement if displacement > 0 else 0
    
    print(bribes)