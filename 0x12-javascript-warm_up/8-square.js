#!/usr/bin/node

const myNum = parseInt(process.argv[2], 10);
if (isNaN(myNum)) {
	console.log('Missing size');
} else {
	for (let i = 1; i <= myNum; i++) {
		console.log('X'.repeat(myNum));
	}
}
