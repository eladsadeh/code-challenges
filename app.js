function persistence(num) {
	return `${num}`.length > 1
		? persistence(`${num}`.split('').reduce((acc, val) => acc * val)) + 1
		: 0;
}

// console.log(persistence(39));

// Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
// Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

const toJadenCase = function (string) {

	console.log(string.split(' ').map((word) => word.replace(word[0],word[0].toUpperCase())).join(' '))
	
};

toJadenCase('How can mirrors be real if our eyes aren\'t real')