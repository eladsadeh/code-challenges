function persistence(num) {
	return `${num}`.length > 1
		? persistence(`${num}`.split('').reduce((acc, val) => acc * val)) + 1
		: 0;
}

// console.log(persistence(39));

// Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
// Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

const toJadenCase = function (string) {
	console.log(
		string
			.split(' ')
			.map((word) => word.replace(word[0], word[0].toUpperCase()))
			.join(' ')
	);
};

// toJadenCase('How can mirrors be real if our eyes aren\'t real')

// Tribonacci: return array length n with tribonacci series beginning with a seed array: ([0,1,2],5) => [0,1,2,3,6]
function tribonacci(signature, n) {
	if (n < 3) return signature.splice(0, n);
	while (signature.length < n) {
		signature.push(
			signature.slice(signature.length - 3).reduce((acc, val) => acc + val)
		);
	}
	return signature;
}

// console.log(tribonacci([1, 1, 1], 0));

function XO(string) {
	const arr = string.split('');
	return (
		arr.filter((c) => c.toLowerCase() === 'x').length ===
		arr.filter((c) => c.toLowerCase() === 'o').length
	);
}

// console.log(XO('zzzbbb'));

// Given an array of ones and zeroes, convert the equivalent binary value to an integer.
// Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

function binaryToNum(arr) {
	console.log(
		arr.reduce((acc, val, idx) => acc + val * 2 ** (arr.length - idx - 1), 0)
	);
}

const binaryArrayToNumber = (arr) => parseInt(arr.join(''), 2);

// console.log(binaryArrayToNumber([1, 1, 1, 0]));

// moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]

function moveZeros(arr) {
	console.log(
		Array(...arr.filter((e) => e !== 0), ...arr.filter((e) => e === 0))
	);
	return arr;
}
// moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]

// Who likes it?
// []                                -->  "no one likes this"
// ["Peter"]                         -->  "Peter likes this"
// ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
// ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
// ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

function whoLikesIt(arr) {
	const answers = [
		'no one likes this',
		`${arr[0]} likes this`,
		`${arr[0]} and ${arr[1]} like this`,
		`${arr[0]}, ${arr[1]} and ${arr[2]} like this`,
		`${arr[0]}, ${arr[1]} and ${arr.length - 2} others like this`,
	];

	console.log(answers[arr.length > 4 ? 4 : arr.length]);
}

// whoLikesIt(['Elad', 'Alex', 'Jacob','anthony']);

function findTheOddInt(arr) {
	const odds = arr.filter(el => el %2);
	console.log(odds);
	return odds.length === 1 ? odds[0] : arr.filter(el => ! (el % 2))[0];
}

console.log(findTheOddInt([1,5,11,5,14]));
