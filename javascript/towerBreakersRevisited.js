function towerBreakers(arr) {
	// convert arr to nim array that represent the number of factors in each arr element
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
	return nim.reduce((xor, hight) => (xor ^= hight)) ? 1 : 2;
}

console.log(towerBreakers([1, 2]));
