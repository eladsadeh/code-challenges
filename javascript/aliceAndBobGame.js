//  https://www.hackerrank.com/challenges/alice-and-bobs-silly-game/problem
//  find how many prime numbers there are between 2 and n
function sillyGame(n) {
	if (n === 1) return 'Bob';

	isPrime = new Array(n + 1).fill(true);
	let num = 2;
	// mark non prime numbers
	while (num * num <= n) {
		if (isPrime[num]) {
			for (i = num * num; i < n + 1; i += num) {
				isPrime[i] = false;
			}
		}
		num += 1;
	}
	const count = isPrime.reduce((c, p) => (p ? c + 1 : c),0);

	return count%2 ? 'Alice' : 'Bob'
}

console.log(sillyGame(11));
