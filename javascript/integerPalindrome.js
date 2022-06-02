// Check if integer is palindrome without converting to string
var isPalindrome = function (x) {
	if (x < 0 || (x % 10 === 0 && x !== 0)) return false;
	if (x < 10) return true;
	let reversed = 0;

	while (x > reversed) {
		reversed = reversed * 10 + (x % 10);
		x = Math.floor(x / 10);
		// console.log(x, reversed);
	}
	return x === reversed || x === Math.floor(reversed / 10);
};
