#!/usr/bin/node

const request = require('request');
const episodeNumber = process.argv[2];
const apiEndpoint = `https://swapi-api.hbtn.io/api/films/${episodeNumber}`;

request.get(apiEndpoint, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  const movieTitle = JSON.parse(body).title;
  console.log(movieTitle);
});
