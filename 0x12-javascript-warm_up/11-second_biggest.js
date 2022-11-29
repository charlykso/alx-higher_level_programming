#!/usr/bin/node

function compare (a, b) {
  return (b - a);
}
const myArg = process.argv.length;
if (myArg <= 3) {
  console.log(0);
} else {
  console.log(process.argv.slice(2).sort(compare)[1]);
}
