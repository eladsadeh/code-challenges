# return the index of target in nums arrau
# or '-1' if not found
def search( nums, target):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low =mid+1
            else:
                high=mid-1
        
        return -1

# return the index of target in nums array
# or the index to insert if not found
def searchInsert(nums, target):
    left = 0
    right = len(nums)-1
    # edge cases
    if nums[right] < target:
        return right+1
    if nums[left] > target:
        return 0

    while left < right:
        mid = (right+left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid
        
    return right