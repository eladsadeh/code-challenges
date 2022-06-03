# return the maximum area between two integers representing height

def maxArea(height) -> int:
    vol = 0
    maxh = max(height)
    # start from both ends and continue until i and j meets
    l, r = 0, len(height)-1
    # while l < r:
    # maxh*(r-l) is the maximum possible for current r and l
    # if vol is bigger than maximum possible, we can stop
    while maxh*(r-l) > vol:
        if height[l] < height[r]:
            vol = max(height[l]*(r-l),vol)
            # advance the left pointer if the left side is smaller
            l += 1
        else:
            vol = max(height[r]*(r-l),vol)
            # reduce the right side if the right side is smaller
            r -= 1
            
    return vol