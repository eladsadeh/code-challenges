// Search string array 'P' if it found within
// grid array G
function gridSearch(G, P) {
	// regex for the first pattern row with overlapping matches (lookahead)
	const first = new RegExp(`(?=${P[0]})`, 'g');
	// loop over grid rows
	for (let i = 0; i <= G.length - P.length; i++) {
		// find all matches with first pattern row in current grid row
		let matches = G[i].matchAll(first);
		// IF found matches of first row, check each match
		if (matches) {
			for (let match of matches) {
				if (patternFoundAt(i, match.index)) return 'YES';
			}
		}
	}
	return 'NO';

	function patternFoundAt(startRow, startIdx) {
		// check if the pattern exist in grid starting from 'startRow' and 'startIdx'
		for (let j = 1; j < P.length; j++) {
			if (G[startRow + j].slice(startIdx, startIdx + P[j].length) !== P[j])
				return false;
		}
		return true;
	}
}
