// https://www.hackerrank.com/challenges/nim-game-1/problem
// Theory: https://en.wikipedia.org/wiki/Nim
function nimGame(pile) {
	return pile.reduce((xor, hight) => (xor ^= hight)) ? 'First' : 'Second';
}
