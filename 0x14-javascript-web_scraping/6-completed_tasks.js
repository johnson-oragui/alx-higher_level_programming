#!/usr/bin/node

const request = require('request');

// Get the API URL from the first command-line argument
const apiUrl = process.argv[2];

// Use the 'request' module to perform an HTTP GET request
request(apiUrl, function (error, response, body) {
  // Check if there was no error during the HTTP request
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    // Create an empty object to store the count of completed tasks for each user ID.
    const completedTasksByUserId = {};
    // Iterate through each todo in the 'todos' array.
    todos.forEach((todo) => {
      if (todo.completed) {
        if (completedTasksByUserId[todo.userId] === undefined) {
          completedTasksByUserId[todo.userId] = 1;
        } else {
          completedTasksByUserId[todo.userId] += 1;
        }
      }
    });

    console.log(completedTasksByUserId);
  } else {
    console.error('Error:', error);
  }
});
