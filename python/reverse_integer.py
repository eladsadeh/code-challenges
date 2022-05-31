def reverse(x):
    t=str(x)
    
    if(x<0):
        t='-'+t[:0:-1]
    else:
        t=t[::-1]
    x=int(t)
    if x<-2147483648 or x>2147483646:
        return 0
    return x