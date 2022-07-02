// HTTP request from server (Node.js)
async function fetchData(url) {
	const https = require('https');
	return new Promise((resolve, reject) => {
		https
			.get(url, (response) => {
				let data = '';
				// console.log(response);
				response.on('data', (stream) => {
					data += stream;
					// console.log(data);
				});
				response.on('end', () => {
					const resolvedData = JSON.parse(data);
					resolve(resolvedData);
				});
			})
			.on('error', (err) => {
				reject(err);
			});
	});
}

async function showData(key) {
	const baseUrl = `https://jsonmock.hackerrank.com/api/moviesdata/search/?Title=`;
	const res = await fetchData(`${baseUrl}${key}`);
	// console.log(res.data);
}

showData('maze');
