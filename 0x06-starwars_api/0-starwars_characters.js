#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (err, res, charBody) => {
        if (err) reject(err);
        resolve(JSON.parse(charBody).name);
      });
    });
  };

  const displayCharacters = async () => {
    for (const url of characters) {
      try {
        const name = await fetchCharacter(url);
        console.log(name);
      } catch (err) {
        console.error(err);
      }
    }
  };

  displayCharacters();
});
