// leetcode.com/problems/longest-substring-without-repeating-characters/
https: var lengthOfLongestSubstring = function (s) {
	if (s === '') return 0;
	cMap = {};
	p = -1;
	max = 0;
	for (let i = 0; i < s.length; i++) {
		c = s[i];
		if (cMap[c] !== undefined && p < cMap[c]) {
			// if c in the current substring, update the pointer
			p = cMap[c];
		} else {
			// else, update max
			max = max < i - p ? i - p : max;
		}
		cMap[c] = i;
	}

	return max;
};

console.log(lengthOfLongestSubstring(''));
