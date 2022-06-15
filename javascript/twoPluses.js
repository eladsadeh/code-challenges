// https://www.hackerrank.com/challenges/two-pluses/problem
function twoPluses(grid) {
	const x = grid[0].length; // number of columns
	const y = grid.length; // number of rows
	const pluses = []; // array to hold pluses [area, x, y]
	// iterate through array
	for (let r = 0; r < y; r++) {
		for (let c = 0; c < x; c++) {
			if (grid[r][c] === 'G') {
				// add plus size 1
				pluses.push([1, r, c]);
				// maximum possible length from center
				const maxLength = Math.min(r, y - 1 - r, c, x - c - 1);
				let i = 1;
				while (i <= maxLength) {
					// if pluse size i, add to array and keep checking
					if (isPlus(grid, r, c, i)) {
						pluses.push([1 + i * 4, r, c]);
						i++;
					} else break;
				}
			}
		}
	}

	// iterate through pluses and if they are not overlap
	// keep maximum multipication of two pluses
	let ans = 1;
	for (let i = 0; i < pluses.length; i++) {
		for (let j = i + 1; j < pluses.length; j++) {
			if (!isOverlap(pluses[i], pluses[j])) {
				ans = Math.max(ans, pluses[i][0] * pluses[j][0]);
			}
		}
	}

	return ans;

	// return true if it's a plus
	function isPlus(grid, r, c, i) {
		return (
			(grid[r - i][c] === 'G') & (grid[r + i][c] === 'G') &&
			grid[r][c - i] === 'G' &&
			grid[r][c + i] === 'G'
		);
	}
	// return true of two pluses overlap
	function isOverlap(p1, p2) {
		// two pluses with area 1 can't overlap
		if (p1[0] === 1 && p2[0] === 1) return false;
		const rowDiff = Math.abs(p1[1] - p2[1]);
		const colDiff = Math.abs(p1[2] - p2[2]);
		const l1 = Math.ceil(p1[0] / 4);
		const l2 = Math.ceil(p2[0] / 4);
		if (!rowDiff && colDiff + 1 < l1 + l2) return true;
		if (!colDiff && rowDiff + 1 < l1 + l2) return true;
		if (rowDiff < Math.min(l1, l2) && colDiff < Math.max(l1, l2)) return true;
		if (colDiff < Math.min(l1, l2) && rowDiff < Math.max(l1, l2)) return true;
		return false;
	}
}

console.log(twoPluses(['GGGGGG', 'GBBBGB', 'GGGGGG', 'GGBBGB', 'GGGGGG']));
console.log(
	twoPluses(['GGGGGGG', 'BGBBBBG', 'BGBBBBG', 'GGGGGGG', 'GGGGGGG', 'BGBBBBG'])
);
