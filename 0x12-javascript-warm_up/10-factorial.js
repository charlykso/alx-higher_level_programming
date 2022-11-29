#!/usr/bin/node

const x = parseInt(process.argv[2], 10);
function fact(a) {
	if (a === 1) {
		return 1;
	}
	if (isNaN(a)) {
		return 1;
	}
	return (a * fact(a - 1));
}
console.log(fact(x));
