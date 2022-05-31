var addTwoNumbers = function (l1, l2) {
	// add the two nodes values
	// store sum in new list and keep the carry
	// walk through the lists and do the same
	// create list head
	let sumList = new ListNode((l1.val + l2.val) % 10);
	// store carry-on
	let carry = Math.floor((l1.val + l2.val) / 10);
	// walkers for the two lists
	let w1 = l1.next;
	let w2 = l2.next;
	// walker for the sum list
	let s = sumList;
	// loop through the lists
	while (w1 || w2 || carry) {
		let sum = 0;
		// create a new node
		s.next = new ListNode(0);
		s = s.next;
		// calculate value and carry
		if (w1) {
			sum += w1.val;
			w1 = w1.next;
		}
		if (w2) {
			sum += w2.val;
			w2 = w2.next;
		}
		if (carry) {
			sum += carry;
		}
		carry = Math.floor(sum / 10);
		// store value in current sum list
		s.val = sum % 10;
	}

	return sumList;
};
