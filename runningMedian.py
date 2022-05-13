import heapq

def runningMedian(a):
# insert number to either bigger or smaller heaps
    def insert(num, bigger, smaller):
        if num > bigger[0]:
            if len(bigger) > len(smaller):
# if there are more numbers in the bigger heap, move
# the smallest to the smaller heap and add the new num
                heapq.heappush(smaller, -heapq.heappop(bigger))
            heapq.heappush(bigger, num)
        else:
# add the number to the smaller heap, and check that the heaps 
# are balanced, correct if needed
            heapq.heappush(smaller, -num)
            if len(smaller) - len(bigger) > 1:
                heapq.heappush(bigger, -heapq.heappop(smaller))

# return the median        
    def get_median(bigger,smaller):
        if len(bigger) == len(smaller):
            return float((bigger[0]-smaller[0])/2)
        elif len(bigger) > len(smaller):
            return float(bigger[0])
        else:
            return float(-smaller[0])
        
    # Create heaps for bigger and smaller numbers
    # initialize the bigger heap with the first number
    bigger = [a.pop(0)]
    smaller = []
    # array of meadians initialzed with the first element
    medians = [round(float(bigger[0]),1)]
    
    for num in a:
        insert(num, bigger, smaller)
        medians.append(round(get_median(bigger,smaller),1))
            
    return medians