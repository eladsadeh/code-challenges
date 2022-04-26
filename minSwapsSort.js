function lilysHomework(arr) {
	// function to count swaps to bring sorted array (s)
	// to reference array (r)
	function countSwaps(s) {
		let count = 0;
		let i = 0;
		while (i < arr.length) {
			if (s[i].val != arr[i]) {
				// swap them and increment count
				// don't increment i to check again
				[s[s[i].idx], s[i]] = [s[i], s[s[i].idx]];
				count += 1;
			} else i += 1;
		}

		return count;
	}

	// create object of value and index
	const vec = arr.map((val, i) => {
		return { val: val, idx: i };
	});
	// assending sorted array
	a = [...vec].sort((a, b) => a.val - b.val);
	// dessending sorted array
	d = [...vec].sort((a,b) => b.val - a.val)

	return Math.min(countSwaps(a), countSwaps(d));
}
console.log(lilysHomework([5, 3, 1, 4, 2]));
