#!/usr/bin/node

const arg2 = process.argv[2];
const x = parseInt(arg2);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
