function towerBreakers(arr) {
	// convert arr to nim array that represent the number of factors in each arr element
	console.log(arr);
	const nim = arr.map((n) => {
		if (n === 1) return 0;
		i = 2;
		count = 0;
		while (i <= n) {
			if (n % i === 0) {
				n /= i;
				count++;
			} else i++;
		}
		return count;
	});
	console.log(nim);
	return nim.reduce((xor, hight) => (xor ^= hight)) ? 1 : 2;
}
// console.log(towerBreakers([2, 6]));


// https://www.hackerrank.com/challenges/tower-breakers-again-1/forum
function towerBreakersAgain(arr) {
	// convert arr to nim array that represent the number of factors in each arr element
	console.log(arr);
	const nim = arr.map((n) => {
		if (n === 1) return 0;
		let count = 0;
		if (n%2 === 0) {
			count++;
			n /= 2;
		}
		let i = 3;
		while (i <= n) {
			if (n%2 === 0) n /= 2;
			else if (n % i === 0) {
				n /= i;
				count++;
			} else i++;
		}
		return count;
	});
	console.log(nim);
	return nim.reduce((xor, hight) => (xor ^= hight)) ? 1 : 2;
}

console.log(towerBreakersAgain([4,36]));
