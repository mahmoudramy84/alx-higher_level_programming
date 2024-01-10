#!/usr/bin/node
const x = process.argv[2];
if (parseInt(x)) {
  for (let row = 0; row < x; row++) {
    let square = '';
    for (let colm = 0; colm < x; colm++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
