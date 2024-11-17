#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command-line argument
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// API endpoint for the movie
const url = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to fetch movie details
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error(`Error: Failed to fetch data (status code: ${res.statusCode})`);
    return;
  }

  // Parse the response body
  const data = JSON.parse(body);

  // Check if characters exist
  if (!data.characters || data.characters.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  // Fetch each character's name in order
  const characters = data.characters;
  const fetchCharacterNames = (index) => {
    if (index >= characters.length) {
      return; // Done
    }

    // Fetch individual character data
    request(characters[index], (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }

      if (res.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      } else {
        console.error(`Failed to fetch character (status code: ${res.statusCode})`);
      }

      // Recursively fetch the next character
      fetchCharacterNames(index + 1);
    });
  };

  fetchCharacterNames(0); // Start fetching
});
