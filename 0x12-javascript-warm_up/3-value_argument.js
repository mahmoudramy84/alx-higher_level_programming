#!/usr/bin/node
// console.log(process.argv[2] ? process.argv[2] : 'No argument');
const secondArgument = process.argv[2];
if (secondArgument) {
  console.log(secondArgument);
} else {
  console.log('No argument');
}
