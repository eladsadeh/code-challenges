var isAnagram = function (s, t) {
	if (s.length !== t.length) return false;
	let sCnt = {};
	let tCnt = {};
	for (let i = 0; i < s.length; i++) {
		if (sCnt[s[i]]) sCnt[s[i]]++;
		else sCnt[s[i]] = 1;
		if (tCnt[t[i]]) tCnt[t[i]]++;
		else tCnt[t[i]] = 1;
	}
	for (c of Object.keys(sCnt)) {
        console.log(c, sCnt[c], tCnt[c]);
		if (tCnt[c] === undefined || tCnt[c] !== sCnt[c]) return false;
	}
	return true;
};

console.log(isAnagram('rat', 'car'));
