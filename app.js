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
	const odds = arr.filter((el) => el % 2);
	console.log(odds);
	return odds.length === 1 ? odds[0] : arr.filter((el) => !(el % 2))[0];
}

// console.log(findTheOddInt([1,5,11,5,14]));

function productFib(prod) {
	const fib = [0, 1];
	while (fib[0] * fib[1] < prod) fib.push(fib.shift() + fib[0]);

	console.log([fib[0], fib[1], fib[0] * fib[1] === prod]);
}

// productFib(273);

function intToRoman(int) {
	const digits = `${int}`.split('');
	const translation = [];
	const translate = [
		['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
		['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
		['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
	];

	if (int > 999) {
		translation.push('M'.repeat(digits.slice(0, digits.length - 3).join('')));
	}
	for (i = Math.min(digits.length - 1, 2); i >= 0; i--) {
		translation.push(translate[i][digits[digits.length - i - 1]]);
	}
	return translation.join('');
}

// console.log(intToRoman(1990));

// Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
// list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ])
// returns 'Bart, Lisa & Maggie'

function printNames(list) {
	return !list.length
		? ''
		: list.reduce(
				(acc, val, idx) =>
					idx === list.length - 1
						? `${acc} & ${val.name}`
						: `${acc}, ${val.name}`,
				list.shift().name
		  );
}

// console.log(printNames([]));

function countSmileys(arr) {
	// return arr.reduce((acc, val) =>
	// 	!!/[:|;][-|~]*[)|D]/.exec(val) ? ++acc : acc, 0
	return arr.reduce(
		(acc, val) => (!!val.match(/[:|;][-|~]*[)|D]/) ? ++acc : acc),
		0
	);
}

// console.log(countSmileys([]));

// Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
//pigIt('Pig latin is cool'); // igPay atinlay siay oolcay

function pigIt(string) {
	return string
		.split(' ')
		.map((word) =>
			/[a-z]/i.test(word[0])
				? word.split('').splice(1).concat([word[0], 'ay']).join('')
				: word
		)
		.join(' ');
}

//   return str.replace(/(\w)(\w*)(\s|$)/g, '$2$1ay$3');

// console.log(pigIt('Hello world !'));

// ┌───┬───┬───┐
// │ 1 │ 2 │ 3 │
// ├───┼───┼───┤
// │ 4 │ 5 │ 6 │
// ├───┼───┼───┤
// │ 7 │ 8 │ 9 │
// └───┼───┼───┘
//     │ 0 │
//     └───┘

//    "8": ["5", "7", "8", "9", "0"],
// "11": ["11", "22", "44", "12", "21", "14", "41", "24", "42"],
// "369": ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"]

// '13' => [[1, 2, 4],[2, 3, 6]]
// 12,13,16,22,23,26,42,43,46
// '130' => [[1, 2, 4],[2, 3, 6],[0,8]]
// 12,13,16,22,23,26,42,43,46
// 120,130,160,220,230,260,420,430,460,128,138,168,228,239,268,428,438,468

function getPINs(observed) {
	const possibilities = {
		0: ['0', '8'],
		1: ['1', '2', '4'],
		2: ['1', '2', '3', '5'],
		3: ['2', '3', '6'],
		4: ['1', '4', '5', '7'],
		5: ['2', '4', '5', '6', '8'],
		6: ['3', '5', '6', '9'],
		7: ['4', '7', '8'],
		8: ['0', '5', '7', '8', '9'],
		9: ['6', '8', '9'],
	};

	return observed.split('').reduce(
		(acc, val) => {
			const tmpArr = [];
			for (i = 0; i < acc.length; i++) {
				for (j = 0; j < possibilities[val].length; j++) {
					tmpArr.push(`${acc[i]}${possibilities[val][j]}`);
				}
			}
			return tmpArr;
		},
		['']
	);
	// acc.map(a => possibilities[val].map(b => `${a}${b}`)).flat(),[''])
}

function combineArrays(arr1, arr2) {
	console.log(arr1, arr2);
	return arr1.map((a) => arr2.map((b) => `${a}${b}`));
}

// console.log(getPINs('345'));
// console.log(combineArrays([8], [2, 3, 6]));

function humanReadable(seconds) {
	const hours = Math.floor(seconds / 3600);
	const minutes = Math.floor((seconds - 3600 * hours) / 60);
	seconds = seconds - 60 * minutes - 3600 * hours;
	return `${String(hours).padStart(2, '0')}:${String(minutes).padStart(
		2,
		'0'
	)}:${String(seconds).padStart(2, '0')}`;
}

// console.log(humanReadable(3689));

// write a function which increments a string, to create a new string.

// If the string already ends with a number, the number should be incremented by 1.
// If the string does not end with a number. the number 1 should be appended to the new string.

function incrementString(strng) {
	console.log(/([0-8]|\d?9+)?$/.exec(strng));
	let m = /^([a-z]*)([0-9]+)$/i.exec(strng);
	return m
		? `${m[1]}${String(++m[2]).padStart(strng.length - m[1].length, '0')}`
		: `${strng}1`;
}

// From codewars
// let incrementString = (str) =>
// 	str.replace(/([0-8]|\d?9+)?$/, (e) => (e ? +e + 1 : 1));

// console.log(incrementString('xx3x199'));

function add(a, b) {
	function addStrings(a, b) {
		const len = Math.max(a.length, b.length);
		let carry = 0;
		let addition = new Array(len).fill(0)
		a = a.padStart(len, '0').split('');
		b = b.padStart(len, '0').split('');
		for(i=len-1 ; i>=0; i--) {
			addition[i] = (Number(a[i]) + Number(b[i]) + carry) % 10;
			carry = Math.floor((Number(a[i]) + Number(b[i]) + carry) / 10);
		}
		return addition.join('');
	}
	return Number.MAX_SAFE_INTEGER > b + a
		? `${Number(a) + Number(b)}`
		: addStrings(a, b);
}

// Solution from codewars

function add(a, b) {
	var res = '',
		c = 0;
	a = a.split('');
	b = b.split('');
	while (a.length || b.length || c) {
		c += ~~a.pop() + ~~b.pop();
		res = (c % 10) + res;
		c = c > 9;
	}
	return res;
}
// console.log(add('63829983432984289347293874', '90938498237058927340892374089'));
