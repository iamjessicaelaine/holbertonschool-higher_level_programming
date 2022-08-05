#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const fileData = process.argv[3];
fs.writeFile(filePath, fileData, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
