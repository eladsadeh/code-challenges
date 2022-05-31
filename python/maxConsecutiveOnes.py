def findMaxConsecutiveOnes(nums) -> int:
        start = -1
        # end = -1
        mx = cur = 0
        for d in nums:
            if d == 1:
                cur += 1
                mx = cur if cur > mx else mx
            else:
                cur = 0
            
                
        return mx

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))