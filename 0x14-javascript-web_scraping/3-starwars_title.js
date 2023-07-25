#!/usr/bin/node

// Import the 'request' module.
const request = require('request');

// Construct the URL for the specific Star Wars film
let url = 'http://swapi.co/api/films/' + process.argv[2];

// Use the 'request' module to perform an HTTP GET request to the constructed URL.
request(url, function (error, response, body) {

  // log title if successful, log error if not.
  console.log(error || JSON.parse(body).title);
});
