#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request.get(url, function (err, res, data) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const dic = {};
    const tasks = JSON.parse(data);
    for (const i in tasks) {
      if (tasks[i].completed) {
        if (dic[tasks[i].userId] === undefined) {
          dic[tasks[i].userId] = 1;
        } else {
          dic[tasks[i].userId]++;
        }
      }
    }
    console.log(dic);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
