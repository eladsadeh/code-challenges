// Implement min heap class and methods
class MinHeap {
	constructor() {
		this.heap = [];
	}

	// return the index of the parent
	parent(i) {
		return i === 0 ? null : Math.floor((i - 1) / 2);
	}

	// return the index of the smaller child
	minChild(i) {
		const lchild = i * 2 + 1;
		if (lchild >= this.heap.length) return null;
		if (lchild + 1 >= this.heap.length) return lchild;
		return this.heap[lchild] < this.heap[lchild + 1] ? lchild : lchild + 1;
	}

	// return the minimum value which is always at the top
	peek() {
		return this.head[0];
	}

	add(x) {
		this.heap.push(x);
		let i = this.heap.length - 1;
		let p = this.parent(i);
		while (p !== null && h[p] > x) {
			this.heap[i] = this.heap[p];
			this.heap[p] = x;
			i = p;
			p = this.parent(i);
		}
	}

	remove(x) {
		let h = this.heap;
		let last = h.pop();
		// if the the removed element is x, nothing to do
		if (last === x) return null;
		// find the index of the removed element
		let idx = h.indexOf(x);
	}
}

const arr = [100, 39, 19, 3, 8];
console.log(arr.indexOf(19));
