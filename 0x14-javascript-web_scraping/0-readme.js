#!/usr/bin/node
// The above line is a shebang used in Unix-like systems to specify the interpreter for the script. It indicates that the script should be interpreted using the Node.js runtime.

const fs = require('fs');
// Import the built-in Node.js 'fs' module, which provides functions for working with the file system, including reading and writing files.

fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Use fs.readFile() to read the contents of a file specified as a command-line argument (process.argv[2]).
  // 'utf8' specifies the encoding of the file being read (in this case, it's a plain text file).
  // A callback function is provided as the last argument, which will be executed once the file has been read.

  if (error) {
    // If an error occurs during the file read operation, the 'error' parameter will contain an error object.
    console.error('Error reading the file:', error);
    // Print the error message to the console using console.error().
  } else {
    // If the file is read successfully, the 'content' parameter will contain the contents of the file as a string.
    console.log(content);
    // Print the file content to the console using console.log().
  }
});
