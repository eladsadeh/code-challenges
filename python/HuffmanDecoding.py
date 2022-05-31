def decodeHuff(root, s):
    NULL = "\x00"
    w = root
    string = ''
    for n in s:
        w = w.left if n == '0' else w.right
        if w.data is not NULL:
            string += w.data
            w = root
    
    print(string)