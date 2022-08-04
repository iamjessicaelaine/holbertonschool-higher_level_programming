#!/usr/bin/node
const twinSquare = require('./5-square.js');

class Square extends twinSquare {
  charPrint (c) {
    let character = c;
    if (c === undefined) {
      character = 'X';
    }
    const eachrow = character.repeat(this.width);
    let rowcount = 0;
    while (rowcount < this.height) {
      console.log(eachrow);
      rowcount++;
    }
  }
}
module.exports = Square;
