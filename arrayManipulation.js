function arrayManipulation(n, queries) {
	const arr = new Array(n).fill(0)
    queries.forEach(([a,b,k]) => {
        arr[a-1] += k
        if(b < n) arr[b] -= k
    })
   console.log(arr.reduce(([c,mx],el) => [c += el, c > mx ? c : mx],[0,0])[1])
}

arrayManipulation(10, [[1,5 ,3],[4, 8, 5]] )