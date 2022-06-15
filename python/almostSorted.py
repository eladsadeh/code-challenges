# https://www.hackerrank.com/challenges/almost-sorted/problem
def almostSorted(arr):
    l = -1 # first mismatch
    r = len(arr)-1 # last mismatch
    diff = 0 # number of mismatches
    arr_sorted = sorted(arr)
    for i in range(len(arr)):
    # count mismatches with sorted array
    # and log the first (l) and last (r) mismatches
        if arr[i] != arr_sorted[i]:
            diff += 1
            if l < 0: 
                l = i
            else:
                r = i
  
    if diff == 0 or len(arr)<2:
        print('yes')
    elif diff == 2:
    # if only 2 mismatches, swap them
        print('yes')
        print('swap',l+1, r+1)
    elif arr[l:r+1][::-1] == arr_sorted[l:r+1]:
    # reversing the sub array match the sorted array
        print('yes')
        print('reverse', l+1, r+1)
    else:
        print('no')

almostSorted([5,4,3,1,2,6])
