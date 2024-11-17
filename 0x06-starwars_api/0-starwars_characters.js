#!/usr/bin/env node  

const request = require('request');  

const movieId = process.argv[2];  

if (!movieId) {  
    console.log('Please provide a movie ID.');  
    process.exit(1);  
}  

request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {  
    if (error || response.statusCode !== 200) {  
        console.error('Error fetching data: ', error);  
        return;  
    }  
    const characters = JSON.parse(body).characters;  

    // Fetching and printing character names  
    characters.forEach(characterUrl => {  
        request(characterUrl, (error, response, body) => {  
            if (error || response.statusCode !== 200) {  
                console.error('Error fetching character data:', error);  
                return;  
            }  
            const name = JSON.parse(body).name;  
            console.log(name);  
        });  
    });  
});
