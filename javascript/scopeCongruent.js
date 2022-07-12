function scope_congruent(input_str) {
	// loop through pairs of strings
	for (let i = 0; i < input_str.length; i += 2) {
		// find substrings and their scope
		scopes1 = processString(input_str[i]);
		scopes2 = processString(input_str[i + 1]);
		console.log(scopes1, scopes2);
		if (!scopes1 || !scopes2) return -1;
		// console.log(Object.keys(scopes2));
		for (let str of Object.keys(scopes2)) {
			// console.log(str);
			if (str in scopes1 && scopes1[str] !== scopes2[str]) {
				return false;
			}
		}
		return true;
	}

	// function return an object in format: {'str1': rank, 'str2':, rank, ...}
	function processString(s) {
		let rank = 0;
		const res = {};
		let sub = '';
		for (let i = 0; i < s.length; i++) {
			if (!/[a-z }{]/.test(s[i])) return false;
			if (s[i] === '{') {
				if (sub) res[sub] = rank;
				rank++;
				sub = '';
			} else if (s[i] === '}') {
				if (sub) res[sub] = rank;
				rank--;
				sub = '';
			} else if (/[a-z]/.test(s[i])) {
				sub += s[i];
			}
			if (i === s.length - 1) {
				if (sub) res[sub] = rank;
			}
		}
		return res;
	}
}

console.log(scope_congruent(['{a{bc{def}{hij}}aac}', 'a{bc{{def}g{hij}}']));
