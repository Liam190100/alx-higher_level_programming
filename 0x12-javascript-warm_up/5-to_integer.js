#!/usr/bin/node
const myArgs = process.argv.slice(2);
const firstArg = myArgs[0];

if (isNaN(parseInt(firstArg))) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(firstArg));
}
