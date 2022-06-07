# find combinations of three numbers that sum equal 0
# no duplaction and each number should be used once
def threeSum(nums):
    # edge cases
    if len(nums) < 3 or (len(nums) == 3 and sum(nums) != 0):
        return []
    
    nums.sort() # for two pointers
    out = set() # prevent duplication

    for i in range(len(nums)-2):
        j = i+1
        k = len(nums)-1
        while k>j:
            if nums[i]+nums[j]+nums[k] == 0:
                out.add((nums[i],nums[j],nums[k]))
                j += 1
                k -= 1
            elif nums[i]+nums[j]+nums[k] < 0:
                j += 1
            else:
                k -= 1
        
    return out