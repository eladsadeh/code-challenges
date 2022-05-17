def twoSum(nums, target):
    map = {}
    for i,n in enumerate(nums):
        # check if we have the complementary index in 'map'
        key = target - n
        if key in map:
            return [map[key], i]
        else:
            map[n] = i