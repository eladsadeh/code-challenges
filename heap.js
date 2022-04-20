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
	smallerChild(i) {
		const lchild = i * 2 + 1;
		// if there is no childs, return null
		if (lchild >= this.heap.length) return null;
		// if there is no right child, return the left child
		if (lchild + 1 >= this.heap.length) return lchild;
		// else, return the smaller child
		return this.heap[lchild] < this.heap[lchild + 1] ? lchild : lchild + 1;
	}

	// return the minimum value which is always at the top
	peek() {
		console.log(this.heap[0]);
	}

	add(x) {
		// add x to the end of the heap
		this.heap.push(x);
		// go up the heap and find the right location for x
		let i = this.heap.length - 1;
		let p = this.parent(i);
		// while the parent is bigger, swap them
		while (p !== null && this.heap[p] > x) {
			this.heap[i] = this.heap[p];
			this.heap[p] = x;
			i = p;
			p = this.parent(i);
		}
	}

	remove(x) {
		let h = this.heap;
		let last = h.pop();
		// if the the last element is x, nothing to do
		if (last === x) return null;
		// find the index of the removed element
		let idx = h.indexOf(x);
		// replace the removed element with the last element
		this.heap[idx] = last;
		// now we need to find the correct placement for the last element
		let child = this.smallerChild(idx); // index of smaller child
		while (child !== null && this.heap[child] < last) {
			// the child element is smaller then the last element
			// swap them
			this.heap[idx] = this.heap[child];
			this.heap[child] = last;
			// and check the next child
			idx = child;
			child = this.smallerChild(idx);
		}
	}
}

function processData(input) {
	let lines = input.split('\n');
	let h = new MinHeap();
	lines.shift();
	// process instructions
	for (line of lines) {
		const [inst, val] = line.split(' ');
		if (inst === '1') h.add(Number(val));
		else if (inst === '2') h.remove(Number(val));
		else h.peek();
	}
}
