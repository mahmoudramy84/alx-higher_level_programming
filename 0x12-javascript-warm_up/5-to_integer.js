#!/usr/bin/node
const argument = process.argv[2];

const number = +argument;

if (!isNaN(number) && Number.isInteger(number)) {
  console.log('My number:', number);
} else {
  console.log('Not a number');
}
