# check if an array of integers can be divided into two arrays
# with equal sum
def canPartition(nums) -> bool:
    # if the sum if the array is not even, it can't be 
    # divided into two equal parts
    if sum(nums)%2!=0:
        return False
    # We need to find numbers that sum to half of the total
    target=sum(nums)//2
    # set of sums
    sums=set()
    sums.add(0)
    for num in nums:
        # temporary set so we don't change sums during iteration
        sumsCopy=set()
        for s in sums:
        # for each sum in sums, check if adding current number is what we are looking for, and return True if so
            if s+num==target:
                return True
        # Else, add both sum and sum+num to sums set
            sumsCopy.add(s)
            sumsCopy.add(s+num)
        # update sums set
        sums=sumsCopy
    return False