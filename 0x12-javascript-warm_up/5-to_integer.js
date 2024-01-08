#!/usr/bin/node
// console.log(parseInt(process.argv[2]) ? `My number: ${parseInt(process.argv[2])}` : 'Not a number');
const num = process.argv[2];
if (parseInt(num)) {
  console.log('My number: ' + parseInt(num));
} else {
  console.log('Not a number');
}
