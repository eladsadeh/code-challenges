function processLogs(logs, maxSpan) {
	let users = {};
	let result = [];
	// prepare object with in/out for each user
	logs.forEach((log) => {
		let [id, time, activity] = log.replace('-', '').split(' ');
		users[id] = { ...users[id], [activity]: time };
	});
	Object.keys(users).forEach((user) => {
		if (users[user].signout - users[user].signin <= maxSpan) {
			result.push(user);
		}
	});
	console.log(result.sort((a, b) => a - b));
}

// processLogs(
// 	[
// 		'99 2 sign-out',
// 		'100 10 sign-in',
// 		'50 20 sign-in',
// 		'100 15 sign-out',
// 		'50 26 sign-out',
// 		'99 1 sign-in',
// 	],
// 	5
// );

function find_meeting_slots(num_slots, employee_schedules) {
	let slots = [];
	// initialize calendar array consist of a slot for every 15 minutes
	// time is converted into an index in the calendar array
	let calendar = new Array(96).fill(employee_schedules.length);
	function timeToIndex(time) {
		const [hour, minutes] = time.split(':');
		return Number(hour) * 4 + Number(minutes) / 15;
	}
	function indexToTime(index) {
		const hour = Math.floor(index / 4);
		const minutes = (index % 4) * 15;
		return `${hour}`.padStart(2, '0') + ':' + `${minutes}`.padStart(2, '0');
	}
	// process employee shedule and reduce the number of available employees
	employee_schedules.forEach((employee) => {
		employee.forEach((schedule) => {
			console.log(schedule);
			const [start, end] = schedule.split('-').map((time) => timeToIndex(time));
			// if the employee is not available reduce the availabilty
			for (let i = start; i <= end; i++) {
				calendar[i]--;
			}
		});
	});
	// process that calendar to find slots with 2 or more participants
	let start = '';
	for (let i = 0; i < calendar.length; i++) {
		if (!start && calendar[i] > 1) {
			// No start time and more than 2 available
			start = indexToTime(Math.max(i - 1, 0));
		} else if (start && calendar[i] !== calendar[i - 1]) {
			// start time and different number available
			if (calendar[i] > 1) {
				// end of slot, start a new slot
				slots.push({
					slot: `${start}-${indexToTime(i)}`,
					participants: calendar[i - 1],
				});
				start = indexToTime(Math.max(i, 0));
			} else {
				// end of slot
				slots.push({
					slot: `${start}-${indexToTime(i)}`,
					participants: calendar[i - 1],
				});
				start = '';
			}
		} else if (start && i === calendar.length - 1) {
			slots.push({ slot: `${start}-24:00`, participants: calendar[i - 1] });
		}
	}
	slots.sort((a, b) => b.participants - a.participants);
	console.log('slots:', slots.slice(0, num_slots - 1));
	let res = slots.map((s) => s.slot);
	console.log(res.slice(0, num_slots - 1));

	// console.log(num_slots, employee_schedules);
}

find_meeting_slots(3, [
	['08:00-12:30', '17:00-22:00'],
	['07:00-14:30', '16:00-19:00'],
	['08:00-14:30', '17:00-19:00'],
]);
