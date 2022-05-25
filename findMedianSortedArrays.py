# find the median of two sorted arrays

# since the arrays are sorted, we can use merge sort
# algorithm until we reach the median point
def findMedianSortedArrays(nums1, nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    nums = []
    l = l1+l2
    isOdd = True if l%2 else False
    mid = l//2
    i1 = i2 = 0
    while len(nums)-1 <= mid and (i1 < l1 or i2 < l2):
        print(i1, i2, l1, l2, nums)
        if (i1 < l1 and i2<l2):
            if (nums1[i1] <= nums2[i2]):
                nums.append(nums1[i1])
                i1 += 1
            else:
                nums.append(nums2[i2])
                i2 += 1
        elif (i1 < l1):
            nums.append(nums1[i1])
            i1 += 1
        elif (i2<l2):
            nums.append(nums2[i2])
            i2 += 1

    return nums[mid] if isOdd else (nums[mid]+nums[mid-1])/2

print(findMedianSortedArrays([],[1]))
