#!/usr/bin/node

const filename = process.argv[2];
const StringToWrite = process.argv[3];
const fs = require('fs');
fs.writeFile(filename, StringToWrite, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
