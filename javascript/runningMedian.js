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
		return this.heap[0];
	}
	size() {
		return this.heap.length;
	}
	heapadd(x) {
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
	// return the top element
	heappop() {
		let h = this.heap;
		if (h.length === 0) return null;
		let top = h[0];
		let last = h.pop();
		// if the the last element is x, nothing to do
		if (last === top) return top;
		// find the index of the removed element
		let idx = 0;
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
		return top;
	}
}

function runningMedian(a) {
	// insert number to either bigger or smaller heaps
	function insert(num, bigger, smaller) {
		if (num > bigger.peek()) {
			if (bigger.size() > smaller.size()) {
				// if there are more numbers in the bigger heap, move
				// the smallest to the smaller heap and add the new num
				smaller.heapadd(-bigger.heappop());
			}
			bigger.heapadd(num);
		} else {
			// add the number to the smaller heap, and check that the heaps
			// are balanced, correct if needed
			smaller.heapadd(-num);
			if (smaller.size() - bigger.size() > 1) {
				bigger.heapadd(-smaller.heappop());
			}
		}
	}
	// return the median
	function getMedian(bigger, smaller) {
		if (bigger.size() == smaller.size())
			return (bigger.peek() - smaller.peek()) / 2;
		else if (bigger.size() > smaller.size()) return bigger.peek();
		else return -smaller.peek();
	}

	// Create heaps for bigger and smaller numbers
	// initialize the bigger heap with the first number
	let bigger = new MinHeap();
	let smaller = new MinHeap();
	bigger.heapadd(a.shift());
	// array of meadians initialzed with the first element
	const medians = [bigger.peek().toFixed(1)];

	for (let num of a) {
		insert(num, bigger, smaller);
		medians.push(getMedian(bigger, smaller).toFixed(1));
	}
	return medians;
}
