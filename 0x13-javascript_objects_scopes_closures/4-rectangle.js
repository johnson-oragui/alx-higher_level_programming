#!/usr/bin/node

// using the class notation for defining class
module.exports = class Rectangle {
  // The constructor take 2 arguments: w and h
  constructor (w, h) {
    // If w or h is equal to 0 or not a positive integer, create an empty object
    if (w > 0 && h > 0) {
      // Initializing the instance attribute width with the value of w
      // Initializing the instance attribute height with the value of h
      [this.width, this.height] = [w, h];
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
