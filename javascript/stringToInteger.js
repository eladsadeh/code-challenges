function myAtoi(s) {
	// return Math.max(-(2**31),Math.min(2**31-1,parseInt(s)||0))

	const str = s.trim().split('');
	let res = 0;
	let sign = 1;
	let i = 0;
	if (str[0] == '-' || str[0] == '+') {
		sign = str[0] === '-' ? -1 : 1;
		i++;
	}
	while (i < str.length && !isNaN(parseInt(str[i]))) {
		res = res * 10 + parseInt(str[i]);
		i++;
	}
	return sign * res < -2147483648
		? -2147483648
		: Math.min(2147483647, sign * res);
};
