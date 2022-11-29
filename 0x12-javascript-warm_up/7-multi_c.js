#!/usr/bin/node

const myNum = parseInt(process.argv[2], 10);
if (isNaN(myNum)) {
	console.log('Missing number of occurrences');
} else {
	for (let i = 1; i <= myNum; i++) {
		console.log('C is fun');
	}
}
