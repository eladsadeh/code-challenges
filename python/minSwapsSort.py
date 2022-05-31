def lilysHomework(arr):
    # function to count swaps to bring sorted array (s)
    # to reference array (r)
    def countSwaps(s,ref):
        count = 0
        i=0
        while i < len(arr):
        # if reference and sorted to the same value
            if s[i]['val'] != ref[i]['val']:
        # swap them and increment count
        # don't increment i to check again
                s[s[i]['idx']],s[i] = s[i],s[s[i]['idx']]
                count += 1
            else:
                i += 1

        return count

    # create object of value and index
    vec = [{"val": arr[i], "idx": i} for i in range(len(arr))]
    # assending sorted array
    a = sorted(vec, key=lambda x: x['val'])
    # dessending sorted array
    d = sorted(vec, key=lambda x: x['val'], reverse=True)

    return min(countSwaps(a,vec), countSwaps(d,vec))

lilysHomework([5,3,1,4,2])    