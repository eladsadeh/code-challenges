// # https://www.hackerrank.com/challenges/larrys-array/problem
// # check if array can be sorted by rotating any 3 consecative
// # elements. For general solution, if swaps%(R-1) is 0 -> YES
// # R is size of subarray.
function larrysArray(A) {
	return A.reduce(
		(swaps, a, i) =>
			(swaps += A.slice(i + 1).reduce(
				(count, b) => (a > b ? (count += 1) : count),
				0
			)),
		0
	) % 2
		? 'NO'
		: 'YES';
}

console.log(larrysArray([1, 3, 4, 2]));
