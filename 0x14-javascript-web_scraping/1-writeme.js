#!/usr/bin/node
// The above line is a shebang used in Unix-like systems to specify the interpreter for the script. It indicates that the script should be interpreted using the Node.js runtime.

const fs = require('fs');
// Import the built-in Node.js 'fs' module, which provides functions for working with the file system, including reading and writing files.

fs.writeFile(process.argv[2], process.argv[3], error => {
  // Use fs.writeFile() to write data to a file specified as the third command-line argument (process.argv[2]).
  // The data to be written is taken from the fourth command-line argument (process.argv[3]).

  if (error) {
    // If an error occurs during the write operation, the 'error' parameter will contain an error object.
    console.error(error);
    // Print the error message to the console using console.error().
  }
  }
});
