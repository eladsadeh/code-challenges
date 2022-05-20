def minSubArrayLen(target, nums):
    # loop through nums array (i)
    sub = []
    sum = 0
    j = 0
    for i in range(len(nums)):
        while sum < target and j < len(nums):
            sum += nums[j]
            j += 1
        if sum >= target:
            sub.append(j-i)
        sum -= nums[i]
    return 0 if len(sub) == 0 else min(sub)

print(minSubArrayLen(7, [3,2,1,2,4,3]))