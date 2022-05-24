def getRow(rowIndex):
    # rows = [[1],[1,1]]
    #     if rowIndex < 2:
    #         return rows[rowIndex]
    #     for i in range(2,rowIndex+1):
    #         cur = [1]
    #         for j in range(1, i):
    #             cur.append(rows[i-1][j-1] + rows[i-1][j])
    #         cur.append(1)
    #         rows.append(cur)
        
    #     return rows[rowIndex]
    prev = [1]
    if rowIndex < 1:
        return prev
    for i in range(1,rowIndex+1):
        cur = [1]
        for j in range(1, i):
            cur.append(prev[j-1] + prev[j])
        cur.append(1)
        print(cur)
        prev = [*cur]
    
    print(cur)

getRow(6)
