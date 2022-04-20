import heapq

def cookies(k, A):
    heapq.heapify(A)
    count = 0

    while A[0] < k and len(A) > 1:
        a = heapq.heappop(A)
        b = heapq.heappop(A)
        heapq.heappush(A, a + 2*b)
        count += 1

    return count if A[0] >= k else -1
