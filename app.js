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
	return arr.filter((c) => c.toLowerCase() === 'x').length
	=== arr.filter((c) => c.toLowerCase() === 'o').length;
}

// console.log(XO('zzzbbb'));

function binaryToNum(arr) {
	console.log(arr.reduce((acc,val,idx) => acc + val * 2 ** (arr.length - idx -1),0));
}

binaryToNum([0,1,1,0])