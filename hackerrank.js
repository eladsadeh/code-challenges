function bomberMan(n, grid) {
	// in the first second nothing happen
	if (n < 2) return grid;
	if (!(n % 2)) {
		// In every even N, the grid is full of bombs
		return new Array(grid.length).fill('O'.repeat(grid[0].length));
	}
	// On the 3rd second, and every 4 second after that, the state is the first explosion
	const firstExposion = explodeGrid(grid);
	if (n % 4 === 3) return firstExposion;
	// On the 5th second, and every 4 second after that, the state is the second explosion
	if (n % 4 === 1) return explodeGrid(firstExposion);

	// function take a grid and return a grid after explosion
	function explodeGrid(grid) {
		// Max row/column indexes
		const y = grid[0].length - 1;
		const x = grid.length - 1;
		// create array of original grid
		const gridArr = grid.map((r) => r.split(''));
		const exploded = gridArr.reduce((acc, row, r) => {
			const line = row.reduce((l, el, c) => {
				// find the elements in the array that are 'O' or near 'O'
				if (
					gridArr[r][c] === 'O' ||
					gridArr[Math.min(r + 1, x)][c] === 'O' ||
					gridArr[Math.max(r - 1, 0)][c] === 'O' ||
					gridArr[r][Math.min(c + 1, y)] === 'O' ||
					gridArr[r][Math.max(c - 1, 0)] === 'O'
				)
					return l + '.';
				else return l + 'O';
			}, '');
			// add the line to the new grid
			acc.push(line);
			return acc;
		}, []);
		return exploded;
	}
}

console.log(
	bomberMan(3, [
		'.......',
		'...O...',
		'....O..',
		'.......',
		'OO.....',
		'OO.....',
	])
);
