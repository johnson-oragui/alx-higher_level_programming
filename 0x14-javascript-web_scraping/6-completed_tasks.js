#!/usr/bin/node

const request = require('request');

// Function to compute the number of completed tasks by user ID
function countCompletedTasks(todos) {
  const completedTasksByUser = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      const userId = todo.userId;
      completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
    }
  });

  return completedTasksByUser;
}

// Main function to fetch data and compute the completed tasks
function fetchAndComputeCompletedTasks(apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const todos = JSON.parse(body);
      const completedTasksByUser = countCompletedTasks(todos);

      console.log(completedTasksByUser);
    } else {
      console.error('Error fetching data:', error);
    }
  });
}

const apiUrl = process.argv[2];
fetchAndComputeCompletedTasks(apiUrl);
