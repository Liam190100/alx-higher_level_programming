#!/usr/bin/node

exports.addMeMaybe = function (agrs, theFunction) {
  theFunction(++agrs);
};
