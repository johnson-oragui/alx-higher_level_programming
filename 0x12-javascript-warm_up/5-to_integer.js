#!/usr/bin/node

const arg2 = process.argv[2];
const parsedNumber = parseInt(arg2);

if (isNaN(parsedNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parsedNumber}`);
}
