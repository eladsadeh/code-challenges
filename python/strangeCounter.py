def strangeCounter(t):
   
    acc = 3
    while t > acc:
        t = t-acc
        acc *= 2

    print(acc-(t-1))

strangeCounter(21)