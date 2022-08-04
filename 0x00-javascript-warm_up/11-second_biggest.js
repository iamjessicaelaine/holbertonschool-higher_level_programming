#!/usr/bin/node
// sort arg vector in order
const cmdArgs = process.argv.slice(2);
const sortedArgs = cmdArgs.sort(function (a, b) { return a - b; });
const argCount = sortedArgs.length;
if (argCount === 0 || argCount === 1) {
  console.log(0);
} else {
  const topTwo = sortedArgs.slice(-2);
  console.log(topTwo[0]);
}
