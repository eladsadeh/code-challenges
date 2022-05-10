function matchingStrings(strings, queries) {
	let res = []
    queries.forEach(q => {
        res.push(strings.filter(s => s === q).length)
    })
    return res
}
