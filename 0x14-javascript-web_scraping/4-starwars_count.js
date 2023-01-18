#!/usr/bin/node

const url = process.argv[2];
const ID = 18;
const request = require('request');
request(url, function (err, res, data) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const films = JSON.parse(data).results;
    let count = 0;
    for (const i in films) {
      const chars = films[i].characters;
      for (const c in chars) {
        if (chars[c].includes(ID)) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Erorr Code:' + res.statusCode);
  }
});
