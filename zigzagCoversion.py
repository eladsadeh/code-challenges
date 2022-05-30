def convert(s, numRows):
    lines = [''] * numRows
    n = len(s)
    for i in range(n):
        c = i%(numRows*2-2)
        m = c%numRows
        if c < numRows:
            row_idx = c
        else:
            row_idx = numRows - m -2
        lines[row_idx] += s[i]
        # row_idx, dir = 0,1
        # for c in s:
        #     lines[row_idx] += c
        #     if row_idx == 0:
        #         dir = 1
        #     elif row_idx == numRows-1:
        #         dir = -1
        #     row_idx += dir
    return ''.join(lines)


convert('abcdefghijklm',5)