#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
// Asynchronous version of readfile method
fs.readFile(filePath, 'utf-8', (error, data) => {
  // if the file doesn't exist then there is error so...
  if (error) {
    // print the error object
    console.log(error);
  } else {
    // print contents of file stored in data as directed in callback
    console.log(data);
  }
});
