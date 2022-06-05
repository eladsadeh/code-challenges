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
		let addition = new Array(len).fill(0);
		a = a.padStart(len, '0').split('');
		b = b.padStart(len, '0').split('');
		for (i = len - 1; i >= 0; i--) {
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

// Nesting Structure Comparison

Array.prototype.sameStructureAs = function (other) {
	if (!isArray(other)) return false;
	const isSameStructure = (a1, a2) => {
		if (a1.length !== a2.length) return false;
		for (i = 0; i < a1.length; i++) {
			// if both elements are arrays, check their structure
			if (isArray(a1[i]) && isArray(a2[i]))
				return isSameStructure(a1[i], a2[i]);
			// If one array and the other not, return false
			else if (isArray(a1[i]) !== isArray(a2[i])) return false;
			// if both not array, move to next element;
		}
		return true;
	};
	return isSameStructure(this, other);
};

// Codewars top solution
// Array.prototype.sameStructureAs = function (other) {
// 	return this.length === other.length
// 		? this.every(function (el, i) {
// 				return Array.isArray(el) ? el.sameStructureAs(other[i]) : true;
// 		  })
// 		: false;
// };

// [a,a,a] , [[a], a, a]
// 'a' : ['a'] -> true
// 'a' : 'a' -> true
// 'a' : 'a' -> true

// Alphabetic Anagrams
// Given a word, return its position in all posible combinations of the same letters, sorted alphabethically
// Sample words, with their rank:
// ABAB = 2
// AAAB = 1
// BAAA = 4
// QUESTION = 24572
// BOOKKEEPER = 10743

function listPosition(word) {
	// create array of the letters
	const chars = word.toUpperCase().split('').sort();
	// array of unique letters
	// const unique = [...new Set(chars)];
	// create an array of all possiblities
	let all = [];
	// chars.forEach((a, i) => {
	// 	// chars.forEach((b, j) => {
	// 	// 	if(i !== j)
	// 	// })
	// })

	// perform binary search to find the index of word
	console.log(chars, unique);
	return 1;
}

// generate all unique combinations whan edding a character to existing array of combinations
const uniqueCombinations = (arr, char) => {
	// go throug all elements in arr
	// arr.reduce((el) => {
	// 	el.split('').map((c) => )
	// })
};

// console.log(listPosition('abba'));
function plusMinus(arr) {
	zeros = arr.filter((e) => e === 0).length;
	pos = arr.filter((e) => e > 0).length;
	neg = arr.filter((e) => e < 0).length;

	[pos, neg, zeros].forEach((n) => {
		console.log((n / arr.length).toFixed(6));
	});
}

// plusMinus([-4, 3, -9, 0, 4, 1])

function miniMaxSum(arr) {
	const sum = arr.reduce((s, e) => s + e);
	const max = sum - Math.min(...arr);
	const min = sum - Math.max(...arr);
	console.log(max, min);
}

// miniMaxSum([1,3,5,7,9])

function timeConversion(s) {
	let [time, hour, min, ampm] = s.match(/(\d\d):(\d\d:\d\d)([a|p])m/i);
	if (hour === '12' && ampm === 'A') hour = '00';
	else if (ampm === 'P' && hour !== '12')
		hour = (Number(hour) + 12).toString().padStart(2, '0');
	return hour + ':' + min;
}

// timeConversion('11:01:34PM');

function matchingStrings(strings, queries) {
	const result = queries.map((e) => strings.filter((s) => s === e).length);
	console.log(result);
}

// matchingStrings(['ab', 'abc', 'ad', 'ab'], ['ab', 'ad', 'abc'])

function equalStacks(h1, h2, h3) {
	let hn = [[...h1], [...h2], [...h3]];
	// check the height of all arrays
	let heights = hn.map((h) => h.reduce((s, e) => e + s, 0));
	// let max = Math.max(...heights);
	while (heights.some((e) => e !== Math.max(...heights))) {
		if (!Math.min(...heights)) return 0;
		// if the heights are equal, return the height
		// if (heights.every((e) => e === max)) return max;
		// find the highst array
		const idx = heights.indexOf(Math.max(...heights));
		// remove the top most element from the highest array
		heights[idx] -= hn[idx].shift();
		// heights = hn.map((h) => h.reduce((s, e) => e + s, 0));
		// max = Math.max(...heights);
	}
	return heights[0];
	// check again
	// return equalStacks(...hn);
}

// console.log(equalStacks([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1]));
// console.log(equalStacks([2, 1, 1, 1], [3, 2], [4, 1]));
// console.log(equalStacks([1,1,1,1,2], [3,7], [1,3,1]));

function maxSubarray(arr) {
	// The maximum possible of any subset is all possitive numbers
	let subset = arr.reduce((s, e) => (e > 0 ? e + s : s), 0);
	subset = subset ? subset : Math.max(...arr);
	console.log(subset);
	// find the max subsequence foreach index
	let maxSeq = (prevMax = arr[0]);
	console.log(maxSeq, prevMax);
	for (i = 1; i < arr.length; i++) {
		// maxSeq[i] = Math.max(maxSeq[i-1], arr[i-1] + arr[i], arr[i])
		maxSeq = Math.max(maxSeq, prevMax + arr[i], arr[i]);
		prevMax = Math.max(prevMax + arr[i], arr[i]);
		// arr[i] = Math.max(arr[i - 1] + arr[i], arr[i]);
		console.log(maxSeq, prevMax);
	}
	console.log([maxSeq, subset]);
}

// maxSubarray([-2,-3,-1,-4,-6])

function lonelyinteger(a) {
	while (a.length) {
		const n = a.pop();
		if (!a.includes(n)) return n;
		a = a.filter((e) => e !== n);
	}
}

function flippingBits(n) {
	return 2 ** 32 - 1 - n;
}

// console.log(flippingBits(9));

function diagonalDifference(arr) {
	return Math.abs(
		arr.reduce(
			(sum, e, idx, arr) => sum + e[idx] - arr[idx][arr.length - 1 - idx],
			0
		)
	);
}

// console.log(diagonalDifference([
// 	[11, 2, 4],
// 	[4, 5, 6],
// 	[10, 8, -12],
// ]));

function countingSort(arr) {
	const freq = new Array(100).fill(0);
	arr.forEach((e) => freq[e]++);
	console.log(freq);
}

// countingSort([1,1,3,2,1])

function pangrams(s) {
	// create an array of all letters
	const alfa = 'abcdefghijklmnopqrstuvwxyz'.split('');
	// check that each letter is in the string
	return alfa.every((l) => s.toLowerCase().includes(l))
		? 'pangram'
		: 'not pangram';
}

// pangrams('We promptly judged antique ivory buckles for the next prize');
// pangrams('We promptly judged antique ivory buckles for the prize');

function twoArrays(k, A, B) {
	const Bsorted = B.sort((a, b) => a - b);
	console.log(Bsorted);
	// loop through all elments in A
	for (let num of A) {
		let i = 0;
		// find the smallest number in B that A + B >= k
		while (num + Bsorted[i] < k && i < Bsorted.length) {
			i++;
		}
		console.log(num, Bsorted[i], Bsorted.length);
		if (i >= Bsorted.length) return 'NO';
		// Remove the B element
		Bsorted.splice(i, 1);
	}
	return 'YES';
}

// console.log(twoArrays(10, [1,2,3], [9,8,7]))
// console.log(twoArrays(94, [84, 2, 50, 51, 19, 58, 12, 90, 81, 68, 54, 73, 81, 31, 79, 85, 39, 2], [53, 102, 40, 17, 33, 92, 18, 79, 66, 23, 84, 25, 38, 43, 27, 55, 8, 19]))

function gridChallenge(grid) {
	// create a sorted grid
	const sorted = grid.map((row) => row.split('').sort());
	// check that columns are sorted too
	for (let c = 0; c < grid.length; c++) {
		for (let r = 0; r < grid.length - 1; r++) {
			if (sorted[r + 1][c] < sorted[r][c]) {
				return 'NO';
			}
		}
	}
	return 'YES';
}

// console.log(gridChallenge(['xywuv','ebacd', 'fghij', 'olmkn', 'trpqs']));

function URLparser(site) {
	console.log(site);
	const regex = /(\S*)/;
	const urlString = site.match(/(https*:\/\/)*(www\.)*(\S*)\/*/);
	console.log(urlString);
	return site;
}

// URLparser('satambus.it');

var valid_countries = ['US', 'IT'];

function extractPrice(description, country) {
	if (!valid_countries.includes(country)) {
		return -1;
	}

	if (country == 'US') {
		var price = description.match(/\$(\d+\.\d+)/)[1];

		if (price == null) {
			return -1;
		}

		return parseFloat(price);
	}

	if (country == 'IT') {
		var price = description.match(/(\€*(\d+)[\.\€](\d+)\€*)/);
		if (price == null || !price[0].includes('€')) {
			return -1;
		}

		return parseFloat(`${price[2]}.${price[3]}`);
	}
}

// console.log(extractPrice('€19.99', 'IT'));
// console.log(extractPrice('19.99', 'US'));
// console.log(extractPrice('19.99€', 'IT'));
// console.log(extractPrice('19€99', 'IT'));

function solution(A) {
	for (let i = 1; i <= Math.max(A); i++) {
		if (!A.includes(i)) return i;
	}
	return i + 1;
}

function minimumStrings(S) {
	const blocks = S.match(/a+/g).concat(S.match(/b+/g));
	const mx = blocks.reduce((a, e) => (e.length > a ? e.length : a), 0);
	return blocks.reduce((t, e) => (t += mx - e.length), 0);
	console.log(blocks, mx, total);
}

// minimumStrings('aababbaaa')

// Exercize to print content of table cells if the background
// and text color are not the same (Codility for Grant street group)
function printTable() {
	const table = document.querySelector('table');
	const rows = table.rows;
	let text = '';
	Array.from(rows).forEach((row) => {
		const cols = row.getElementsByTagName('td');
		console.log(cols);
		Array.from(cols).forEach((col) => {
			if (col.style.color !== col.style.backgroundColor) {
				text += col.textContent;
			}
		});
	});
	return text;
}

function binaryGap(N) {
	const binary = N.toString(2).split('');
	let currentGap = 0;
	let biggestGap = 0;
	let count = false;
	for (i = 0; i < binary.length; i++) {
		if (!count && binary[i] === '1') count = true;
		else if (count && binary[i] === '0') currentGap++;
		else if (currentGap && binary[i] === '1') {
			// count = false;
			biggestGap = currentGap > biggestGap ? currentGap : biggestGap;
			currentGap = 0;
		}
		// console.log(binary[i],count, currentGap, biggestGap);
	}
	return biggestGap;
}

// binaryGap(328);

function compareDates(obj) {
	console.log(obj.d1, obj.d2);
	console.log(obj.d1 < obj.d2 ? 'd1' : 'd2');
}

// compareDates({ d1: new Date(2022, 4, 8), d2: new Date('2022-05-12') });
// compareDates(new Date(2022, 4, 8), new Date(2022, 4, 8));

function calcActivity(month, rate, users) {
	let [year, mon] = month.split('-');
	mon = Number(mon);
	// console.log(year, mon);
	const firstDay = new Date(year, mon - 1, 1);
	const lastDay = new Date(year, mon, 0);
	const daysInMonth = lastDay.getDate();
	let dailyUsers = new Array(daysInMonth).fill(0);
	// console.log(firstDay, lastDay);
	const dailyRate = rate.monthlyRate / daysInMonth;
	users.forEach((user) => {
		// console.log(user);
		let first = 1;
		let last = daysInMonth;
		user.end = user.end === null ? lastDay : user.end;
		// console.log(user.start, user.end);
		if (user.start === null) last = 0;
		else if (user.start > lastDay) {
			first = daysInMonth;
		} else if (user.start > firstDay) {
			first = user.start.getDate();
		}
		if (user.end < firstDay) {
			last = 0;
		} else if (user.end < lastDay) {
			last = user.end.getDate();
		}
		// console.log(first, last);
		if (last) {
			dailyUsers[first - 1] += 1;
			if (last < daysInMonth) dailyUsers[last] -= 1;
		}
	});
	// console.log(dailyUsers);
	let c = 0;
	let total = 0;
	dailyUsers.forEach((count, i) => {
		c += count;
		total += c * dailyRate;
		console.log(
			`${year}-${String(mon).padStart(2, '0')} ${c} $${
				c * dailyRate.toFixed(2)
			}`
		);
	});
	console.log(`Total: $${total.toFixed(2)}`);
}

// calcActivity('2019-01', { monthlyRate: 4 }, [
// 	{ id: 1, start: new Date(2018, 1, 1), end: null },
// 	{ id: 1, start: new Date(2018, 1, 1), end: new Date(2018, 11, 30) },
// 	{ id: 1, start: new Date(2018, 1, 1), end: new Date(2019, 0, 1) },
// 	{ id: 2, start: new Date(2018, 1, 1), end: new Date(2019, 0, 15) },
// 	{ id: 2, start: new Date(2019, 0, 15), end: new Date(2019, 0, 15) },
// 	{ id: 3, start: new Date(2019, 0, 10), end: null },
// 	{ id: 3, start: new Date(2019, 0, 31), end: null },
// 	{ id: 3, start: null, end: null },
// ]);

// function sum(a) {

// 	return function (b) {
// 		return a + b;
// 	};
// }

// let sum1 = sum(2)(-3);

function sum(a) {
	sum.current = (sum.current ?? 0) + a;
	sum.toString = () => sum.current;
	return sum;
// 	let currentSum = a;
// console.log(currentSum);
// 	function f(b) {
// 		// console.log(currentSum);
// 		currentSum += b;
// 		return f;
// 	}

// 	f.toString = function () {
// 		return currentSum;
// 	};

// 	return f;
}

// console.log(sum(2)(3)(-1).toString());
// console.log(sum(5)(-1));

function printNumbers(from, to) {
	let num = from;
	let id = setInterval(() => {
		console.log(num);
		if (num === to) clearInterval(id)
		num++
		
	}, 1000);
}

function printNumbersTimer(from,to) {
	let num = from;
	setTimeout(function wait() {
		console.log(num);
		num++
		if (num <= to) {
			setTimeout(wait, 1000);
		}
	}, 1000);
	
}

printNumbersTimer(4,9)