#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const eachItem of list) {
    if (eachItem === searchElement) {
      counter++;
    }
  }
  return counter;
};
