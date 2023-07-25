#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error.message);
    return;
  }

  const movieData = JSON.parse(body);
  console.log(`Characters of "${movieData.title}":`);

  // Use the map function and return the promises
  const characterPromises = movieData.characters.map((characterUrl) => {
    return new Promise((resolve, reject) => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(`Error fetching character data: ${charError.message}`);
          reject(charError);
        } else {
          const characterData = JSON.parse(charBody);
          resolve(characterData.name);
        }
      });
    });
  });

  Promise.all(characterPromises)
    .then((characterNames) => {
      console.log(characterNames.join('\n'));
    })
    .catch((error) => {
      console.error(error.message);
    });
});
