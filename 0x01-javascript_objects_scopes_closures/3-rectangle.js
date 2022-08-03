#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // space needed between class members
  print () {
    const character = 'X';
    const eachrow = character.repeat(this.width);
    let rowcount = 0;
    while (rowcount < this.height) {
      console.log(eachrow);
      rowcount++;
    }
  }
}
module.exports = Rectangle;
