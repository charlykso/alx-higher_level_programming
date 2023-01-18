#!/usr/bin/node

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const request = require('request');
request.get(url + movieId, function (err, res, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(data).title);
  }
});
