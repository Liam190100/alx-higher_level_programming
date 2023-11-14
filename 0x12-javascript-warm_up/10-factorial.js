#!/usr/bin/node

const number = process.argv[2];

function factol (number) {
  if (number <= 1 || isNaN(number)) {
    return 1;
  } else {
    return number * factol(number - 1);
  }
}

console.log(factol(number));
