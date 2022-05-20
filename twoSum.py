def twoSum(nums, target):
    map = {}
    for i,n in enumerate(nums):
        # check if we have the complementary index in 'map'
        key = target - n
        if key in map:
            return [map[key], i]
        else:
            map[n] = i

def twoSumTwoPointers(nums,target):
    l = 0
    r = len(nums)-1
    while l<r:
        sum = nums[l] + nums[r]
        print(sum)
        if sum == target:
            return [l+1, r+1]
        elif sum < target:
            l += 1
        else:
            r -= 1

print(twoSumTwoPointers([2,7,11,15],9))