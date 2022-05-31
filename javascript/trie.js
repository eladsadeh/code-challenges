class SimpleTrie {
	// create empty dictionary
	constructor() {
		this.trie = {};
	}
	// if prefix is found return true
	// otherwise add the string to trie and return false
	check_prefix(s) {
		// pointer to current node (walker)
		let w = this.trie;
		let chars = s.split('');
		for (let i = 0; i < chars.length; i++) {
			const c = chars[i];
			// if current character is not in current node
			// add it as either end of word or empty dictionary
			if (!Object.keys(w).includes(c))
				w[c] = i == chars.length - 1 ? 'eow' : {};
			// else return true if it's end of word or the last character.
			else if (w[c] === 'eow' || i === chars.length - 1) return true;
			w = w[c]; // set walker to current node
		}
		return false;
	}
}

function noPrefix(words) {
	const trie = new SimpleTrie();
	for (const word of words) {
		if (trie.check_prefix(word)) {
			console.log('BAD SET');
			console.log(word);
			return;
		}
	}

	console.log('GOOD SET');
}

noPrefix(['aab', 'bcd', 'aabgab']);
noPrefix(['acb', 'defgab', 'abcde', 'aabcde', 'bbbbbbbbbb', 'jabjjjad']);
