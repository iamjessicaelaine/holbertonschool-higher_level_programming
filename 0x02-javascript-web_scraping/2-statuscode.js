#!/usr/bin/node
const request = require('request');
const urlArg = process.argv[2];
request.get(urlArg, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  console.log(`code: ${response.statusCode}`);
});
