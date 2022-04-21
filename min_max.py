def solve(arr, queries):
    print(arr)
    # Correct solution but doesn't fail due to time constraint
    ans = []
    # for d in queries:
    #     maxs = [max(arr[i:i+d]) for i in range(len(arr)-d+1)]
    #     ans.append(min(maxs))
    # print(ans)
    for d in queries:
        # find max of first section and initialize min
        mn = mx = max(arr[:d])
        for i in range(1,len(arr)-d+1):
            # IF arr[i-1] is max, we need to find
            # the max of current section
            if arr[i-1] == mx:
                mx = max(arr[i:i+d])
                if mx < mn: mn = mx
            
        ans.append(mn)
            
    print(ans)

solve([5,3,4,3,5,4,8,2,1,2],[3])