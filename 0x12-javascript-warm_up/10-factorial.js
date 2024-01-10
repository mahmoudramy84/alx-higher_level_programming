#!/usr/bin/node
const facNum = parseInt(process.argv[2]);
function factorial (facNum) {
  if (facNum === 0 || isNaN(facNum)) {
    return 1;
  } else {
    return (facNum * factorial(facNum - 1));
  }
// return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
}
console.log(factorial(facNum));
