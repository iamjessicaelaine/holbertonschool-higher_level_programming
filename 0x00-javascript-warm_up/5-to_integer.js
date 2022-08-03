#!/usr/bin/node
const process = require('process');
const convertedArg = parseInt(process.argv[2]);
if (isNaN(convertedArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convertedArg);
}
