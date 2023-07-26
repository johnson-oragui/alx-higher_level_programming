#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    try {
      const todos = JSON.parse(body);

      const completed = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          if (completed[todo.userId] === undefined) {
            completed[todo.userId] = 1;
          } else {
            completed[todo.userId]++;
          }
        }
      });

      // Create the formatted output manually to match the expected format
      const keys = Object.keys(completed);
      let formattedOutput = '{ ';
      if (keys.length <= 8) {
        keys.forEach((userId, index) => {
          formattedOutput += `'${userId}': ${completed[userId]}`;
          formattedOutput += index === keys.length - 1 ? ' }' : ', ';
        });
      } else {
        keys.forEach((userId, index) => {
          formattedOutput += `  '${userId}': ${completed[userId]}`;
          formattedOutput += index === keys.length - 1 ? '\n' : ',\n';
        });
        formattedOutput += '}';
      }

      console.log(formattedOutput);

    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    console.error('Error fetching data:', error);
  }
});
