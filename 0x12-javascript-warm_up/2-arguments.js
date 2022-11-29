#!/usr/bin/node

const count = process.argv.length;
if (count >= 3) {
  if (count === 3) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
} else {
  console.log('No argument');
}
