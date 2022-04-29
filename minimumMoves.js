function minimumMoves(grid, startRow, startCol, goalRow, goalCol) {
	// initialize a 2d matrix to track visited nodes and its parents
	console.log(grid);
	const n = grid.length;
	const visited = Array(n)
		.fill(false)
		.map((_) =>
			Array(n)
				.fill(false)
				.map((_) => ({ v: false, p: null }))
		);
	// Mark the start point as visited
	// but leave the parent as null
	visited[startRow][startCol].v = true;
	// Start from the start point
	const Queue = [[startRow, startCol]];
	// const Queue = [startCol];
	// explore all directions
	function exploreNeighbours(row, col) {
		// down, up, left, right directon vectors
		const dir = [
			[-1, 0],
			[1, 0],
			[0, -1],
			[0, 1],
		];
		// for each direction
		for (let i = 0; i < 4; i++) {
			let rr = row;
			let cc = col;
			let [dr, dc] = dir[i];
			while (true) {
				rr += dr;
				cc += dc;
				// stop at out of bounderies or is blocked
				if (
					cc < 0 ||
					rr < 0 ||
					rr > n - 1 ||
					cc > n - 1 ||
					grid[rr][cc] === 'X'
				)
					break;
				// if point was not visited before
				// mark as visited and store the parent
				// in the queue
				if (!visited[rr][cc].v) {
					Queue.push([rr, cc]);
					visited[rr][cc].v = true;
					visited[rr][cc].p = [row, col];
				}
			}
		}
	}
	let moves = 0;
	let parent = null;
	while (Queue.length !== 0) {
		const [row, col] = Queue.shift();
		// If its the end point, stop exploring
		// and set the first point to the parent
		// of the end point.
		// (first step back toward to the start point)
		if (row === goalRow && col === goalCol) {
			parent = visited[row][col].p;
			break;
		}
		// Explore all possible movements from the
		// current point
		exploreNeighbours(row, col);
	}
	// When parent === null, we made it to the start point.
	while (parent !== null) {
		// increment moves counter and set the next
		// point to the parent of current point
		moves++;
		parent = visited[parent[0]][parent[1]].p;
	}

	return moves;
}

console.log(
	minimumMoves(['..X..', '....X', 'XX.X.', '.....', '.X..X'], 4, 0, 0, 4)
);
