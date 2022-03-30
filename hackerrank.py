def palindromIndex(s):
    found = False
    print(s)
    print(len(s))
    # if its a palindrom return -1
    if s == s[::-1]: 
        return -1

    i = 0
    j = len(s)-1
    while(i < j):
        if s[i] != s[j]:
            # save the last i and j that were equal for the other side
            a = max(i-1,0)
            # check if the right side (j) can be an option
            if s[i] == s[j-1] and found is False:
                found = True
                idx = j
                i += 1
                j -= 2
            else:
                # try the left side
                break
        else:
            # keep going
            i += 1
            j -= 1
    
    if (found is True and i >= j):
        print(f'right: {i}')
        return idx
    # Else, try the other side
    found = False

    b = len(s)-a-1
    # print(a, b, s[a],s[b] )
    while(a < b):
        if s[a] == s[b]:
            a += 1
            b -= 1
            # if idx already found its more than one character
        elif s[a+1] == s[b] and found is False:
            found = True
            idx = a
            a += 2
            b -= 1
        else:
            return -1

    return idx

# print(palindromIndex('baa'))

def getTotalX(A, B):
     # numbers must be between the max of array A and the min of array B (inclusive)
    a = max(A)
    b = min(B)+1
    if b<a:
        return 0
    counter = 0
    # numbers must be multiples of a
    for n in range(a, b, a):
        if all(n%x == 0 for x in A) and all(x%n == 0 for x in B):
            counter += 1

    return counter

# getTotalX([2,4],[16,32,96])

# find minimum number of string to change to make to halfs of string anagram (contain the same letters)
def anagram(s):
    # if s is odd number of letters
    if len(s)%2 == 1: 
        return -1
    
    left = s[:len(s)//2]
    right = s[len(s)//2:]
    # for every letter in left,
    for l in left:
    # if letter found in right, remove from right
        right = right.replace(l,'',1)
    # return the length of right
    return len(right)

# print(anagram('xaxbbbxx'))

def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1,0,-1):
        if i+1 != q[i]:
            j = 1
            while(i+1 != q[i-j]):
                if j > 1: 
                    return print('Too chaotic')
                j += 1
            bribes += j
            q.pop(i-j)
        else:
             q.pop()
               
    print(bribes)

# minimumBribes([2,1,5,3,4])
# minimumBribes([2,5,1,3,4])

def isValid(s):
    f = []
    while len(s) > 0:
        f.append(s.count(s[0]))
        s = s.replace(s[0],'')

    mini = min(f)
    maxi = max(f)

    print(f, min(f), f.count(maxi))
    if max(f) == min(f) or (f.count(mini) == len(f)-1 and maxi-mini == 1) or (f.count(maxi) == len(f)-1 and mini == 1):
        return 'YES'

    return 'NO'

# print(isValid('abcdefghhgfedecba'))

def climbingLeaderboard(ranked, player):
    res = []
    # create a uniqu ranked array
    uniq = list(dict.fromkeys(ranked).keys())

    r = len(uniq)-1
    for score in player:
        while r >= 0 and score >= uniq[r]:
            r -= 1
        res.append(r+2)

    print(res)

# climbingLeaderboard([100,100,50,40,40,20,10], [5,25,50,110,120])

def reverse(llist):
	w = llist
	r = None
	while (w):
		w.prev = w.next
		w.next = r
		r = w
		w = w.prev
	return r

def insertNodeAtPosition(llist, data, position):
    new_node = SinglyLinkedListNode(data)
    w = llist
    i = 1
    while(w and i < position):
        w = w.next
        i += 1
    
    new_node.next = w.next
    w.next = new_node
    return llist

def mergeLists(head1, head2):
    if(head1 == None): return head2
    if(head2 == None): return head1

    if head1.data <= head2.data:
        head = head1
        w1 = head1.next
        w2 = head2
    else:
        head = head2
        w1 = head1
        w2 = head2.next
    w = head
    while w1 and w2:
        if w1.data <= w2.data:
            w.next = w1
            w1 = w1.next
        else:
            w.next = w2
            w2 = w2.next
        w = w.next

    w.next = w1 if w2 == None else w2

    return head

# Two sum function
def icecreamParlor(m, arr):
    # Object to store previous possible options
    used = {}
    # For each index/cost
    for i,cost in enumerate(arr):
        # Key + cost = m (total)
        key = m - cost
        # If key in 'storage' than key + cost is what we are looking for, return the indexes
        if key in used:
            return [used[key], i+1]
        # Otherwise, store for the next options
        else:
            used[cost] = i+1

# Queue with two stacks
class Queue:
    def __init__(self):
        self.en = []
        self.dq = []
 
    # EnQueue item to the queue
    def enQueue(self, x):
        self.en.append(x)
 
    # DeQueue item from the queue
    def deQueue(self):

        # if both the stacks are empty
        if len(self.en) == 0 and len(self.dq) == 0:
            return None

        # if dq is empty and en has elements
        # move all items to dq stack
        elif len(self.dq) == 0 and len(self.en) > 0:
            while len(self.en):
                self.dq.append(self.en.pop())
        # dequeue from dq stack
        return self.dq.pop()
    
    def peek(self):
        # if both the stacks are empty
        if len(self.en) == 0 and len(self.dq) == 0:
            return None

        # if dq is empty print the first item in en, 
        # else print the last itme in dq
        print(self.en[0]) if len(self.dq) == 0 else print(self.dq[len(self.dq)-1])
    
queue = Queue()
for _ in range(int(input())):
    l = input()
    if l == '3':
        queue.peek()
    elif l == '2':
        queue.deQueue()
    else:
        [q, x] = l.split(' ')
        queue.enQueue(x)
