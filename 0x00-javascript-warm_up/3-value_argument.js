#!/usr/bin/node
const process = require('process');
const firstArg = process.argv[2];
if (firstArg) {
  console.log(firstArg);
} else {
  console.log('No argument');
}
