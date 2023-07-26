#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

// Fetch todo tasks data
request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const todoData = JSON.parse(body);

    const completedTasks = {}; // Object to store the count of completed tasks for each user

    // Loop through the tasks and count completed tasks for each user
    todoData.forEach((task) => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 1;
        } else {
          completedTasks[task.userId]++;
        }
      }
    });

    console.log(`{${Object.entries(completedTasks).map(([key, value]) => ` '${key}': ${value}`).join(",\n ")} }`);
  } else {
    console.error('Error fetching todo data:', error);
  }
});

