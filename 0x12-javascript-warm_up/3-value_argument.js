#!/usr/bin/node

const firstArgument = process.argv[2];

if (typeof firstArgument === 'undefined') {
    console.log("No argument");
} else {
    console.log(firstArgument);
}
