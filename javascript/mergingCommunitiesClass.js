class Person {
	constructor(n) {
		this.n = n
		this.parent = this
		this.size = 1
	}
}

function mergingCommunities(n, queries) {
	const people = [];
	for (let i = 0; i < n; i++) {
		people.push(new Person(i));
	}

	function findRoot(person) {
		while (person !== person.parent) {
			person.parent = person.parent.parent
			person = person.parent
		}
		return person
	}

	for (let query of queries) {
		let q = query.split(' ');
		if (q[0] === 'Q') {
			const r = findRoot(people[Number(q[1]) - 1]);
			console.log('size:', r.size);
		} else if (q[0] === 'M') {
			console.log(q);
			const r1 = findRoot(people[Number(q[1]) - 1]);
			const r2 = findRoot(people[Number(q[2]) - 1]);
			if (r1 != r2) {
				r2.parent = r1;
				r1.size += r2.size;
				// console.log('merge:', people);
			}
		}
	}
}

mergingCommunities(5, [
	'Q 1',
	'M 1 2',
	'Q 2',
	'M 2 3',
	'M 4 5',
	'Q 3',
	'Q 2',
	'M 1 4',
	'Q 1',
	'Q 5',
]);
