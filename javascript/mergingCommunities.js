// class Node:
//     def __init__(self, data):
//         self.data = data
//         self.parent = self
//         self.rank = 0
//         self.size = 1

// class DSF:
//     @staticmethod
//     def make_set(data):
//         return Node(data)

//     @staticmethod
//     def find(node):
//         # retrun the top level parent
//         if node != node.parent:
//             node.parent = DSF.find(node.parent)
//         return node.parent

//     @staticmethod
//     def union(node_a, node_b):
//         root_a = DSF.find(node_a)
//         root_b = DSF.find(node_b)

//         if root_a != root_b:
//             if root_a.rank > root_b.rank:
//                 root_b.parent = root_a
//                 root_a.size += root_b.size
//             else:
//                 root_a.parent = root_b
//                 root_b.size += root_a.size
//                 if root_a.rank == root_b.rank:
//                     root_b.rank += 1

// # N, Q = map(int, input().split())
// # # Initialize array of people for 1 - N
// # people = [DSF.make_set(i) for i in range(1, N+1)]
// # print(people)
// # for _ in range(Q):
// #     inputs = input().split()
// #     if inputs[0] == 'Q':
// #         I = int(inputs[1])
// #         print(DSF.find(people[I-1]).size)
// #     elif inputs[0] == 'M':
// #         I, J = map(int, inputs[1:])
//         # DSF.union(people[I-1], people[J-1])

function mergingCommunities(n, queries) {
	const people = [];
	for (let i = 0; i < n; i++) {
		people.push({ parent: i, n: i, size: 1 });
	}

	function parent_index(n) {
		while (people[n].parent != people[n].n) {
			people[n].parent = people[people[n].parent].parent;
			n = people[n].parent;
			console.log('lookup:', people);
		}
		return n;
	}

	for (let query of queries) {
		let q = query.split(' ');
		if (q[0] === 'Q') {
			const n = parent_index(Number(q[1]) - 1);
			console.log('size:', people[n].size);
		} else if (q[0] === 'M') {
			console.log(q);
			const p1 = parent_index(Number(q[1]) - 1);
			const p2 = parent_index(Number(q[2]) - 1);
			if (p1 != p2) {
				people[p2].parent = people[p1].parent;
				people[p1].size += people[p2].size;
				console.log('merge:', people);
			}
		}
	}
}

mergingCommunities(5, [
	'Q 1',
	'M 2 1',
	'Q 2',
	'M 2 3',
	'M 4 5',
	'Q 3',
	'Q 2',
	'M 3 4',
	'Q 1',
	'Q 5',
]);
