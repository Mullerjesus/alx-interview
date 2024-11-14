#!/usr/bin/node  

const request = require('request');  

const movieId = process.argv[2]; // Get the Movie ID from command line arguments  
const url = `https://swapi.dev/api/films/${movieId}/`; // API endpoint for the movie  

request(url, (error, response, body) => {  
    if (error) {  
        console.error('Error fetching movie:', error);  
        return;  
    }  

    const movie = JSON.parse(body);  
    const characters = movie.characters; // Array of character URLs  

    characters.forEach((characterUrl) => {  
        request(characterUrl, (err, res, charBody) => {  
            if (err) {  
                console.error('Error fetching character:', err);  
                return;  
            }  
            const character = JSON.parse(charBody);  
            console.log(character.name); // Print character name  
        });  
    });  
});
