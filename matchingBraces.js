function matchingBraces(braces) {
	const ans = [];
	for (let brace of braces) {
		let match = brace.match(/(\{\}|\(\)|\[\])/);
		while (match) {
			brace = brace.replace(match[0], '');
			match = brace.match(/(\{\}|\(\)|\[\])/);
		}
		if (brace.length > 0) ans.push('NO');
		else ans.push('YES');
	}
	return ans;
}


console.log(matchingBraces(['[{}]', '[{]}', '{([])}']));
