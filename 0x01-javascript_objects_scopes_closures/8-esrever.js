#!/usr/bin/node
exports.esrever = function (list) {
  let reverse = [];
  for (let index = list.length - 1; index >= 0; index--) {
    reverse.push(list[index]);
  }
  return reverse;
};
