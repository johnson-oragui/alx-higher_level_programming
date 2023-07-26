#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    try {
      const todos = JSON.parse(body);

      const completed = {};

      todos.forEach((todo) => {
        if (todo.completed && completed[todo.userId] === undefined) {
          completed[todo.userId] = 1;
        } else if (todo.completed) {
          completed[todo.userId] += 1;
        }
      });

      console.log(completed);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    console.error('Error:', error);
  }
});
