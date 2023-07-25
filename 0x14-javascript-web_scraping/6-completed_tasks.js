#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Use the 'request' module to perform an HTTP GET request to the URL
request(process.argv[2], function (error, response, body) {
  // Check if there was no error during the HTTP request.
  if (!error) {
    // parse the JSON data using 'JSON.parse()'
    const todos = JSON.parse(body);

    // Create an empty object 'completed' to store the count of completed todos for each user ID.
    const completed = {};

    // Iterate through each todo in the 'todos' array.
    todos.forEach((todo) => {
      if (todo.completed && completed[todo.userId] === undefined) {
        completed[todo.userId] = 1;
      } else if (todo.completed) {
        completed[todo.userId] += 1;
      }
    });
    console.log(completed);
  }
});
