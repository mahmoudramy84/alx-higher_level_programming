#!/usr/bin/node

const argument1 = process.argv[2];
const argument2 = process.argv[3];

const num1 = parseInt(argument1);
const num2 = parseInt(argument2);

if (!isNaN(num1) && !isNaN(num2)) {
  console.log(num1 + num2);
} else {
  console.log('Please provide two valid integer arguments.');
}
