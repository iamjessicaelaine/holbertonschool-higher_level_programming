#!/usr/bin/node
const process = require('process');
const squaresize = parseInt(process.argv[2]);
let rowcount = 0;
if (!isNaN(squaresize)) {
  const character = 'X';
  const eachrow = character.repeat(squaresize);
  while (rowcount < squaresize) {
    console.log(eachrow);
    rowcount++;
  }
} else {
  console.log('Missing size');
}
