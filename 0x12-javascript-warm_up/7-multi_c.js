#!/usr/bin/node

const argument = process.argv[2];
const x = +argument;

if (!isNaN(x) && Number.isInteger(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
