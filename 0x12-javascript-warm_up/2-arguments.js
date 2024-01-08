#!/usr/bin/node
const numArguments = process.argv.length ;
if (numArguments === 2) {
  console.log('No argument');
} else if (numArguments === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
