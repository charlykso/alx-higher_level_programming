#!/usr/bin/node

exports.esrever = function (list) {
  let x = 0;
  let y = list.length - 1;
  let temp = 0;
  while (x <= y) {
    temp = list[x];
    list[x] = list[y];
    list[y] = temp;
    x++;
    y--;
  }
  return list;
};
