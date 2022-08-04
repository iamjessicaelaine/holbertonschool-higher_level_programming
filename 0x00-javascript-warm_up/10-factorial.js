#!/usr/bin/node
// cast string arg into integer
const firstArg = Number(process.argv[2]);
console.log(factorial (firstArg));

// going tot test hoisting out
function factorial (n) {
    // base case
    if (n === NaN) {
	return 1;
    } else if (n === 0 || n === 1) {
	return 1;
    } else {
	return n * factorial (n - 1);
    }
}


// firstArg = parseInt(process.argv[2]);
// console.log(factorial (firstArg));
