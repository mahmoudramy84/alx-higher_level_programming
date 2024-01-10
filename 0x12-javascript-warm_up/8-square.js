#!/usr/bin/node
const x = process.argv[2];
for (let row = 0; row < x; row++) {
  let square = '';
  for (let colm = 0; colm < x; colm++) {
    square += 'X';
  }
  console.log(square);
}
