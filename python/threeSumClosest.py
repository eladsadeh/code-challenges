# return the closest sum of three numbers to target
def threeSumClosest(nums, target) -> int:
    # edge case
    if len(nums) == 3:
        return sum(nums)
    
    closest = sum(nums[:3]) # first guess
    if closest == target:
        return closest
    
    nums.sort()
    for i in range(len(nums)-2):
        j = i+1
        k = len(nums)-1
        while k>j:
            sum3 = nums[i]+nums[j]+nums[k]
            if sum3 == target:
                return sum3
            if abs(sum3-target)<abs(closest-target):
                closest = sum3
            if sum3<target:
                j +=1
            else:
                k -= 1
        
    return closest