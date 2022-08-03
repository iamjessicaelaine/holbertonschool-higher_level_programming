#!/usr/bin/node
// include process module
const process = require('process');
// assign arg array to a variable
const args = process.argv;
// get # of args for script logic
const argsCount = args.length - 2;
if (argsCount > 0) {
  if (argsCount === 1) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
} else {
  console.log('No argument');
}
