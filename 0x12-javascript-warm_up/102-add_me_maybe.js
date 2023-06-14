#!/usr/bin/node
const addMeMaybe = (number, theFunction) => {
  number++;
  theFunction(number);
};

module.exports.addMeMaybe = addMeMaybe;
